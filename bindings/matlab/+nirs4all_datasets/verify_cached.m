% SPDX-License-Identifier: MIT
function out = verify_cached(resolved_json, dir)
  % Re-verify a cached dataset directory against the contract's SHA-256s (JSON report).
  out = n4ds('verify_cached', resolved_json, dir);
end
