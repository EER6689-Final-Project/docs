"""Freeze prospective secondary selection. Does not author semantic QA."""
from pathlib import Path
import csv
import datetime
import hashlib
import json

own = Path(__file__).resolve().parent
path = own / 'secondary_freeze.json'
assert not path.exists(), 'Never overwrite a prospective freeze.'
rows = list(csv.DictReader((own / 'overlay.csv').open()))
producer = {r['occurrence_E_ID']: r for r in csv.DictReader((own.parent / 'Scholar Batch6/overlay.csv').open())}

def type_proxy(r):
    m = r['raw_record_metadata'].lower()
    if 'arxiv' in m or 'ssrn' in m:
        return 'PREPRINT_PLATFORM_PROXY'
    if r['title'].startswith('[B]') or any(s in m for s in ['handbook', 'books.google', 'igi-global']):
        return 'BOOK_CHAPTER_PROXY'
    if any(s in m for s in ['conference', 'proceedings', 'globecom', 'edmedia', 'ieee/rsj', 'isat2011']):
        return 'PROCEEDINGS_LABEL_PROXY'
    if any(s in m for s in ['repository', 'repositorio', 'scholaris', 'proquest', 'ela.kpi', 'unbscholar', 'dbc.wroc', 'pearl.plymouth']):
        return 'REPOSITORY_OR_THESIS_PROXY'
    if any(s in m for s in ['journal', 'sensors', 'scientific reports', 'optometry', 'ophthalmology', 'eye', 'measurement', 'symmetry', 'computers', 'maritime engineering', 'advanced electromagnetics', 'organic coatings', 'information and software', 'bmj', 'transactions']):
        return 'JOURNAL_LABEL_PROXY'
    return 'UNRESOLVED_METADATA_TYPE_PROXY'

groups = {}
for r in rows:
    eid = r['occurrence_E_ID']
    for owner in ['producer', 'Sol']:
        positive = ([f'R{n}' for n in range(1,7) if not producer[eid][f'producer_R{n}_judgment'].startswith('Not established')]
                    if owner == 'producer' else r['effective_positive_Rs'].split(';'))
        for rid in filter(None, positive):
            groups.setdefault(f'{owner}/{rid}/{type_proxy(r)}', []).append(eid)
frozen_groups = {k: {'members': sorted(v), 'selected_first_EID': min(v), 'nonselected_count': len(v)-1} for k,v in sorted(groups.items())}
px = [r['occurrence_E_ID'] for r in rows if r['effective_producer_disposition']=='X3']
sx = [r['occurrence_E_ID'] for r in rows if r['effective_disposition']=='X3']
patterns = {
    'domain_ban_native_human_analogues_vs_exact_transfer': [r['occurrence_E_ID'] for r in rows],
    'experimental_repeated_word_not_R4_comparison_not_R5': [r['occurrence_E_ID'] for r in rows],
    'generic_score_web_developer_words_construct_not_assumed': [r['occurrence_E_ID'] for r in rows],
    'contaminated_citation_only_method_poor_snippet_not_fulltext': [r['occurrence_E_ID'] for r in rows],
    'date_language_type_identity_unverified_not_invented_exclusions': [r['occurrence_E_ID'] for r in rows],
}
data = {'timestamp_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'status': 'FROZEN AFTER primary pass, BEFORE actual secondary rereads',
        'primary_overlay_sha256': hashlib.sha256((own/'overlay.csv').read_bytes()).hexdigest(),
        'primary_authored_checks_sha256': hashlib.sha256((own/'authored_checks.tsv').read_bytes()).hexdigest(),
        'producer_X3': px, 'Sol_proposed_X3': sx, 'groups': frozen_groups,
        'grouping_rule': 'Explicit positive R tokens only: producer per-R field not starting Not established; Sol authored positive_Rs. Cross with declared bibliographic metadata type proxy. No query-membership R inference.',
        'type_proxy_rule': 'Ordered platform/label proxies only; preprint, book/chapter, proceedings, repository/thesis, journal, unresolved. Not verified original type; [PDF]/[HTML] do not establish type.',
        'type_proxy_assignments': {r['occurrence_E_ID']: type_proxy(r) for r in rows},
        'first_EID_group_samples': sorted({g['selected_first_EID'] for g in frozen_groups.values()}),
        'finite_common_error_pattern_expansions': patterns,
        'secondary_selected_EIDs': [r['occurrence_E_ID'] for r in rows],
        'selection_reason': 'All producer and Sol X3 plus first per explicit positive R/type proxy group, expanded prospectively to all 100 for finite common error patterns; no unchecked cohort remains after completed rereads.',
        'claim_QC_boundary': 'Occurrence/type proxies only, not canonical S-ID/C-ID claim groups or section 9 passage QC. Separate-pass AI self-audit; not independent human review.'}
path.write_text(json.dumps(data, indent=2)+'\n')
print('Frozen secondary targets:',len(rows),'producer X3',len(px),'Sol X3',len(sx),'groups',len(groups),'distinct firsts',len(data['first_EID_group_samples']))
