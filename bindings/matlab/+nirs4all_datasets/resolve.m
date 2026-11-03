% SPDX-License-Identifier: CECILL-2.1 OR AGPL-3.0-or-later
function out = resolve(index_json, dataset_id)
  % Resolve a dataset id against an index JSON to its download contract (JSON string).
  out = n4ds('resolve', index_json, dataset_id);
end
