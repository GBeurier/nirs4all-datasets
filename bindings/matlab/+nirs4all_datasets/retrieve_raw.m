% SPDX-License-Identifier: CECILL-2.1 OR AGPL-3.0-or-later
function out = retrieve_raw(request_json, opts_json)
  % Retrieve raw origin resources into the cache (JSON status string).
  if nargin < 2, opts_json = ''; end
  out = n4ds('retrieve_raw', request_json, opts_json);
end
