% SPDX-License-Identifier: MIT
% Smoke test for the MATLAB/Octave binding (offline: resolve / verify / abi).
% Assumes the `n4ds` mex is on the path (run from bindings/matlab after build.m).
template = ['{`schema`:`1.0`,`n_datasets`:1,`datasets`:{`demo`:{' ...
  '`tier`:`public`,' ...
  '`dataverse`:{`instance`:`https://dv.example`,`doi`:`10.70112/ABC`,`dataset_version`:`1.0`},' ...
  '`files`:[{`name`:`X.parquet`,`relpath`:`canonical/sources/X.parquet`,`directory_label`:`canonical/sources`,`sha256`:`aa`,`size`:9,`file_id`:42}],' ...
  '`origins`:[],`descriptor`:{`id`:`demo`}}}}'];
index = strrep(template, '`', '"');

% resolve -> a contract that mentions the tier + file id.
contract = n4ds('resolve', index, 'demo');
assert(~isempty(strfind(contract, '"tier"')), 'contract missing tier');          %#ok<STREMP>
assert(~isempty(strfind(contract, '"file_id":42')), 'contract missing file_id'); %#ok<STREMP>

% verify_cached on an empty dir reports the file missing.
report = n4ds('verify_cached', contract, tempdir());
assert(~isempty(strfind(report, '"missing"')), 'report should mark the file missing'); %#ok<STREMP>

% an unknown id is rejected.
rejected = false;
try
  n4ds('resolve', index, 'nope');
catch
  rejected = true;
end
assert(rejected, 'unknown id was not rejected');

assert(~isempty(n4ds('abi_version')), 'empty abi_version');

disp('matlab/octave binding smoke OK');
