import csv
import json
from collections import Counter
from datetime import datetime, timezone
from freeze import HERE, ROOT, QUEUE, PRODUCER, sha

def load(name):
    return json.loads((HERE / name).read_text())

target, frozen, expansion = load('target_freeze.json'), load('qa_freeze.json'), load('qa_expansion_freeze.json')
assert sha(QUEUE) == target['original_queue_sha256'] == frozen['original_queue_sha256'] == expansion['original_queue_sha256']
assert sha(PRODUCER) == target['producer_sha256'] == frozen['producer_sha256'] == expansion['producer_sha256']
assert sha(HERE / 'delta_overlay25.csv') == frozen['primary_overlay_sha256'] == expansion['primary_overlay_sha256']
assert sha(HERE / 'qa_freeze.json') == expansion['qa_freeze_sha256']
assert sha(HERE / 'judgments.json') == frozen['judgments_sha256']
with QUEUE.open() as f:
    reader = csv.DictReader(f)
    original_fields = reader.fieldnames
    original = {r['occurrence_E_ID']: r for r in reader if r['occurrence_E_ID'] in target['target_ids']}
with (HERE / 'delta_overlay25.csv').open() as f:
    overlay = list(csv.DictReader(f))
assert [r['occurrence_E_ID'] for r in overlay] == target['target_ids']
assert [r['corrective_event_ID'] for r in overlay] == target['corrective_events']
assert [r['producer_event_ID_preserved'] for r in overlay] == target['producer_events_preserved']
for r in overlay:
    assert all(r[k] == original[r['occurrence_E_ID']][k] for k in original_fields)
    assert r['title'] and r['abstract_or_snippet']
    assert all(r[f'effective_R{i}_judgment'] for i in range(1,7))
    assert r['effective_claim_support'] == r['effective_methodological_confidence'] == 'UNASSESSED'
    assert r['effective_fulltext'] == r['effective_citations'] == 'NOT RUN'
    assert r['effective_stage1_disposition'] in ('ADVANCE', 'PENDING', 'X3')
qa = load('qa_judgments.json')
assert len({j['id'] for j in qa}) == len(qa) == 16
assert {j['id'] for j in qa} == set(frozen['selected_ids']) | set(expansion['target_ids'])
with (HERE / 'qa_results.csv').open('x', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(qa[0])); w.writeheader(); w.writerows(qa)
by_id = {j['id']: j for j in qa}
group_results = []
for g in frozen['groups']:
    assert g['selected_first_EID'] == min(g['members'])
    group_results.append(dict(g, result=by_id[g['selected_first_EID']]['result'], result_anchor=by_id[g['selected_first_EID']]['original_anchor']))
with (HERE / 'qa_group_results.json').open('x') as f:
    json.dump(group_results, f, indent=2); f.write('\n')
counts = {
    'created_utc': datetime.now(timezone.utc).isoformat(), 'count_basis': 'occurrences, not unique works',
    'frozen_targets':25, 'primary_original_export_checks_completed':25, 'original_export_missing':0,
    'effective_dispositions':dict(Counter(r['effective_stage1_disposition'] for r in overlay)),
    'ADVANCE':25, 'PENDING':0, 'X3':0, 'producer_disposition_changes':0,
    'six_question_judgments':150,
    'positive_explicit_R_counts':dict(Counter(rid for r in overlay for rid in r['effective_explicit_R_IDs'].split(';'))),
    'groups_frozen':18, 'groups_secondary_checked':18,
    'group_sample_distinct_occurrences_frozen':9, 'group_sample_distinct_occurrences_checked':9,
    'finite_expansion_frozen':7, 'finite_expansion_checked':7,
    'secondary_distinct_occurrences_checked':16,
    'secondary_result_counts':dict(Counter(j['result'] for j in qa)),
    'primary_only_occurrences_without_secondary_reread':[r['occurrence_E_ID'] for r in overlay if r['occurrence_E_ID'] not in by_id],
    'proposed_exclusions':0, 'exclusion_QA':'not applicable: no proposed exclusions',
    'fulltext_pass':'NOT RUN', 'citation_pass':'NOT RUN', 'claim_support':'UNASSESSED', 'methodological_confidence':'UNASSESSED',
    'identity_date_language_type':'unverified/pending for all 25; metadata proxies are not validation',
    'other_frozen_batch4_targets_unreviewed_by_this_task':75,
    'independent_human_review':'NOT DONE', 'shared_aggregate_or_gate_changes':'NONE',
}
with (HERE / 'counts.json').open('x') as f:
    json.dump(counts, f, indent=2); f.write('\n')
verification = {
    'original_queue_hash_unchanged':True, 'producer_hash_unchanged':True,
    'ordered_target_and_event_joins':True, 'all_original_fields_preserved':True,
    'all_25_nonempty_original_title_and_snippet':True,
    'all_150_R_judgments_present':True, 'QA_selection_exact_and_disjoint':True,
    'all_18_first_EID_group_selections_reproduced':True,
    'all_frozen_primary_hashes_match':True,
    'meaning':'mechanical integrity only, not source-method validation or independent scientific review',
}
with (HERE / 'verification.json').open('x') as f:
    json.dump(verification, f, indent=2); f.write('\n')
print(json.dumps(counts, indent=2))
