def ProbInRange(pmf, inTime):
    filteredPrgLengths = {prgLength:prob for prgLength,prob in pmf.Items() if inTime(prgLength)}
    print "filtered pregnancy legths", filteredPrgLengths
    return sum(filteredPrgLengths.values())

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



