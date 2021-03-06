def ProbInRange(pmf, IsWithinTimeRange):
    filteredPrgLengths = {prgLength: prob for prgLength, prob in pmf.Items() if IsWithinTimeRange(prgLength)}
    return sum(filteredPrgLengths.values())

def ProbEarly(pmf):
    return ProbInRange(pmf, lambda week: week <= 37)

def ProbOnTime(pmf):
    return ProbInRange(pmf, lambda week: 38 <= week <= 40)

def ProbLate(pmf):
    return ProbInRange(pmf, lambda week: week >= 41)


def FindAndPrintProbs(pmfName, probEarly, probOnTime, probLate):
    print '{0} pregnancy length probabilities:\nEarly {1:.2f}%\nOn Time {2:.2f}%\nLate {3:.2f}%\n'.format(
        pmfName,
        probEarly * 100,
        probOnTime * 100,
        probLate * 100
    )

import first

all, firsts, others = first.MakeTables()
first.ProcessTables(all, firsts, others)

import Pmf

pmfFirst = Pmf.MakePmfFromList(firsts.lengths, "First Babies")
firstProbEarly = ProbEarly(pmfFirst)
firstProbOnTime = ProbOnTime(pmfFirst)
firstProbLate = ProbLate(pmfFirst)
FindAndPrintProbs(pmfFirst.name, firstProbEarly, firstProbOnTime, firstProbLate)

pmfOthers = Pmf.MakePmfFromList(others.lengths, "Other Babies")
otherProbEarly = ProbEarly(pmfOthers)
otherProbOnTime = ProbOnTime(pmfOthers)
otherProbLate = ProbLate(pmfOthers)
FindAndPrintProbs(pmfOthers.name, otherProbEarly, otherProbOnTime, otherProbLate)

pmfAll = Pmf.MakePmfFromList(all.lengths, "All Babies")
allProbEarly = ProbEarly(pmfAll)
allProbOnTime = ProbOnTime(pmfAll)
allProbLate = ProbLate(pmfAll)
FindAndPrintProbs(pmfAll.name, allProbEarly, allProbOnTime, allProbLate)

print "first vs others relative risk: early", firstProbEarly / otherProbEarly
print "first vs others relative risk: on time", firstProbOnTime / otherProbOnTime
print "first vs others relative risk: late", firstProbLate / otherProbLate
