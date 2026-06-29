% SPDX-License-Identifier: MIT
function out = retrieve_raw(request_json, opts_json)
  % Retrieve raw origin resources into the cache (JSON status string).
  if nargin < 2, opts_json = ''; end
  out = n4ds('retrieve_raw', request_json, opts_json);
end
