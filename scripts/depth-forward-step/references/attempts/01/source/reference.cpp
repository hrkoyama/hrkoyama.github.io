// Independent educational finite-volume reference, MIT, (c) 2026 Hiroshi Koyama.
// This file imports no Python/Numart/primary-solver operators.
// Primitive MUSCL generalized minmod(theta=1.5), Davis HLL, Heun/SSPRK2.
// No Woodward--Colella entropy/enthalpy reset at the step corner.
#include <algorithm>
#include <array>
#include <chrono>
#include <cmath>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <limits>
#include <stdexcept>
#include <string>
#include <vector>

using V = std::array<double,4>;
using Field = std::vector<V>;
constexpr double gamma_gas=1.4, cfl=.3, theta=1.5;
constexpr V inlet{{1.4,3.,0.,1.}};
V zero() { return V{{0.,0.,0.,0.}}; }
void require(bool v,const std::string &s) { if(!v) throw std::runtime_error(s); }
bool admissible(const V&q) {
  if(!(q[0]>0.)) return false;
  for(double v:q) if(!std::isfinite(v)) return false;
  return (q[3]-.5*(q[1]*q[1]+q[2]*q[2])/q[0])>0.;
}
V conserved(const V&w) {
  return V{{w[0],w[0]*w[1],w[0]*w[2],w[3]/(gamma_gas-1.)+.5*w[0]*(w[1]*w[1]+w[2]*w[2])}};
}
V primitive(const V&q) {
  require(admissible(q),"inadmissible conserved state");
  return V{{q[0],q[1]/q[0],q[2]/q[0],(gamma_gas-1.)*(q[3]-.5*(q[1]*q[1]+q[2]*q[2])/q[0])}};
}
V reflected(V w,int axis) { w[axis+1]=-w[axis+1];return w; }
V flux(const V&w,const V&q,int axis) {
  const double u=w[axis+1]; V f;
  for(int k=0;k<4;++k)f[k]=q[k]*u;
  f[axis+1]+=w[3];f[3]+=w[3]*u;return f;
}
V hll(const V&l,const V&r,int axis) {
  require(l[0]>0.&&l[3]>0.&&r[0]>0.&&r[3]>0.,"nonpositive face primitive");
  const V ql=conserved(l),qr=conserved(r),fl=flux(l,ql,axis),fr=flux(r,qr,axis);
  const double cl=std::sqrt(gamma_gas*l[3]/l[0]),cr=std::sqrt(gamma_gas*r[3]/r[0]);
  const double sl=std::min(l[axis+1]-cl,r[axis+1]-cr),sr=std::max(l[axis+1]+cl,r[axis+1]+cr);
  if(sl>=0.)return fl;if(sr<=0.)return fr;
  V f;for(int k=0;k<4;++k)f[k]=(sr*fl[k]-sl*fr[k]+sl*sr*(qr[k]-ql[k]))/(sr-sl);return f;
}
double minmod(double a,double b,double c) {
  if(a>0.&&b>0.&&c>0.)return std::min(a,std::min(b,c));
  if(a<0.&&b<0.&&c<0.)return std::max(a,std::max(b,c));return 0.;
}
struct Step {
  int nx,ny,ix,jy;double h;
  std::vector<unsigned char>fluid;
  Field w,sx,sy,fx,fy;
  long long slope_rescalings=0;
  explicit Step(int n):nx(3*n),ny(n),ix(3*n/5),jy(n/5),h(1./n),fluid(nx*ny),
      w(nx*ny),sx(nx*ny),sy(nx*ny),fx((nx+1)*ny),fy(nx*(ny+1)) {
    require(n>=10&&n%5==0,"Ny must be divisible by 5 and >=10");
    for(int i=0;i<nx;++i)for(int j=0;j<ny;++j)fluid[id(i,j)]=!(i>=ix&&j<jy);
  }
  int id(int i,int j) const{return i*ny+j;}
  bool active(int i,int j) const{return i>=0&&j>=0&&i<nx&&j<ny&&fluid[id(i,j)];}
  V face(int i,int j,int axis,double sign) const{
    const int z=id(i,j);V v=w[z];const V&s=axis==0?sx[z]:sy[z];
    for(int k=0;k<4;++k)v[k]+=.5*sign*s[k];return v;
  }
  void reconstruct(const Field&q) {
    std::fill(sx.begin(),sx.end(),zero());std::fill(sy.begin(),sy.end(),zero());
    for(int i=0;i<nx;++i)for(int j=0;j<ny;++j)if(active(i,j))w[id(i,j)]=primitive(q[id(i,j)]);
    for(int i=0;i<nx;++i)for(int j=0;j<ny;++j)if(active(i,j)) {
      int z=id(i,j);
      for(int axis=0;axis<2;++axis) {
        const int di=axis==0,dj=axis==1;
        if(!active(i-di,j-dj)||!active(i+di,j+dj))continue;
        V&s=axis==0?sx[z]:sy[z];
        for(int k=0;k<4;++k) {
          const double dl=w[z][k]-w[id(i-di,j-dj)][k],dr=w[id(i+di,j+dj)][k]-w[z][k];
          s[k]=minmod(theta*dl,.5*(dl+dr),theta*dr);
        }
        // Convex slope rescaling preserves the cell average. It is not a state floor.
        double a=1.;for(int k:{0,3})if(std::abs(s[k])>0.)a=std::min(a,(2.*(1.-1e-12)*w[z][k])/std::abs(s[k]));
        if(a<1.){for(double&v:s)v*=a;++slope_rescalings;}
      }
    }
  }
  // net is the incoming integrated rate, including ALL step and outer wall tractions.
  void rhs(const Field&q,Field&dq,V&net) {
    reconstruct(q);net=zero();
    for(int i=0;i<=nx;++i)for(int j=0;j<ny;++j) {
      bool l=active(i-1,j),r=active(i,j);V f=zero();
      if(l&&r) f=hll(face(i-1,j,0,1.),face(i,j,0,-1.),0);
      else if(i==0&&r)f=hll(inlet,face(i,j,0,-1.),0);
      else if(i==nx&&l){V v=face(i-1,j,0,1.);f=hll(v,v,0);}
      else if(l){V v=face(i-1,j,0,1.);f=hll(v,reflected(v,0),0);}
      else if(r){V v=face(i,j,0,-1.);f=hll(reflected(v,0),v,0);}
      fx[i*ny+j]=f;
      if(l!=r)for(int k=0;k<4;++k)net[k]+=(r?1.:-1.)*h*f[k];
    }
    for(int i=0;i<nx;++i)for(int j=0;j<=ny;++j) {
      bool b=active(i,j-1),t=active(i,j);V f=zero();
      if(b&&t)f=hll(face(i,j-1,1,1.),face(i,j,1,-1.),1);
      else if(b){V v=face(i,j-1,1,1.);f=hll(v,reflected(v,1),1);}
      else if(t){V v=face(i,j,1,-1.);f=hll(reflected(v,1),v,1);}
      fy[i*(ny+1)+j]=f;
      if(b!=t)for(int k=0;k<4;++k)net[k]+=(t?1.:-1.)*h*f[k];
    }
    std::fill(dq.begin(),dq.end(),zero());
    for(int i=0;i<nx;++i)for(int j=0;j<ny;++j)if(active(i,j))
      for(int k=0;k<4;++k)dq[id(i,j)][k]=-(fx[(i+1)*ny+j][k]-fx[i*ny+j][k]+fy[i*(ny+1)+j+1][k]-fy[i*(ny+1)+j][k])/h;
  }
  V integral(const Field&q) const {
    std::array<long double,4>a{{0.,0.,0.,0.}};
    for(int z=0;z<nx*ny;++z)if(fluid[z])for(int k=0;k<4;++k)a[k]+=static_cast<long double>(q[z][k])*h*h;
    V v;for(int k=0;k<4;++k)v[k]=static_cast<double>(a[k]);return v;
  }
  void validate(const Field&q,double&rmin,double&pmin) const {
    for(int z=0;z<nx*ny;++z)if(fluid[z]){const V v=primitive(q[z]);rmin=std::min(rmin,v[0]);pmin=std::min(pmin,v[3]);}
  }
  double timestep(const Field&q) const {
    double a=0.,b=0.;
    for(int z=0;z<nx*ny;++z)if(fluid[z]){const V v=primitive(q[z]);const double c=std::sqrt(gamma_gas*v[3]/v[0]);a=std::max(a,std::abs(v[1])+c);b=std::max(b,std::abs(v[2])+c);}
    return cfl*h/(a+b);
  }
};
void vector_json(std::ostream&f,const V&a){f<<'[';for(int k=0;k<4;++k){if(k)f<<',';f<<a[k];}f<<']';}
void save_state(const std::string&name,const Field&q){std::ofstream f(name,std::ios::binary);require(bool(f),"cannot open raw state output");f.write(reinterpret_cast<const char*>(q.data()),static_cast<std::streamsize>(q.size()*sizeof(V)));require(bool(f),"cannot write raw state output");}
int self_test(){
  V q=conserved(inlet),roundtrip=primitive(q);for(int k=0;k<4;++k)require(std::abs(roundtrip[k]-inlet[k])<1e-14,"primitive/conserved round trip");
  for(int axis=0;axis<2;++axis){V a=hll(inlet,inlet,axis),b=flux(inlet,q,axis);for(int k=0;k<4;++k)require(std::abs(a[k]-b[k])<1e-13,"consistent HLL flux");V f=hll(inlet,reflected(inlet,axis),axis);require(std::abs(f[0])<1e-13&&std::abs(f[3])<1e-13,"impermeable wall");}
  require(minmod(1.,2.,3.)==1.&&minmod(-1.,-2.,-3.)==-1.&&minmod(-1.,2.,3.)==0.,"minmod branches");
  Step g(20);Field a(g.nx*g.ny,q),d(a.size());V rate;g.rhs(a,d,rate);
  require(std::count(g.fluid.begin(),g.fluid.end(),1)==1008,"aligned fluid area");
  V integ=g.integral(d);for(int k=0;k<4;++k)require(std::abs(integ[k]-rate[k])<1e-11,"masked divergence theorem including step wall");
  require(rate[1]<0.,"step horizontal wall force opposes inflow");
  std::cout<<"{\"self_tests_passed\":8}\n";return 0;
}
int main(int argc,char**argv) {
  std::string prefix;
  try {
    if(argc==2&&std::string(argv[1])=="--self-test")return self_test();
    require(argc==3,"usage: reference Ny output-prefix (or --self-test)");
    int n=std::stoi(argv[1]);prefix=argv[2];Step g(n);
    Field q(g.nx*g.ny,conserved(inlet)),first(q.size()),out(q.size()),d0(q.size()),d1(q.size());
    const V initial=g.integral(q);V boundary=zero();double time=0.,rmin=1.4,pmin=1.;int steps=0;
    const auto start=std::chrono::steady_clock::now();
    while(time<4.){
      double dt=std::min(4.-time,g.timestep(q));require(dt>0.&&std::isfinite(dt),"invalid time step");
      V b0,b1;g.rhs(q,d0,b0);
      for(std::size_t z=0;z<q.size();++z)for(int k=0;k<4;++k)first[z][k]=q[z][k]+dt*d0[z][k];
      try{g.validate(first,rmin,pmin);}catch(...){save_state(prefix+"-failed-stage1.f64",first);throw;}
      g.rhs(first,d1,b1);
      for(std::size_t z=0;z<q.size();++z)for(int k=0;k<4;++k)out[z][k]=.5*(q[z][k]+first[z][k]+dt*d1[z][k]);
      try{g.validate(out,rmin,pmin);}catch(...){save_state(prefix+"-failed-stage2.f64",out);throw;}
      for(int k=0;k<4;++k)boundary[k]+=.5*dt*(b0[k]+b1[k]);
      q.swap(out);time+=dt;++steps;require(steps<100000,"step budget exhausted");
    }
    const auto seconds=std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();
    V total=g.integral(q),residual,relative;
    for(int k=0;k<4;++k){residual[k]=total[k]-initial[k]-boundary[k];relative[k]=std::abs(residual[k])/std::max(1.,std::max(std::abs(total[k]),std::max(std::abs(initial[k]),std::abs(boundary[k]))));}
    save_state(prefix+".f64",q);
    std::ofstream f(prefix+".json");require(bool(f),"cannot open metadata output");f<<std::setprecision(17);
    f<<"{\"schema_version\":1,\"passed\":true,\"ny\":"<<n<<",\"nx\":"<<3*n<<",\"time\":"<<time<<",\"steps\":"<<steps<<",\"wall_seconds\":"<<seconds<<",\"gamma\":1.4,\"cfl\":0.3,\"muscl_theta\":1.5,\"minimum_density_all_stages\":"<<rmin<<",\"minimum_pressure_all_stages\":"<<pmin<<",\"slope_rescalings\":"<<g.slope_rescalings<<",\"state_floor_count\":0,\"rejected_steps\":0,\"corner_entropy_reset\":false,\"initial_integral\":";vector_json(f,initial);f<<",\"final_integral\":";vector_json(f,total);f<<",\"boundary_net_integral\":";vector_json(f,boundary);f<<",\"conservation_residual\":";vector_json(f,residual);f<<",\"conservation_relative\":";vector_json(f,relative);f<<"}\n";
    std::cout<<std::setprecision(10)<<"{\"ny\":"<<n<<",\"steps\":"<<steps<<",\"wall_seconds\":"<<seconds<<",\"min_rho\":"<<rmin<<",\"min_p\":"<<pmin<<"}\n";
    return 0;
  }catch(const std::exception&e){std::cerr<<"reference failure: "<<e.what()<<'\n';if(!prefix.empty()){std::ofstream f(prefix+"-failure.json");f<<"{\"passed\":false,\"failure\":\""<<e.what()<<"\"}\n";}return 1;}
}
