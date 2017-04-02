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
all, firstBabies, others = first.MakeTables()
first.ProcessTables(firstBabies, others)

firstBabies.s = math.sqrt(thinkstats.Var(firstBabies.lengths, firstBabies.mu))
others.s = math.sqrt(thinkstats.Var(others.lengths, others.mu))

print 'first babies mean:', firstBabies.mu, 'standard deviation:', firstBabies.s
print 'others mean:', others.mu, 'standard deviation:', others.s
print 'mean difference (hours)', (firstBabies.mu - others.mu) * 7 * 24
print 'spread difference (hours)', (firstBabies.s - others.s) * 7 * 24

# Distributions
hist = {}
for length in firstBabies.lengths:
    hist[length] = hist.get(length, 0) + 1

print hist

pmf = {}
n = float(firstBabies.n)
for x, freq in hist.items():
    pmf[x] = freq / n

print pmf

# 2.3
import Pmf
def Mode(hist):
    return max(hist.Items(), key=lambda (val, freq): freq)

hist = Pmf.MakeHistFromList([1,2,2,3,5])
print 'Mode', Mode(hist)

def AllModes(hist):
    return sorted(hist.Items(), cmp=lambda f1,f2: f2 - f1 , key=operator.itemgetter(1))

print 'All Modes', AllModes(hist)