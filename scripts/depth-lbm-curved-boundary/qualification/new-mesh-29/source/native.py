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

class NativeCompileFailure(RuntimeError):
    def __init__(self,receipt):
        super().__init__('C++17 compiler did not complete successfully; see compiler.json')
        self.receipt=receipt

class Native:
    def __init__(self,root=None):
        root=Path(root or Path(__file__).resolve().parent)
        self.temporary=tempfile.TemporaryDirectory(prefix='atlas-lbm-',dir=os.environ.get('TMPDIR'))
        destination=Path(self.temporary.name)/('kernel.dylib' if platform.system()=='Darwin' else 'kernel.so')
        compiler=shlex.split(os.environ.get('CXX','c++'))
        command=[*compiler,*FLAGS,'-dynamiclib' if platform.system()=='Darwin' else '-shared',
                 str(root/'kernel.cpp'),'-o',str(destination)]
        self.compile_receipt=dict(command=command,returncode=None,stdout='',stderr='',
                                  timed_out=False,timeout_seconds=15,
                                  source_sha256=hashlib.sha256((root/'kernel.cpp').read_bytes()).hexdigest())
        try:
            result=subprocess.run(command,capture_output=True,text=True,check=False,timeout=15)
        except subprocess.TimeoutExpired as error:
            def decoded(value):
                return value.decode('utf-8',errors='replace') if isinstance(value,bytes) else (value or '')
            self.compile_receipt.update(timed_out=True,stdout=decoded(error.stdout),stderr=decoded(error.stderr))
            self.close()
            raise NativeCompileFailure(self.compile_receipt) from error
        except OSError as error:
            self.compile_receipt.update(error_type=type(error).__name__,error=str(error))
            self.close()
            raise NativeCompileFailure(self.compile_receipt) from error
        self.compile_receipt.update(returncode=result.returncode,stdout=result.stdout,stderr=result.stderr)
        if result.returncode:
            self.close()
            raise NativeCompileFailure(self.compile_receipt)
        self.library=ctypes.CDLL(str(destination));self.function=self.library.lbm_advance
        I=ctypes.c_int;D=ctypes.c_double;PI=np.ctypeslib.ndpointer(dtype=np.int32,flags='C_CONTIGUOUS')
        PD=np.ctypeslib.ndpointer(dtype=np.float64,flags='C_CONTIGUOUS')
        self.function.argtypes=[I,I,D,PI,PI,PI,PI,I,I,PD,PD,PD,PI,I,PI,I,PD,PD,PD,PI]
        self.function.restype=I

    def close(self):
        """Explicitly release the temporary compiler directory; never filter warnings."""
        self.temporary.cleanup()

    def advance(self,f,geometry,tau,steps):
        if f.dtype!=np.float64 or not f.flags.c_contiguous or f.shape!=(9,geometry['n']):
            raise ValueError('Native state must be contiguous float64[9,n]')
        if type(steps) is not int or steps<0 or not np.isfinite(tau) or tau<=.5:
            raise ValueError('Invalid fixed steps/tau')
        h=np.zeros((steps,16),dtype=np.float64);status=np.zeros(3,dtype=np.int32)
        g=geometry
        code=self.function(g['n'],steps,tau,g['source'],g['back'],g['back2'],g['kind'],
                           g['interpolation_order'],g['outlet_mode'],g['fraction'],
                           g['wall_dot'],g['lever'],g['inlet'],len(g['inlet']),g['outlet'],
                           len(g['outlet']),g['inlet_speed'],f,h,status)
        if code:raise NativeFailure(code,status,f,h)
        if not np.all(np.isfinite(f)) or not np.all(np.isfinite(h)):
            raise NativeFailure(6,status,f,h)
        return h
