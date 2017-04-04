import Pmf

def PmfMean(pmf):
    return sum([pi * xi for pi,xi in pmf.GetDict().iteritems()])

def PmfVar(pmf):

pmf = Pmf.MakePmfFromDict({3: 4, 4: 1, 7:1, 8:2})

print "mean is", PmfMean(pmf)