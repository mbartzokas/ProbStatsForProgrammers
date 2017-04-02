import thinkstats
import math
import first
import operator

# ex 2.1
class Pumpkin():
    def __init__(self, weight):
        self.weight = weight

pumpkins = [Pumpkin(1), Pumpkin(1), Pumpkin(1), Pumpkin(3), Pumpkin(3), Pumpkin(591)]

def Pumpkin():
    weights = [p.weight for p in pumpkins]
    mu, var = thinkstats.MeanVar(weights)
    s = math.sqrt(var)
    return (mu, var, s)

print 'mean, variance, standard deviation', Pumpkin()

# ex 2.2
all, firsts, others = first.MakeTables()
first.ProcessTables(firsts, others)

firsts.s = math.sqrt(thinkstats.Var(firsts.lengths, firsts.mu))
others.s = math.sqrt(thinkstats.Var(others.lengths, others.mu))

print 'first babies mean:', firsts.mu, 'standard deviation:', firsts.s
print 'others mean:', others.mu, 'standard deviation:', others.s
print 'mean difference (hours)', (firsts.mu - others.mu) * 7 * 24
print 'spread difference (hours)', (firsts.s - others.s) * 7 * 24

# Distributions
firstsPrgLengthFreqDict = {}
for length in firsts.lengths:
    firstsPrgLengthFreqDict[length] = firstsPrgLengthFreqDict.get(length, 0) + 1

print firstsPrgLengthFreqDict

firstsPrgLengthProbDict = {}
n = float(firsts.n)
for x, freq in firstsPrgLengthFreqDict.items():
    firstsPrgLengthProbDict[x] = freq / n

print firstsPrgLengthProbDict

# 2.3
import Pmf
def Mode(hist):
    return max(hist.items(), key=lambda (val, freq): freq)

# firstsHist = Pmf.MakeHistFromList([1, 2, 2, 3, 5])
print 'Mode', Mode(firstsPrgLengthFreqDict)

def AllModes(hist):
    return sorted(hist.items(), cmp=lambda f1,f2: f2 - f1 , key=operator.itemgetter(1))

print 'All Modes', AllModes(firstsPrgLengthFreqDict)

import matplotlib.pyplot as pyplot
# vals, freqs =  .Render()
rectangles = pyplot.bar(firstsPrgLengthFreqDict.keys(), firstsPrgLengthFreqDict.values())
pyplot.show()

