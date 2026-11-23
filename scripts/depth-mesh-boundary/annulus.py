"""Curved polar-Q1 vector viscous BVP in Cartesian physical components.

Solve -div(2 mu epsilon(u))=f, with zero Dirichlet on both circles,
periodic theta. This is a linear vector viscous BVP, not Navier-Stokes.
"""
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import spsolve
from references import fields


def shape(a,b):
    return np.array([(1-a)*(1-b),a*(1-b),a*b,(1-a)*b]),np.array([-(1-b),1-b,b,-b]),np.array([-(1-a),-a,a,1-a])


def mapped(n,nt):
    ir,j=np.meshgrid(np.arange(n),np.arange(nt),indexing='ij');ir=ir.ravel();j=j.ravel()
    cells=np.column_stack((ir*nt+j,(ir+1)*nt+j,(ir+1)*nt+(j+1)%nt,ir*nt+(j+1)%nt))
    return cells,1+ir/n,2*np.pi*j/nt


def gradients(Nr,Nt,r,theta,dr,dtheta):
    radial=Nr[None,:]/dr;angular=Nt[None,:]/dtheta/r[:,None]
    return np.stack((np.cos(theta)[:,None]*radial-np.sin(theta)[:,None]*angular,
                     np.sin(theta)[:,None]*radial+np.cos(theta)[:,None]*angular),axis=-1)


def solve(n,diagnostic_path=None):
    nt=2*n;dr=1/n;dtheta=2*np.pi/nt;cells,r0,t0=mapped(n,nt);E=len(cells);dofs=np.stack((2*cells,2*cells+1),axis=-1).reshape(E,8)
    z,w=leggauss(4);z=(z+1)/2;w=w/2;Kloc=np.zeros((E,8,8));Floc=np.zeros((E,8));volume_force=np.zeros(2)
    for a,wa in zip(z,w):
        for b,wb in zip(z,w):
            N,Nr,Nt=shape(a,b);r=r0+a*dr;theta=t0+b*dtheta;x=r*np.cos(theta);y=r*np.sin(theta);weight=wa*wb*r*dr*dtheta
            G=gradients(Nr,Nt,r,theta,dr,dtheta);mu=1+.2*r*r;B=np.zeros((E,3,8))
            B[:,0,0::2]=G[:,:,0];B[:,1,1::2]=G[:,:,1];B[:,2,0::2]=G[:,:,1];B[:,2,1::2]=G[:,:,0]
            C=mu[:,None]*np.array([2.,2.,1.])[None,:]
            Kloc+=np.einsum('eki,ek,ekj,e->eij',B,C,B,weight)
            force=fields.viscous(x,y)[2];Floc+=np.einsum('a,ec,e->eac',N,force,weight).reshape(E,8);volume_force+=np.sum(force*weight[:,None],axis=0)
    size=2*(n+1)*nt;K=coo_matrix((Kloc.ravel(),(np.repeat(dofs,8,axis=1).ravel(),np.tile(dofs,(1,8)).ravel())),shape=(size,size)).tocsr();F=np.zeros(size);np.add.at(F,dofs.ravel(),Floc.ravel());u=np.zeros(size);boundary=np.zeros(size,dtype=bool);boundary[:2*nt]=True;boundary[-2*nt:]=True;free=~boundary
    A=K[free][:,free];u[free]=spsolve(A,F[free])
    if diagnostic_path is not None:np.savez_compressed(diagnostic_path,u=u,F=F,free=free,n=n,cells=cells)
    if not np.isfinite(u).all() or not np.isfinite(F).all():raise ArithmeticError('Nonfinite annular solution/load; candidate retained')
    U=u.reshape(n+1,nt,2);values=U.reshape(-1,2)[cells];errors=np.zeros(2);reference_norm=np.zeros(2);dissipation=0.;area=0.
    for a,wa in zip(z,w):
        for b,wb in zip(z,w):
            N,Nr,Nt=shape(a,b);r=r0+a*dr;theta=t0+b*dtheta;G=gradients(Nr,Nt,r,theta,dr,dtheta);weight=wa*wb*r*dr*dtheta
            computed=np.einsum('a,eac->ec',N,values);gradient=np.einsum('eac,eak->eck',values,G)
            exact,eg,force=fields.viscous(r*np.cos(theta),r*np.sin(theta));strain=gradient+gradient.swapaxes(1,2);estrain=eg+eg.swapaxes(1,2)
            errors[0]+=np.sum(weight*np.sum((computed-exact)**2,axis=1));errors[1]+=np.sum(weight*np.sum((strain-estrain)**2,axis=(1,2)))
            reference_norm[0]+=np.sum(weight*np.sum(exact**2,axis=1));reference_norm[1]+=np.sum(weight*np.sum(estrain**2,axis=(1,2)));dissipation+=np.sum(weight*.5*(1+.2*r*r)*np.sum(strain**2,axis=(1,2)));area+=weight.sum()
    traction_error=0.;traction_norm=0.;traction_flux=np.zeros(2);exact_flux=np.zeros(2);saved_traction=[]
    for side,a,sign in [(0,0.,-1.),(n-1,1.,1.)]:
        ids=np.arange(side*nt,(side+1)*nt);v=values[ids];r=np.full(nt,1. if side==0 else 2.);theta0=t0[ids]
        for b,wb in zip(z,w):
            N,Nr,Nt=shape(a,b);theta=theta0+b*dtheta;G=gradients(Nr,Nt,r,theta,dr,dtheta);gradient=np.einsum('eac,eak->eck',v,G);mu=1+.2*r*r;tau=mu[:,None,None]*(gradient+gradient.swapaxes(1,2));normal=sign*np.column_stack((np.cos(theta),np.sin(theta)))
            tr=np.einsum('eij,ej->ei',tau,normal);et=np.einsum('eij,ej->ei',fields.stress(r*np.cos(theta),r*np.sin(theta)),normal);weight=wb*r*dtheta
            traction_error+=np.sum(weight*np.sum((tr-et)**2,axis=1));traction_norm+=np.sum(weight*np.sum(et**2,axis=1));traction_flux+=np.sum(weight[:,None]*tr,axis=0);exact_flux+=np.sum(weight[:,None]*et,axis=0);saved_traction.append(np.column_stack((r,theta,tr,et)))
    # Explicit real product/sum avoids backend dense-dot floating-status warnings.
    # This is exactly the same scalar work contraction, without suppression.
    reaction=(K@u-F).reshape(-1,2).sum(axis=0);force_scale=max(1.,np.linalg.norm(volume_force));work=float(np.sum(u*F))
    # Exact circle integration: radial A(s)e_x contributes -756*pi/5
    # to total outward x-traction; angular xy/D terms integrate to zero.
    analytic_force=np.array([756*np.pi/5,0.])
    row=dict(n=n,theta_cells=nt,dofs=int(free.sum()),relative_l2=float(np.sqrt(errors[0]/reference_norm[0])),relative_strain_l2=float(np.sqrt(errors[1]/reference_norm[1])),relative_traction_l2=float(np.sqrt(traction_error/traction_norm)),residual=float(np.max(abs(A@u[free]-F[free]))),boundary_error=float(np.max(abs(u[boundary]))),area_error=float(abs(area-3*np.pi)),reaction_balance=float(np.linalg.norm(reaction+volume_force)/force_scale),traction_flux_balance=float(np.linalg.norm(traction_flux+volume_force)/force_scale),exact_flux_balance=float(np.linalg.norm(exact_flux+volume_force)/force_scale),analytic_force_error=float(np.linalg.norm(volume_force-analytic_force)/np.linalg.norm(analytic_force)),work_identity=float(abs(work-dissipation)/max(1,abs(work))),symmetry=float(abs(A-A.T).max()) if (A-A.T).nnz else 0.)
    rr,tt=np.meshgrid(np.linspace(1,2,n+1),np.arange(nt)*dtheta,indexing='ij');xx=rr*np.cos(tt);yy=rr*np.sin(tt)
    return row,dict(x=xx,y=yy,u=U,reference=fields.viscous(xx,yy)[0],cells=cells,traction_samples=np.concatenate(saved_traction),body_force_integral=volume_force,analytic_body_force_integral=analytic_force,traction_flux=traction_flux,exact_traction_flux=exact_flux,boundary_reaction=reaction)
