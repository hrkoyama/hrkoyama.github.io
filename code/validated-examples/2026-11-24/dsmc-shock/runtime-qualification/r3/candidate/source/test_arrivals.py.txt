import numpy as np
import pytest
from dsmc import macro_arrival_count


def test_variance_reduced_arrivals_unbiased_count_and_exact_fraction_variance():
    class MidpointUniform:
        def __init__(self):self.index=0
        def random(self):
            value=(self.index+.5)/10000
            self.index+=1
            return value
    for mean in [0.,.25,4.25,1000.]:
        rng=MidpointUniform()
        values=np.array([macro_arrival_count(mean,rng) for _ in range(10000)])
        fraction=mean-np.floor(mean)
        assert np.mean(values)==mean
        assert np.var(values)==fraction*(1-fraction)
        assert set(values)<=set([int(np.floor(mean)),int(np.ceil(mean))])
    with pytest.raises(ValueError):macro_arrival_count(-1,np.random.default_rng(1))
