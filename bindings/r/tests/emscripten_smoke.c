/* SPDX-License-Identifier: CECILL-2.1 OR AGPL-3.0-or-later
 * Run against the actual WebR-target static library, not a native mock:
 * emcc emscripten_smoke.c -I../nirs4alldatasets/src path/to/libnirs4all_datasets_capi.a \
 *   -sALLOW_MEMORY_GROWTH=1 -sEXIT_RUNTIME=1 -o smoke.js && node smoke.js
 */
#include "nirs4all_datasets.h"
#include <assert.h>
#include <stdio.h>
#include <string.h>
#include <sys/stat.h>
#include <unistd.h>

#ifndef __EMSCRIPTEN__
#error "This smoke must run against the actual Emscripten target"
#endif

static void write_file(const char *path, const char *text) {
    FILE *file = fopen(path, "wb");
    assert(file);
    assert(fwrite(text, 1, strlen(text), file) == strlen(text));
    assert(fclose(file) == 0);
}

int main(void) {
    n4ds_context_t *ctx = NULL;
    char *contract = NULL, *out = NULL;
    const char *index = "{\"schema\":\"1.0\",\"n_datasets\":1,\"datasets\":{\"demo\":{"
        "\"tier\":\"public\",\"dataverse\":{\"instance\":\"https://dv.example\",\"doi\":\"10.70112/ABC\",\"dataset_version\":\"1.0\"},"
        "\"files\":[{\"name\":\"data.txt\",\"relpath\":\"data.txt\",\"directory_label\":\"\","
        "\"sha256\":\"d79d9fd44ad034758fbdc3b2fa305894e98f111aae32efeb2c70a3b97cd0a456\",\"size\":10,\"file_id\":42}],\"origins\":[]}}}";
    assert(n4ds_context_create(&ctx) == N4DS_OK);
    assert(n4ds_check_abi_compatibility(0, 3) == N4DS_OK);
    assert(n4ds_resolve(ctx, index, "demo", &contract) == N4DS_OK);
    mkdir("/cache", 0700);
    mkdir("/cache/demo", 0700);
    assert(n4ds_verify_cached(ctx, contract, "/cache/demo", &out) == N4DS_OK);
    assert(strstr(out, "\"missing\""));
    n4ds_string_free(out);

    write_file("/cache/demo/data.txt", "good-bytes");
    assert(n4ds_verify_cached(ctx, contract, "/cache/demo", &out) == N4DS_OK);
    assert(strstr(out, "\"ok\":true"));
    n4ds_string_free(out);
    assert(n4ds_fetch(ctx, contract, "{\"cache_dir\":\"/cache\"}", &out) == N4DS_OK);
    assert(strstr(out, "\"cached\""));
    n4ds_string_free(out);

    write_file("/cache/demo/data.txt", "tampered");
    assert(n4ds_verify_cached(ctx, contract, "/cache/demo", &out) == N4DS_OK);
    assert(strstr(out, "\"corrupt\""));
    n4ds_string_free(out);
    assert(unlink("/cache/demo/data.txt") == 0);
    assert(n4ds_fetch(ctx, contract, "{\"cache_dir\":\"/cache\",\"token\":\"private-header\"}", &out) == N4DS_ERR_HTTP);
    assert(out == NULL);
    assert(strstr(n4ds_context_last_error(ctx), "blocking HTTP is unavailable in WebR"));
    assert(!strstr(n4ds_context_last_error(ctx), "private-header"));

    mkdir("/cache/demo/raw", 0700);
    mkdir("/cache/demo/raw/official", 0700);
    write_file("/cache/demo/raw/official/table.csv", "a;b\n1;2\n3;4\n");
    const char *request = "{\"dataset_id\":\"demo\",\"route\":{\"id\":\"official\",\"method\":\"raw_retrieve\","
        "\"provider\":\"url\",\"locator\":\"https://example.test/table.csv\",\"resources\":[{\"id\":\"table\","
        "\"selector\":{\"kind\":\"direct_url\",\"value\":\"https://example.test/table.csv\"},"
        "\"file_name\":\"table.csv\",\"format\":\"csv\"}]}}";
    assert(n4ds_prepare_raw(ctx, request, "{\"cache_dir\":\"/cache\"}", &out) == N4DS_OK);
    assert(strstr(out, "\"ok\":true"));
    assert(strstr(out, "\"engine\":\"nirs4all_io\""));
    assert(strstr(out, "\"n_rows\":2"));
    n4ds_string_free(out);
    n4ds_string_free(contract);
    n4ds_context_destroy(ctx);
    puts("WebR target: resolve, missing/valid/corrupt integrity, cache hit, explicit HTTP refusal, native CSV preparation OK");
    return 0;
}
