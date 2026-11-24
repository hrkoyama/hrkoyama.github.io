"""Compile the shipped portable source into a disposable directory, never into results."""
import ctypes
import hashlib
import os
from pathlib import Path
import platform
import shlex
import subprocess
import tempfile
import numpy as np

FLAGS=['-O2','-std=c++17','-ffp-contract=off','-fPIC','-Wall','-Wextra','-Werror']
HISTORY_NAMES=['mass','momentum_x','momentum_y','boundary_mass','boundary_px','boundary_py',
               'body_fx','body_fy','body_torque','max_mach','min_rho','max_rho','min_population',
               'wall_mass','open_mass','wall_torque']

class NativeFailure(ArithmeticError):
    def __init__(self,code,status,f,history):
        super().__init__(f'Native LBM failure code={code}, status={status.tolist()}')
        self.payload=dict(f=f.copy(),history=history[:int(status[0])].copy(),native_status=status.copy())

class Native:
    def __init__(self,root=None):
        root=Path(root or Path(__file__).resolve().parent)
        self.temporary=tempfile.TemporaryDirectory(prefix='atlas-lbm-',dir=os.environ.get('TMPDIR'))
        destination=Path(self.temporary.name)/('kernel.dylib' if platform.system()=='Darwin' else 'kernel.so')
        compiler=shlex.split(os.environ.get('CXX','c++'))
        command=[*compiler,*FLAGS,'-dynamiclib' if platform.system()=='Darwin' else '-shared',
                 str(root/'kernel.cpp'),'-o',str(destination)]
        result=subprocess.run(command,capture_output=True,text=True,check=False,timeout=15)
        self.compile_receipt=dict(command=command,returncode=result.returncode,stdout=result.stdout,
                                  stderr=result.stderr,source_sha256=hashlib.sha256((root/'kernel.cpp').read_bytes()).hexdigest())
        if result.returncode:raise RuntimeError('C++17 compilation failed: '+result.stderr)
        self.library=ctypes.CDLL(str(destination));self.function=self.library.lbm_advance
        I=ctypes.c_int;D=ctypes.c_double;PI=np.ctypeslib.ndpointer(dtype=np.int32,flags='C_CONTIGUOUS')
        PD=np.ctypeslib.ndpointer(dtype=np.float64,flags='C_CONTIGUOUS')
        self.function.argtypes=[I,I,D,PI,PI,PI,PD,PD,PD,PI,I,PI,I,PD,PD,PD,PI]
        self.function.restype=I

    def advance(self,f,geometry,tau,steps):
        if f.dtype!=np.float64 or not f.flags.c_contiguous or f.shape!=(9,geometry['n']):
            raise ValueError('Native state must be contiguous float64[9,n]')
        if type(steps) is not int or steps<0 or not np.isfinite(tau) or tau<=.5:
            raise ValueError('Invalid fixed steps/tau')
        h=np.zeros((steps,16),dtype=np.float64);status=np.zeros(3,dtype=np.int32)
        g=geometry
        code=self.function(g['n'],steps,tau,g['source'],g['back'],g['kind'],g['fraction'],
                           g['wall_dot'],g['lever'],g['inlet'],len(g['inlet']),g['outlet'],
                           len(g['outlet']),g['inlet_speed'],f,h,status)
        if code:raise NativeFailure(code,status,f,h)
        if not np.all(np.isfinite(f)) or not np.all(np.isfinite(h)):
            raise NativeFailure(6,status,f,h)
        return h
