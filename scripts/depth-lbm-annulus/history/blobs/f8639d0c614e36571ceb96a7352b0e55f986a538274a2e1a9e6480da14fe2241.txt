// Independently written D2Q9 BGK, link interpolation and Zou-He open boundaries.
// Standard C++17; no fast-math, no population/density clipping or repair.
#include <algorithm>
#include <cmath>
#include <cstddef>
#include <vector>

namespace {
constexpr int cx[9]={0,1,0,-1,0,1,-1,-1,1};
constexpr int cy[9]={0,0,1,0,-1,1,1,-1,-1};
constexpr int opposite[9]={0,3,4,1,2,7,8,5,6};
constexpr double weight[9]={4./9,1./9,1./9,1./9,1./9,1./36,1./36,1./36,1./36};
}

// q-major contiguous arrays. kind0=fluid,1=flat wall,2=inner/body,
// 3=outer annular wall,4=inlet,5=outlet. Geometry is fixed during advance.
// history columns: initial M,Px,Py; boundary dM,dPx,dPy; body Fx,Fy,T;
// maximum Ma,min/max rho,min f; wall dM,open dM,total wall torque.
// status={completed_steps, failing_step, failing_node}. Return0 means complete.
extern "C" int lbm_advance(
 int n,int steps,double tau,const int* source,const int* back,const int* kind,
 const double* fraction,const double* wall_dot,const double* lever,
 const int* inlet,int nin,const int* outlet,int nout,const double* inlet_speed,
 double* f,double* history,int* status) {
 status[0]=0;status[1]=-1;status[2]=-1;
 if(n<=0||steps<0||!std::isfinite(tau)||tau<=.5)return 1;
 const std::size_t count=static_cast<std::size_t>(9)*n;
 std::vector<double> post(count),next(count),old_uy(n);
 for(int step=0;step<steps;++step){
  double* h=history+static_cast<std::size_t>(step)*16;
  std::fill(h,h+16,0.);h[10]=1.e300;h[11]=-1.e300;h[12]=1.e300;
  status[1]=step;
  for(int i=0;i<n;++i){
   double rho=0.,px=0.,py=0.;
   for(int q=0;q<9;++q){const double v=f[static_cast<std::size_t>(q)*n+i];
    if(!std::isfinite(v)){status[2]=i;return 2;}
    rho+=v;px+=cx[q]*v;py+=cy[q]*v;h[12]=std::min(h[12],v);
   }
   if(!std::isfinite(rho)||rho<=0.){status[2]=i;return 2;}
   const double ux=px/rho,uy=py/rho,speed2=ux*ux+uy*uy;
   old_uy[i]=uy;h[0]+=rho;h[1]+=px;h[2]+=py;
   h[9]=std::max(h[9],std::sqrt(3.*speed2));
   h[10]=std::min(h[10],rho);h[11]=std::max(h[11],rho);
   for(int q=0;q<9;++q){
    const auto index=static_cast<std::size_t>(q)*n+i;
    const double cu=cx[q]*ux+cy[q]*uy;
    const double eq=weight[q]*rho*(1.+3.*cu+4.5*cu*cu-1.5*speed2);
    post[index]=f[index]-(f[index]-eq)/tau;
    if(!std::isfinite(post[index])){status[2]=i;return 3;}
   }
  }
  for(int q=0;q<9;++q)for(int i=0;i<n;++i){
   const auto index=static_cast<std::size_t>(q)*n+i;
   const int k=kind[index],o=opposite[q];
   if(k==0){
    const int src=source[index];if(src<0||src>=n){status[2]=i;return 4;}
    next[index]=post[static_cast<std::size_t>(q)*n+src];
   }else if(k>=1&&k<=3){
    const double d=fraction[index];const double outgoing=post[static_cast<std::size_t>(o)*n+i];
    if(!(d>0.&&d<=1.)){status[2]=i;return 4;}
    double incoming;
    if(d<.5){
     const int b=back[index];if(b<0||b>=n){status[2]=i;return 4;}
     incoming=2.*d*outgoing+(1.-2.*d)*post[static_cast<std::size_t>(o)*n+b]
              -6.*weight[o]*wall_dot[index];
    }else{
     incoming=outgoing/(2.*d)+(2.*d-1.)/(2.*d)*post[index]
              -3.*weight[o]/d*wall_dot[index];
    }
    if(!std::isfinite(incoming)){status[2]=i;return 3;}
    next[index]=incoming;
    const double sum=outgoing+incoming;
    const double dm=incoming-outgoing,fx=sum*cx[o],fy=sum*cy[o];
    h[3]+=dm;h[4]-=fx;h[5]-=fy;h[13]+=dm;h[15]-=sum*lever[index];
    if(k==2){h[6]+=fx;h[7]+=fy;h[8]+=sum*lever[index];}
   }else if(k==4||k==5){
    next[index]=0.;
    const double outgoing=post[static_cast<std::size_t>(o)*n+i];
    h[3]-=outgoing;h[4]-=outgoing*cx[o];h[5]-=outgoing*cy[o];h[14]-=outgoing;
   }else{status[2]=i;return 4;}
  }
  // Only the three missing incoming populations are reconstructed at wet nodes.
  for(int a=0;a<nin;++a){
   const int i=inlet[a];const double u=inlet_speed[a];
   const double rho=(next[i]+next[2*n+i]+next[4*n+i]
                    +2.*(next[3*n+i]+next[6*n+i]+next[7*n+i]))/(1.-u);
   if(!std::isfinite(rho)||rho<=0.){std::copy(next.begin(),next.end(),f);status[2]=i;return 5;}
   next[n+i]=next[3*n+i]+(2./3)*rho*u;
   next[5*n+i]=next[7*n+i]+.5*(next[4*n+i]-next[2*n+i])+rho*u/6.;
   next[8*n+i]=next[6*n+i]+.5*(next[2*n+i]-next[4*n+i])+rho*u/6.;
   for(int q:{1,5,8}){const double v=next[q*n+i];h[3]+=v;h[4]+=cx[q]*v;h[5]+=cy[q]*v;h[14]+=v;}
  }
  for(int a=0;a<nout;++a){
   const int i=outlet[a];const double rho=1.;
   // The adjacent interior node index is source of the east-going population.
   const int interior=source[n+i];
   if(interior<0||interior>=n){status[2]=i;return 4;}
   const double uy=old_uy[interior];
   const double ux=-1.+(next[i]+next[2*n+i]+next[4*n+i]
                       +2.*(next[n+i]+next[5*n+i]+next[8*n+i]))/rho;
   next[3*n+i]=next[n+i]-(2./3)*rho*ux;
   next[6*n+i]=next[8*n+i]+.5*(next[4*n+i]-next[2*n+i])-rho*ux/6.+.5*rho*uy;
   next[7*n+i]=next[5*n+i]+.5*(next[2*n+i]-next[4*n+i])-rho*ux/6.-.5*rho*uy;
   for(int q:{3,6,7}){const double v=next[q*n+i];h[3]+=v;h[4]+=cx[q]*v;h[5]+=cy[q]*v;h[14]+=v;}
  }
  std::copy(next.begin(),next.end(),f);status[0]=step+1;
 }
 status[1]=-1;status[2]=-1;return 0;
}
