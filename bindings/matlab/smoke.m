% SPDX-License-Identifier: MIT
% Smoke test for the MATLAB/Octave binding (offline: resolve / verify / abi).
% Assumes the `n4ds` mex is on the path (run from bindings/matlab after build.m).
template = ['{`schema`:`1.0`,`n_datasets`:1,`datasets`:{`demo`:{' ...
  '`tier`:`public`,' ...
  '`dataverse`:{`instance`:`https://dv.example`,`doi`:`10.70112/ABC`,`dataset_version`:`1.0`},' ...
  '`files`:[{`name`:`X.parquet`,`relpath`:`canonical/sources/X.parquet`,`directory_label`:`canonical/sources`,`sha256`:`aa`,`size`:9,`file_id`:42}],' ...
  '`origins`:[],' ...
  '`retrieval`:{`schema_version`:`1.0`,`status`:`raw_reproducible`,`routes`:[{`id`:`raw`,`method`:`raw_retrieve`,`provider`:`url`,`locator`:`https://example.test/raw.csv`,`resources`:[{`id`:`raw`,`selector`:{`kind`:`direct_url`,`value`:`https://example.test/raw.csv`}}]}]},' ...
  '`descriptor`:{`id`:`demo`,`retrieval`:{`schema_version`:`1.0`,`status`:`raw_reproducible`,`routes`:[]}}}}}'];
index = strrep(template, '`', '"');

% resolve -> a contract that mentions the tier + file id.
contract = n4ds('resolve', index, 'demo');
assert(~isempty(strfind(contract, '"tier"')), 'contract missing tier');          %#ok<STREMP>
assert(~isempty(strfind(contract, '"file_id":42')), 'contract missing file_id'); %#ok<STREMP>
assert(~isempty(strfind(contract, '"retrieval"')), 'contract missing retrieval'); %#ok<STREMP>

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

% retrieve_raw rejects non-automatic routes without network.
manual_request = strrep('{`dataset_id`:`demo`,`route`:{`id`:`manual`,`method`:`manual`,`provider`:`manual`,`access`:`manual`,`locator`:`https://example.org`}}', '`', '"');
rejected = false;
try
  n4ds('retrieve_raw', manual_request, ['{"cache_dir":"' tempdir() '"}']);
catch
  rejected = true;
end
assert(rejected, 'manual route was not rejected');

% prepare_raw shares the same route validation and rejects manual routes.
rejected = false;
try
  n4ds('prepare_raw', manual_request, ['{"cache_dir":"' tempdir() '"}']);
catch
  rejected = true;
end
assert(rejected, 'manual route was not rejected by prepare_raw');

assert(~isempty(n4ds('abi_version')), 'empty abi_version');

disp('matlab/octave binding smoke OK');
