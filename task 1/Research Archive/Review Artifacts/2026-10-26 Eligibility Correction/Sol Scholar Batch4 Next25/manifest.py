import json
from datetime import datetime, timezone
from freeze import HERE, sha

if __name__ == '__main__':
    manifest = {
        'created_utc': datetime.now(timezone.utc).isoformat(),
        'scope': 'this subtree only; immutable inputs separately frozen in target_freeze.json',
        'algorithm': 'SHA-256',
        'self_excluded': 'file_manifest.json',
        'files': {str(p.relative_to(HERE)): sha(p) for p in sorted(HERE.iterdir())
                  if p.is_file() and p.name != 'file_manifest.json'},
    }
    with (HERE/'file_manifest.json').open('x') as f:
        json.dump(manifest, f, indent=2)
        f.write('\n')
    assert all(sha(HERE/name) == value for name,value in manifest['files'].items())
    print(f"Verified {len(manifest['files'])} deliverable hashes.")
