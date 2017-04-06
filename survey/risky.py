def ProbInRange(pmf, range):
    items = pmf.Items()
    print "items", items
    filteredItems = filter(lambda (v,f): range(v), items)
    print "filtered items", filteredItems
    return float(len(filteredItems)) / len(pmf.Items())

def ProbEarly(pmf):
    def isEarly(value):
        return value <= 37
    return ProbInRange(pmf, isEarly)

def ProbOnTime(pmf):
    def isOnTime(value):
        return 38 <= value <= 40
    return ProbInRange(pmf, isOnTime)

def ProbLate(pmf):
    def isLate(value):
        return value >= 41
    return  ProbInRange(pmf, isLate)

import first

all, firsts, others = first.MakeTables()
first.ProcessTables(all, firsts, others)

firstsAsDict = {}
for length in firsts.lengths:
    firstsAsDict[length] = firstsAsDict.get(length, 0) + 1

import Pmf

firstsPmf = Pmf.MakePmfFromDict(firstsAsDict, "first babies")
print "prob of first born early", ProbEarly(firstsPmf)

# othersPmf = Pmf.MakePmfFromDict(others, "other babies")
# allPmf = Pmf.MakePmfFromDict(all, "all live births")



