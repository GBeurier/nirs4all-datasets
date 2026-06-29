% SPDX-License-Identifier: MIT
function out = prepare_raw(request_json, opts_json)
  % Prepare already-retrieved raw resources with the Rust reader stack (JSON status string).
  if nargin < 2, opts_json = ''; end
  out = n4ds('prepare_raw', request_json, opts_json);
end
