import itertools
import numpy as np
from dsmc import matching_order


def test_matching_stable_cell_partition_preserves_every_distinct_priority_order():
    labels=np.array([0,0,1,1,1])
    class FixedPermutation:
        def __init__(self,values):self.values=np.array(values)
        def permutation(self,n):return self.values.copy()
    for permutation in itertools.permutations(range(5)):
        ranks=np.empty(5);ranks[list(permutation)]=np.arange(5)
        expected=np.lexsort((ranks,labels))
        actual=matching_order(labels,FixedPermutation(permutation))
        np.testing.assert_array_equal(actual,expected)
