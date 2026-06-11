/* SPDX-License-Identifier: MIT
 * MATLAB/Octave MEX glue for the nirs4all-datasets C ABI.
 *
 *   n4ds('resolve',       index_json, dataset_id)   -> char  (download contract)
 *   n4ds('fetch',         resolved_json[, opts_json]) -> char (fetch status)
 *   n4ds('verify_cached', resolved_json, dir)       -> char  (verify report)
 *   n4ds('abi_version')                             -> char
 *
 * Mirrors the verified R glue (bindings/r/nirs4alldatasets/src/n4ds.c) against the
 * same frozen header: a per-call context carries the error buffer; a non-OK status
 * becomes a MATLAB/Octave error; owned result strings are copied out and freed with
 * n4ds_string_free. Build with bindings/matlab/build.m (needs the prebuilt
 * libnirs4all_datasets_capi). */
#include "mex.h"
#include "nirs4all_datasets.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static const char *opt_arg(int nrhs, const mxArray *prhs[], int idx) {
    if (idx >= nrhs || mxIsEmpty(prhs[idx]) || !mxIsChar(prhs[idx]))
        return NULL;
    return mxArrayToString(prhs[idx]); /* leaks per call; the MEX process is short-lived */
}

static void raise_ctx(struct n4ds_context_t *ctx) {
    const char *msg = n4ds_context_last_error(ctx);
    char buf[1024];
    snprintf(buf, sizeof(buf), "%s", msg ? msg : "unknown error");
    n4ds_context_destroy(ctx);
    mexErrMsgIdAndTxt("n4ds:error", "%s", buf);
}

static mxArray *owned_to_mx(char *owned) {
    mxArray *out = mxCreateString(owned ? owned : "");
    n4ds_string_free(owned);
    return out;
}

void mexFunction(int nlhs, mxArray *plhs[], int nrhs, const mxArray *prhs[]) {
    if (nlhs > 1)
        mexErrMsgIdAndTxt("n4ds:nargout", "at most one output argument is returned");
    if (nrhs < 1 || !mxIsChar(prhs[0]))
        mexErrMsgIdAndTxt("n4ds:arg", "first argument must be a command string");
    char *cmd = mxArrayToString(prhs[0]);

    struct n4ds_context_t *ctx = NULL;
    if (n4ds_context_create(&ctx) != N4DS_OK)
        mexErrMsgIdAndTxt("n4ds:ctx", "failed to create context");

    if (strcmp(cmd, "abi_version") == 0) {
        n4ds_context_destroy(ctx);
        plhs[0] = owned_to_mx(n4ds_abi_version());
        return;
    }

    const char *a1 = opt_arg(nrhs, prhs, 1);
    const char *a2 = opt_arg(nrhs, prhs, 2);
    char *out = NULL;
    enum n4ds_status_t st;
    if (strcmp(cmd, "resolve") == 0) {
        if (a1 == NULL || a2 == NULL) {
            n4ds_context_destroy(ctx);
            mexErrMsgIdAndTxt("n4ds:arg", "resolve requires (index_json, dataset_id)");
        }
        st = n4ds_resolve(ctx, a1, a2, &out);
    } else if (strcmp(cmd, "fetch") == 0) {
        if (a1 == NULL) {
            n4ds_context_destroy(ctx);
            mexErrMsgIdAndTxt("n4ds:arg", "fetch requires resolved_json");
        }
        st = n4ds_fetch(ctx, a1, a2 ? a2 : "", &out);
    } else if (strcmp(cmd, "verify_cached") == 0) {
        if (a1 == NULL || a2 == NULL) {
            n4ds_context_destroy(ctx);
            mexErrMsgIdAndTxt("n4ds:arg", "verify_cached requires (resolved_json, dir)");
        }
        st = n4ds_verify_cached(ctx, a1, a2, &out);
    } else {
        n4ds_context_destroy(ctx);
        mexErrMsgIdAndTxt("n4ds:cmd", "unknown command '%s'", cmd);
        return;
    }
    if (st != N4DS_OK)
        raise_ctx(ctx);
    n4ds_context_destroy(ctx);
    plhs[0] = owned_to_mx(out);
}
