% SPDX-License-Identifier: MIT
function out = fetch(resolved_json, opts_json)
  % Download + SHA-256-verify a resolved dataset into the cache (JSON status string).
  if nargin < 2, opts_json = ''; end
  out = n4ds('fetch', resolved_json, opts_json);
end
