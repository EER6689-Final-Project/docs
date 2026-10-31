import json
from datetime import datetime, timezone
from freeze import HERE, QUEUE, PRODUCER, sha

receipt = {
    'created_utc': datetime.now(timezone.utc).isoformat(),
    'phase': 'before additional secondary original-export rereads',
    'reason': 'Finite risk expansion for producer extrapolation from reference-list/fragmentary snippets and unsupported repetition/correlation inferences; corrected in primary, now checked in a separate pass. No final primary disposition discrepancy found in the nine frozen group selections.',
    'target_ids': ['E-0704','E-0705','E-0711','E-0713','E-0717','E-0718','E-0724'],
    'pattern_membership': {
        'reference-list snippet same-title companion to sampled E-0720': ['E-0704'],
        'weak/absent repeat structure or truncated method interpretation': ['E-0705','E-0711','E-0713','E-0717','E-0718'],
        'truncated correlation statement previously read as warning': ['E-0724'],
    },
    'original_queue_sha256': sha(QUEUE), 'producer_sha256': sha(PRODUCER),
    'primary_overlay_sha256': sha(HERE / 'delta_overlay25.csv'),
    'qa_freeze_sha256': sha(HERE / 'qa_freeze.json'),
    'boundary': 'Only E-0700–E-0724; no other batch targets or full texts',
}
with (HERE / 'qa_expansion_freeze.json').open('x') as f:
    json.dump(receipt, f, indent=2); f.write('\n')
print(json.dumps(receipt, indent=2))
