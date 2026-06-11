% SPDX-License-Identifier: MIT
function out = resolve(index_json, dataset_id)
  % Resolve a dataset id against an index JSON to its download contract (JSON string).
  out = n4ds('resolve', index_json, dataset_id);
end
