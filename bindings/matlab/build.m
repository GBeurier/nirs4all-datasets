% SPDX-License-Identifier: MIT
% Build the n4ds MEX against the prebuilt nirs4all-datasets-capi cdylib.
% Set the env vars first (build_and_test.sh does this):
%   N4DS_INCLUDE  -> dir containing nirs4all_datasets.h
%   N4DS_CAPI_DIR -> dir containing libnirs4all_datasets_capi.{so,dylib,dll}
% Works in both MATLAB and Octave (mex is provided by both).
inc = getenv('N4DS_INCLUDE');
libdir = getenv('N4DS_CAPI_DIR');
here = fileparts(mfilename('fullpath'));
src = fullfile(here, 'n4ds.c');
mex(src, ...
    ['-I' inc], ...
    ['-L' libdir], '-lnirs4all_datasets_capi', ...
    ['-Wl,-rpath,' libdir], ...
    '-output', fullfile(here, 'n4ds'));
