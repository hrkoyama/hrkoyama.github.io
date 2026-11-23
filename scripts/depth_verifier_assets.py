"""Render the self-contained public verifier's reviewed group allowlist."""
from atlas_registration import registered_groups


def render_depth_verifier(root):
    source = root/'scripts/templates/verify-depth-public.py.tmpl'
    text = source.read_text()
    token = '{{registered_groups}}'
    if text.count(token) != 1:
        raise ValueError('Expected one explicit verifier registration token')
    text = text.replace(token, repr(registered_groups(root)))
    lines = text.splitlines(keepends=True)
    lines.insert(1, '# Generated from scripts/templates/verify-depth-public.py.tmpl; edit that template.\n')
    (root/'scripts/verify-depth-public.py').write_text(''.join(lines))
