import Pmf
import math

def PmfMean(pmf):
    return sum([pi * xi for xi, pi in pmf.GetDict().iteritems()])

def PmfVar(pmf):
    m = PmfMean(pmf)
    return sum([pi * math.pow(xi - m, 2) for xi, pi in pmf.GetDict().iteritems()])

pmf = Pmf.MakePmfFromDict({3: 4, 4: 1, 7:1, 8:2})

print "mean is", PmfMean(pmf)
print "variance is", PmfVar(pmf)
print "standard deviation is", math.sqrt(PmfVar(pmf))