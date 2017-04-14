import first
import Pmf


def firstBabiesPFM():
    all, firsts, others = first.MakeTables()
    first.ProcessTables(all, firsts, others)
    return Pmf.MakePmfFromList(firsts.lengths, "First Babies")


def generateFakeCohortAsDict(pmf, size):
    return {length: int(size * pmf.Prob(length)) for length in pmf.Values()}

def firstAlgorithm(pmf):
    # 1
    cohort = generateFakeCohortAsDict(pmf, 1000)
    print 'cohort', cohort
    # 2
    cohortGtEq39 = {lengthToCount[0]: 0 if lengthToCount[0] < 39 else lengthToCount[1] for lengthToCount in
                    cohort.items()}
    print 'cohort with lengths >= 39', cohortGtEq39
    # 3
    conditionalPmf = Pmf.MakePmfFromDict(cohortGtEq39)
    # 4
    print 'PMF(39): {0} \nConditional PMF(39): {1}'.format(pmf.Prob(39), conditionalPmf.Prob(39))


# def moreEfficientAlgorithm(pmf):
# 1


firstAlgorithm(firstBabiesPFM())
