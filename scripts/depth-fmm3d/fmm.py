"""Uncompressed3D tensor-Chebyshev FMM for isolated gravitational -1/r.

Actual upward M2M, dual-tree M2L, downward L2L and differentiated L2P.
Only ownership diagnostics, never a global dense production kernel, are N-by-N.
"""
from dataclasses import dataclass,field
import numpy as np

def chebyshev(p):
    t=(2*np.arange(p)+1)*np.pi/(2*p)
    return np.cos(t),(-1.)**np.arange(p)*np.sin(t)

def basis(t,p):
    nodes,w=chebyshev(p);t=np.asarray(t,float).reshape(-1);B=np.zeros((len(t),p));D=np.zeros_like(B)
    for n,value in enumerate(t):
        gap=value-nodes;at=np.flatnonzero(abs(gap)<=8*np.finfo(float).eps)
        if len(at):
            k=int(at[0]);B[n,k]=1.;other=np.arange(p)!=k;D[n,other]=w[other]/(w[k]*(nodes[k]-nodes[other]));D[n,k]=-D[n,other].sum()
        else:
            v=w/gap;S=v.sum();B[n]=v/S;D[n]=B[n]*(np.sum(w/gap**2)/S-1/gap)
    return B,D

@dataclass
class Node:
    center:np.ndarray
    half:float
    ids:np.ndarray
    depth:int
    children:list=field(default_factory=list)
    W:object=None
    local:object=None
    chain:object=None

def build(x,center,half,level,cap,forced,capacity):
    node=Node(np.asarray(center),half,np.arange(len(x)),level)
    # ids are replaced by the caller's global ids below.
    def branch(ids,c,h,d):
        n=Node(c,h,ids,d)
        if d<cap and (forced or len(ids)>capacity):
            code=np.sum((x[ids]>=c)*np.array([1,2,4]),axis=1)
            for k in range(8):
                subset=ids[code==k]
                if len(subset):
                    direction=np.array([1 if k&(1<<a) else -1 for a in range(3)])
                    n.children.append(branch(subset,c+direction*h/2,h/2,d+1))
        return n
    return branch(node.ids,node.center,node.half,level)

def walk(node):
    yield node
    for child in node.children:yield from walk(child)

def grid(node,p):
    z=chebyshev(p)[0];a=np.stack(np.meshgrid(z,z,z,indexing='ij'),axis=-1).reshape(-1,3)
    return node.center+node.half*a

def maps(parent,child,p):
    z=chebyshev(p)[0]
    return [basis((child.center[a]+child.half*z-parent.center[a])/parent.half,p)[0] for a in range(3)]

def up(node,x,m,p,counts):
    if not node.children:
        B=[basis((x[node.ids,a]-node.center[a])/node.half,p)[0] for a in range(3)]
        node.W=np.einsum('n,na,nb,nc->abc',m[node.ids],*B,optimize=False);counts['p2m']+=1
    else:
        node.W=np.zeros((p,p,p))
        for child in node.children:
            up(child,x,m,p,counts);A,B,C=maps(node,child,p)
            v=np.einsum('abc,au->ubc',child.W,A,optimize=False);v=np.einsum('ubc,bv->uvc',v,B,optimize=False)
            node.W+=np.einsum('uvc,cw->uvw',v,C,optimize=False);counts['m2m']+=1

def transfer(parent,child,value,p):
    A,B,C=maps(parent,child,p);v=np.einsum('uvw,au->avw',value,A,optimize=False);v=np.einsum('avw,bv->abw',v,B,optimize=False)
    return np.einsum('abw,cw->abc',v,C,optimize=False)

def local_values(node,values,points,p):
    B=[];D=[]
    for a in range(3):
        b,d=basis((points[:,a]-node.center[a])/node.half,p);B.append(b);D.append(d/node.half)
    potential=np.einsum('ia,ib,ic,abc->i',*B,values,optimize=False);gradient=np.zeros_like(points)
    for a in range(3):
        b=B.copy();b[a]=D[a];gradient[:,a]=np.einsum('ia,ib,ic,abc->i',*b,values,optimize=False)
    return potential,-gradient

def solve(x,m,p=5,depth=2,forced=True,capacity=8,targets=None,self_indices=None,half=1.,admissibility=.5):
    x=np.asarray(x,float);m=np.asarray(m,float)
    if x.ndim!=2 or x.shape[1]!=3 or m.shape!=(len(x),) or not np.isfinite(x).all() or not np.isfinite(m).all() or np.min(m)<=0:raise ValueError('Finite3D positions and positive masses required')
    if p<2 or depth<1 or capacity<1 or np.max(abs(x))>half:raise ValueError('Invalid fixed FMM controls')
    if targets is None:targets=x.copy();self_indices=np.arange(len(x))
    else:targets=np.asarray(targets,float)
    if self_indices is None:self_indices=np.full(len(targets),-1,int)
    if np.max(abs(targets))>half:raise ValueError('Targets outside fixed root')
    counts=dict(p2m=0,m2m=0,m2l=0,l2l=0,nonzero_l2l=0,chain_pairs=0,p2p_pairs=0,far_pairs=0,maximum_kernel_entries=0)
    source=build(x,np.zeros(3),half,0,depth,forced,capacity);target=build(targets,np.zeros(3),half,0,depth,forced,capacity);up(source,x,m,p,counts)
    for node in walk(target):node.local=np.zeros((p,p,p));node.chain=np.zeros((p,p,p))
    phi=np.zeros(len(targets));acc=np.zeros_like(targets);owner=np.zeros((len(targets),len(x)),np.int16);pairs=[]
    def interact(s,t):
        distance=float(np.sqrt(np.sum((s.center-t.center)**2)));ratio=np.sqrt(3)*(s.half+t.half)/distance if distance else np.inf
        if ratio<=admissibility:
            a=grid(t,p);b=grid(s,p);d=a[:,None,:]-b[None,:,:];r2=np.sum(d*d,axis=2)
            if np.min(r2)<=0:raise ArithmeticError('Singular accepted FMM box pair')
            kernel=-1/np.sqrt(r2);contribution=np.einsum('ij,j->i',kernel,s.W.ravel(),optimize=False).reshape(p,p,p);t.local+=contribution
            if s.children and t.children:t.chain+=contribution;counts['chain_pairs']+=1
            owner[np.ix_(t.ids,s.ids)]+=1;counts['m2l']+=1;counts['far_pairs']+=len(s.ids)*len(t.ids);counts['maximum_kernel_entries']=max(counts['maximum_kernel_entries'],kernel.size);pairs.append([s.depth,t.depth,len(s.ids),len(t.ids),ratio]);return
        if not s.children and not t.children:
            d=targets[t.ids,None,:]-x[None,s.ids,:];r2=np.sum(d*d,axis=2);selfmask=self_indices[t.ids,None]==s.ids[None,:]
            if np.any((r2==0)&~selfmask):raise ValueError('Coincident distinct unsoftened sources')
            r2[selfmask]=np.inf;inverse=1/np.sqrt(r2);phi[t.ids]-=np.sum(inverse*m[s.ids][None,:],axis=1);acc[t.ids]-=np.einsum('ij,ijk->ik',inverse**3*m[s.ids][None,:],d,optimize=False)
            for i,ii in enumerate(t.ids):owner[ii,s.ids[~selfmask[i]]]+=1
            counts['p2p_pairs']+=int((~selfmask).sum());return
        if s.children and (not t.children or s.half>=t.half):
            for c in s.children:interact(c,t)
        else:
            for c in t.children:interact(s,c)
    interact(source,target);chain_phi=np.zeros(len(targets))
    def down(node):
        if node.children:
            for child in node.children:
                value=transfer(node,child,node.local,p);child.local+=value;child.chain+=transfer(node,child,node.chain,p);counts['l2l']+=1;counts['nonzero_l2l']+=int(np.any(value!=0));down(child)
        else:
            v,a=local_values(node,node.local,targets[node.ids],p);phi[node.ids]+=v;acc[node.ids]+=a;chain_phi[node.ids]=local_values(node,node.chain,targets[node.ids],p)[0]
    down(target)
    if not np.isfinite(phi).all() or not np.isfinite(acc).all():raise ArithmeticError('Nonfinite FMM result')
    nodes=list(walk(source));leaves=[n for n in nodes if not n.children]
    boxes=np.array([np.r_[n.center,n.half,n.depth,len(n.ids),int(bool(n.children))] for n in nodes]);expected=np.ones_like(owner)
    for i,j in enumerate(self_indices):
        if j>=0:expected[i,j]=0
    data=dict(potential=phi,acceleration=acc,chain_potential=chain_phi,ownership=owner,expected_ownership=expected,boxes=boxes,accepted_box_pairs=np.array(pairs).reshape(-1,5),leaf_depths=np.array([n.depth for n in leaves]),leaf_sizes=np.array([len(n.ids) for n in leaves]))
    counts['overfull_leaves']=sum(len(n.ids)>capacity for n in leaves);counts['maximum_leaf_depth']=max(n.depth for n in leaves);counts['minimum_leaf_depth']=min(n.depth for n in leaves)
    return data,counts
