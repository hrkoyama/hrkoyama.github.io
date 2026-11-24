"""Fixed cell/link geometry. Coordinates are physical; f and wall speeds use lattice units."""
import numpy as np

C=np.array([[0,0],[1,0],[0,1],[-1,0],[0,-1],[1,1],[-1,1],[-1,-1],[1,-1]],dtype=np.int32)
OPP=np.array([0,3,4,1,2,7,8,5,6],dtype=np.int32)
W=np.array([4/9]+[1/9]*4+[1/36]*4)

def equilibrium(rho,u):
    cu=np.einsum('qd,dn->qn',C,u)
    return np.ascontiguousarray(W[:,None]*rho*(1+3*cu+4.5*cu**2-1.5*np.sum(u*u,axis=0)))

def moments(f):
    rho=np.sum(f,axis=0)
    if not np.all(np.isfinite(f)) or np.any(rho<=0):raise ArithmeticError('Nonpositive/nonfinite LBM state')
    return rho,np.einsum('qd,qn->dn',C,f)/rho

def circle_fraction(point,direction,center,radius):
    r=np.asarray(point)-center;d=np.asarray(direction)
    aa=float(np.sum(d*d));bb=2*float(np.sum(r*d));cc=float(np.sum(r*r)-radius**2)
    disc=bb*bb-4*aa*cc
    if disc<0:raise ValueError('Circle-link discriminant negative')
    roots=[(-bb-np.sqrt(disc))/(2*aa),(-bb+np.sqrt(disc))/(2*aa)]
    valid=[q for q in roots if q>0 and q<=1+2e-12]
    if not valid:raise ValueError('No physical circle intersection')
    return min(valid)

def build(family,n,dx,dt,lid=.04,inner_speed=.02,stair=False):
    if family=='cylinder':
        nx=int(round(2.2/dx))+1;ny=int(round(.41/dx));x=np.arange(nx)*dx;y=(np.arange(ny)+.5)*dx
        center=np.array([.2,.2]);radii=[.05];periodic=False
    elif family in ['annulus','cavity','couette','periodic']:
        nx=n if family!='couette' else 4;ny=n
        length=2*np.pi if family=='periodic' else 1.
        x=(np.arange(nx)+.5)*dx;y=(np.arange(ny)+.5)*dx
        center=np.array([length/2,length/2]);radii=[.2,.4];periodic=family=='periodic'
    else:raise ValueError('Unknown fixed geometry')
    xx,yy=np.meshgrid(x,y);r=np.sqrt((xx-center[0])**2+(yy-center[1])**2)
    mask=(r>radii[0])&(r<radii[1]) if family=='annulus' else ((r>radii[0]) if family=='cylinder' else np.ones_like(xx,dtype=bool))
    iy,ix=np.nonzero(mask);count=len(ix);table=np.full(mask.shape,-1,dtype=np.int32);table[iy,ix]=np.arange(count,dtype=np.int32)
    source=np.full((9,count),-1,dtype=np.int32);back=source.copy();kind=np.zeros_like(source)
    fraction=np.full((9,count),.5);wall_dot=np.zeros((9,count));lever=np.zeros((9,count))
    for qi,ci in enumerate(C):
        for j,(row,col) in enumerate(zip(iy,ix)):
            sy=int(row-ci[1]);sx=int(col-ci[0]);out=-ci.astype(float)
            if periodic or family=='couette':sx%=nx
            if periodic:sy%=ny
            # Open wet-node boundaries own simultaneous x/y missing links.
            if family=='cylinder' and (sx<0 or sx>=nx):kind[qi,j]=4 if sx<0 else 5;continue
            if 0<=sx<nx and 0<=sy<ny and table[sy,sx]>=0:
                source[qi,j]=table[sy,sx];continue
            point=np.array([xx[row,col],yy[row,col]])
            uw=np.zeros(2);k=1;distance=.5
            if family in ['annulus','cylinder'] and 0<=sx<nx and 0<=sy<ny:
                radius=radii[0] if family=='cylinder' or r[sy,sx]<radii[0] else radii[1]
                k=2 if radius==radii[0] else 3
                distance=.5 if stair else circle_fraction(point,out*dx,center,radius)
                wall_point=point+distance*out*dx
                if family=='annulus' and k==2:
                    radial=(wall_point-center)/radius
                    uw=inner_speed*np.array([-radial[1],radial[0]])*dt/dx
            else:
                # Side-wall ownership at a simultaneous top-side corner.
                if family in ['cavity','couette'] and sy>=ny and (0<=sx<nx or family=='couette'):
                    uw=np.array([lid,0.])
            kind[qi,j]=k;fraction[qi,j]=distance;wall_dot[qi,j]=float(np.sum(out*uw))
            lever[qi,j]=((point[0]-center[0])*out[1]-(point[1]-center[1])*out[0])/dx
            by=int(row+ci[1]);bx=int(col+ci[0])
            if family=='couette':bx%=nx
            if 0<=bx<nx and 0<=by<ny:back[qi,j]=table[by,bx]
            if distance<.5 and back[qi,j]<0:raise ValueError('Short interpolated link lacks its interior neighbor')
    inlet=table[:,0].copy() if family=='cylinder' else np.empty(0,dtype=np.int32)
    outlet=table[:,-1].copy() if family=='cylinder' else np.empty(0,dtype=np.int32)
    speed=(4*.3*y*(.41-y)/.41**2*dt/dx) if family=='cylinder' else np.empty(0)
    return dict(n=count,nx=nx,ny=ny,dx=dx,dt=dt,x=xx[mask],y=yy[mask],mask=mask,
                ix=ix,iy=iy,source=source,back=back,kind=kind,fraction=fraction,
                wall_dot=wall_dot,lever=lever,inlet=inlet,outlet=outlet,
                inlet_speed=np.ascontiguousarray(speed),center=center)

def full_field(values,g):
    result=np.zeros((g['ny'],g['nx']),dtype=np.asarray(values).dtype);result[g['mask']]=values
    return result
