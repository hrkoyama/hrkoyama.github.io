"""Independent homogeneous forced-exchange exact solution; no solver imports."""
import numpy as np


def closed_step(u,v,time,epsilon,source):
    total=epsilon*u+v+source*time
    rate=1+1/epsilon
    difference=(u-v)*np.exp(-rate*time)+source/(epsilon+1)*(-np.expm1(-rate*time))
    return (total+difference)/(epsilon+1),(total-epsilon*difference)/(epsilon+1)
