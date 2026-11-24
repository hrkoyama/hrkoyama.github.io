"""Fresh-output fixed-source Bratu runner; no reference download or hidden calibration."""
import argparse,hashlib,json,time,traceback
from pathlib import Path
import numpy as np
from experiments import run_continuation,run_jfnk
from io_contract import dump


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def main():
    root=Path(__file__).resolve().parent;parser=argparse.ArgumentParser();parser.add_argument('--input',type=Path,default=root/'inputs.json');parser.add_argument('--output',type=Path,required=True);a=parser.parse_args()
    contract=json.loads((root/'pre-run-contract.json').read_text())
    for name,h in contract['files_sha256'].items():
        if sha(root/name)!=h:raise ValueError('Frozen source changed:'+name)
    if sha(a.input)!=contract['files_sha256']['inputs.json']:raise ValueError('Fixed input only')
    if a.output.exists() and any(a.output.iterdir()):raise ValueError('Fresh output required')
    a.output.mkdir(parents=True,exist_ok=True);start=time.monotonic();cases=[];failure=None;inputs=json.loads(a.input.read_text());limits=json.loads((root/'acceptance.json').read_text())
    try:
        run_continuation(a.output,inputs['continuation'],limits['continuation'],cases)
        run_jfnk(a.output,inputs['jfnk'],limits['jfnk'],cases)
    except Exception as e:
        failure=dict(type=type(e).__name__,message=str(e));(a.output/'failure-traceback.txt').write_text(traceback.format_exc())
        if getattr(e,'arrays',None):np.savez_compressed(a.output/'failed-candidate.npz',**e.arrays)
    ids=contract['case_ids'];count=sum(len(c['checks']) for c in cases)
    passed=failure is None and {c['id'] for c in cases}==set(ids) and all(c['passed'] for c in cases) and count==contract['planned_case_gates']
    result=dict(schema_version=1,passed=bool(passed),termination='fixed_budget_completed' if passed else 'calculation_failed',failure=failure,
                checks={i:next((c['passed'] for c in cases if c['id']==i),False) for i in ids},cases=cases,numerical_gate_count=count,
                input_sha256=sha(a.input),source_sha256={n:sha(root/n) for n in [*contract['files_sha256'],'pre-run-contract.json']},duration_seconds=time.monotonic()-start)
    dump(a.output/'result.json',result);print(json.dumps(dict(passed=bool(passed),gates=count,failure=failure)));return 0 if passed else 1


if __name__=='__main__':raise SystemExit(main())
