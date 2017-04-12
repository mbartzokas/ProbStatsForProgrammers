def ProbInRange(pmf, IsWithinTimeRange):
    filteredPrgLengths = {prgLength: prob for prgLength, prob in pmf.Items() if IsWithinTimeRange(prgLength)}
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


def FindAndPrintProbs(pmf):
    print '{0} pregnancy length probabilities:\nEarly {1:.2f}%\nOn Time {2:.2f}%\nLate {3:.2f}%\n'.format(
        pmf.name,
        ProbEarly(pmf) * 100,
        ProbOnTime(pmf) * 100,
        ProbLate(pmf) * 100
    )

import first

all, firsts, others = first.MakeTables()
first.ProcessTables(all, firsts, others)

import Pmf

FindAndPrintProbs(Pmf.MakePmfFromList(firsts.lengths, "First Babies"))
FindAndPrintProbs(Pmf.MakePmfFromList(others.lengths, "Other Babies"))
FindAndPrintProbs(Pmf.MakePmfFromList(all.lengths, "All Babies"))
