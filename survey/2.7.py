import first
import Pmf


def firstBabiesPFM():
    all, firsts, others = first.MakeTables()
    first.ProcessTables(all, firsts, others)
    return Pmf.MakePmfFromList(firsts.lengths, "First Babies")


def generateFakeCohortAsDict(pmf, size):
    return {length: int(size * pmf.Prob(length)) for length in pmf.Values()}


def firstSolution(pmf):
    print '*** Conceptually clear solution ***'
    # 1
    cohort = generateFakeCohortAsDict(pmf, 1000)
    print 'cohort', cohort
    # 2
    cohortGtEq39 = {lengthToCount[0]: 0 if lengthToCount[0] < 39 else lengthToCount[1] for lengthToCount in
                    cohort.items()}
    print 'cohort with lengths >= 39', cohortGtEq39
    # 3
    conditionalPmf = Pmf.MakePmfFromDict(cohortGtEq39, pmf.name + " with pregnancy length >= 39")
    # 4
    print 'PMF(39): {0} \nConditional PMF(39): {1}'.format(pmf.Prob(39), conditionalPmf.Prob(39))


def moreEfficientSolution(pmf):
    print '*** More efficient solution ***'
    # 1
    # cohort = generateFakeCohortAsDict(pmf, 1000)
    # print 'cohort', cohort
    # # 2
    # for length in cohort.keys():
    #     if length < 39:
    #         pmf.Remove(length)

    conditionalPmf = pmf.Copy(pmf.name + " with pregnancy length >= 39")
    for length in pmf.Values():
        if length < 39:
            conditionalPmf.Remove(length)

    conditionalPmf.Normalize()
    print 'PMF(39): {0} \nConditional PMF(39): {1}'.format(pmf.Prob(39), conditionalPmf.Prob(39))


firstSolution(firstBabiesPFM())
moreEfficientSolution(firstBabiesPFM())
