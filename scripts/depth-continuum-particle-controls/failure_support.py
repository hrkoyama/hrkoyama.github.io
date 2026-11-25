"""Portable failure-state ownership and NPZ-first strict-JSON persistence."""
import hashlib,json,math
from pathlib import Path
import numpy as np


class NumericalFailure(RuntimeError):
    def __init__(self,reason,diagnostics=None,state_arrays=None):
        super().__init__(reason)
        self.diagnostics=diagnostics or {}
        self.state_arrays=state_arrays or {}


def own_failure(error,stage,physical_time,step,start_arrays,failed_arrays):
    failure=error if isinstance(error,NumericalFailure) else NumericalFailure(str(error),{'cause_type':type(error).__name__})
    failure.diagnostics.update(stage=stage,physical_time=physical_time,step=step)
    failure.state_arrays.update({key:np.array(value,copy=True) for key,value in start_arrays.items()})
    failure.state_arrays.update({key:np.array(value,copy=True) for key,value in failed_arrays.items()})
    return failure


def diagnostic_json(value):
    """Only failure diagnostics are labelled; scientific results stay strict."""
    if isinstance(value,np.ndarray):return diagnostic_json(value.tolist())
    if isinstance(value,np.generic):return diagnostic_json(value.item())
    if isinstance(value,float) and not math.isfinite(value):
        return 'NONFINITE:NaN' if math.isnan(value) else ('NONFINITE:+Infinity' if value>0 else 'NONFINITE:-Infinity')
    if isinstance(value,dict):return {str(k):diagnostic_json(v) for k,v in value.items()}
    if isinstance(value,(list,tuple)):return [diagnostic_json(x) for x in value]
    if value is None or isinstance(value,(str,bool,int,float)):return value
    return str(value)


def persist_failure(directory,error,traceback_text=''):
    directory=Path(directory);directory.mkdir(parents=True,exist_ok=True)
    raw={key:np.asarray(value) for key,value in getattr(error,'state_arrays',{}).items()}
    payload={'type':type(error).__name__,'message':str(error),'diagnostics':diagnostic_json(getattr(error,'diagnostics',{})),'traceback':traceback_text}
    # Deliberately BEFORE JSON: NaN/Inf remain exact numeric bytes in raw arrays.
    if raw:
        if not all(np.issubdtype(value.dtype,np.number) or value.dtype==np.dtype(bool) for value in raw.values()):
            raise TypeError('Failure arrays must be numeric, never pickled objects')
        target=directory/'failure-state.npz';np.savez_compressed(target,**raw)
        payload['raw_state']={'file':target.name,'sha256':hashlib.sha256(target.read_bytes()).hexdigest(),'contains_original_nonfinite_values':any(not np.isfinite(value).all() for value in raw.values())}
    (directory/'failure.json').write_text(json.dumps(payload,ensure_ascii=False,indent=2,allow_nan=False)+'\n')
    return payload
