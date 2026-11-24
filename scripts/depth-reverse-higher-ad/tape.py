"""Small real reverse tape and forward-over-reverse, not a NumPy AD system."""
import numpy as np


def unbroadcast(value, shape):
    value=np.asarray(value)
    while value.ndim>len(shape):value=value.sum(axis=0)
    for axis,length in enumerate(shape):
        if length==1 and value.shape[axis]!=1:value=value.sum(axis=axis,keepdims=True)
    if value.shape!=shape:raise ValueError('Unbroadcast shape mismatch')
    return np.array(value,copy=True)


class Node:
    __array_priority__=10000
    def __init__(self,tape,value,tangent,op='input',parents=(),key=None):
        self.tape=tape;self.value=np.array(value,dtype=float,copy=True)
        self.tangent=np.array(tangent,dtype=float,copy=True)
        if self.value.shape!=self.tangent.shape:raise ValueError('Tangent shape mismatch')
        if not np.all(np.isfinite(self.value)) or not np.all(np.isfinite(self.tangent)):
            raise ArithmeticError('Nonfinite node')
        self.cotangent=np.zeros_like(self.value);self.cotangent_tangent=np.zeros_like(self.value)
        self.op=op;self.parents=tuple(parents);self.key=key;self.index=len(tape.nodes);tape.nodes.append(self)

    def __float__(self):raise TypeError('A live derivative node cannot become float')
    def __array__(self,*args,**kwargs):raise TypeError('A live derivative node cannot become an ndarray')
    def _coerce(self,x):
        if isinstance(x,Node):
            if x.tape is not self.tape:raise ValueError('Different tapes')
            return x
        return self.tape.constant(x)
    def __add__(self,x):
        x=self._coerce(x);return Node(self.tape,self.value+x.value,self.tangent+x.tangent,'add',(self,x))
    __radd__=__add__
    def __neg__(self):return Node(self.tape,-self.value,-self.tangent,'neg',(self,))
    def __sub__(self,x):return self+(-self._coerce(x))
    def __rsub__(self,x):return self._coerce(x)+(-self)
    def __mul__(self,x):
        x=self._coerce(x)
        return Node(self.tape,self.value*x.value,self.tangent*x.value+self.value*x.tangent,'mul',(self,x))
    __rmul__=__mul__
    def __truediv__(self,x):
        x=self._coerce(x)
        if np.any(x.value==0):raise ValueError('Zero divisor')
        return Node(self.tape,self.value/x.value,(self.tangent*x.value-self.value*x.tangent)/(x.value*x.value),'div',(self,x))
    def __rtruediv__(self,x):return self._coerce(x)/self
    def __getitem__(self,key):
        if isinstance(key,list):key=np.array(key,dtype=int)
        if isinstance(key,np.ndarray)and(key.ndim!=1 or key.dtype.kind not in 'iu'):raise TypeError('Only1D integer gather')
        if isinstance(key,np.ndarray):key=np.array(key,copy=True)
        return Node(self.tape,self.value[key],self.tangent[key],'gather',(self,),key)
    def sum(self):return Node(self.tape,self.value.sum(),self.tangent.sum(),'sum',(self,))
    def exp(self):
        if np.max(self.value)>700 or np.min(self.value)<-700:raise ValueError('Exponential domain guard')
        value=np.exp(self.value);return Node(self.tape,value,value*self.tangent,'exp',(self,))
    def pad(self):
        if self.value.ndim!=1:raise ValueError('1D padding only')
        return Node(self.tape,np.r_[0.,self.value,0.],np.r_[0.,self.tangent,0.],'pad',(self,))


class Tape:
    def __init__(self):self.nodes=[];self.pullbacks=0;self.backward_rules=0;self.second_rules=0
    def variable(self,value,tangent=None):
        return Node(self,value,np.zeros_like(value,dtype=float)if tangent is None else tangent)
    def constant(self,value):return Node(self,value,np.zeros_like(value,dtype=float),'constant')
    def reverse(self,outputs,seed,second_order=False,negative_control=None):
        """Return owning cotangents. Fault modes are ONLY declared qualification negatives."""
        sequence=isinstance(outputs,(list,tuple));outs=list(outputs)if sequence else[outputs]
        seeds=np.asarray(seed,dtype=float)
        expected=(len(outs),)if sequence else outs[0].value.shape
        if seeds.shape!=expected:raise ValueError('Cotangent shape mismatch')
        if negative_control!='stale-cotangent':
            for node in self.nodes:
                node.cotangent.fill(0.);node.cotangent_tangent.fill(0.)
        if negative_control=='permuted-output':seeds=seeds[::-1].copy()
        for i,node in enumerate(outs):node.cotangent+=seeds[i]if sequence else seeds
        self.pullbacks+=1
        def add(parent,bar,dbar):
            if negative_control=='broadcast-first'and parent.value.shape==()and np.asarray(bar).shape!=():
                parent.cotangent+=np.asarray(bar).flat[0]
                parent.cotangent_tangent+=np.asarray(dbar).flat[0]
            else:
                parent.cotangent+=unbroadcast(bar,parent.value.shape)
                parent.cotangent_tangent+=unbroadcast(dbar,parent.value.shape)
        for node in reversed(self.nodes):
            if not node.parents:continue
            self.backward_rules+=1
            if second_order:self.second_rules+=1
            c=node.cotangent;d=node.cotangent_tangent
            a=node.parents[0]
            if node.op=='add':
                add(a,c,d);add(node.parents[1],c,d)
            elif node.op=='neg':add(a,-c,-d)
            elif node.op=='mul':
                b=node.parents[1]
                add(a,c*b.value,d*b.value+c*b.tangent if second_order else np.zeros_like(c*b.value))
                add(b,c*a.value,d*a.value+c*a.tangent if second_order else np.zeros_like(c*a.value))
            elif node.op=='div':
                b=node.parents[1];bv=b.value;av=a.value
                pa=1/bv;dpa=-b.tangent/(bv*bv)
                pb=-av/(bv*bv);dpb=-a.tangent/(bv*bv)+2*av*b.tangent/(bv*bv*bv)
                add(a,c*pa,d*pa+c*dpa if second_order else np.zeros_like(c*pa))
                add(b,c*pb,d*pb+c*dpb if second_order else np.zeros_like(c*pb))
            elif node.op=='exp':add(a,c*node.value,d*node.value+c*node.tangent if second_order else np.zeros_like(c*node.value))
            elif node.op=='sum':
                add(a,np.broadcast_to(c,a.value.shape),np.broadcast_to(d,a.value.shape))
            elif node.op=='pad':add(a,c[1:-1],d[1:-1])
            elif node.op=='gather':
                if negative_control=='drop-duplicate':
                    b=np.zeros_like(a.value);db=np.zeros_like(a.value);b[node.key]=c;db[node.key]=d
                    a.cotangent+=b;a.cotangent_tangent+=db
                else:
                    np.add.at(a.cotangent,node.key,c);np.add.at(a.cotangent_tangent,node.key,d)
            else:raise TypeError('Unsupported operation '+node.op)
        inputs=[n for n in self.nodes if n.op=='input']
        if len(inputs)!=1:raise ValueError('Exactly one input vector/scalar')
        return np.array(inputs[0].cotangent,copy=True),np.array(inputs[0].cotangent_tangent,copy=True)
    def inventory(self):
        return {'nodes':len(self.nodes),'primal_rules':sum(bool(n.parents)for n in self.nodes),
                'tangent_rules':sum(bool(n.parents)for n in self.nodes),'pullbacks':self.pullbacks,
                'backward_rules':self.backward_rules,'second_rules':self.second_rules,
                'peak_node_array_bytes':sum(n.value.nbytes+n.tangent.nbytes+n.cotangent.nbytes+n.cotangent_tangent.nbytes for n in self.nodes),
                'max_node_rank':max(n.value.ndim for n in self.nodes)}
    def descriptors(self):
        return [{'id':n.index,'op':n.op,'parents':[p.index for p in n.parents],
                 'shape':list(n.value.shape),'key':n.key.tolist()if isinstance(n.key,np.ndarray)else str(n.key)}for n in self.nodes]


def build(function,x,v=None):
    tape=Tape();node=tape.variable(x,v);out=function(node)
    if not isinstance(out,(Node,list,tuple)):raise TypeError('Function erased derivative type')
    return tape,node,out


def values(output,field='value'):
    if isinstance(output,(list,tuple)):return np.array([getattr(x,field).item()for x in output])
    return np.array(getattr(output,field),copy=True)
