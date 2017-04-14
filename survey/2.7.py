import first
import Pmf


def firstBabiesPFM():
    all, firsts, others = first.MakeTables()
    first.ProcessTables(all, firsts, others)
    return Pmf.MakePmfFromList(firsts.lengths, "First Babies")


def generateFakeCohortAsDict(pmf, size):
    return {length: int(size * pmf.Prob(length)) for length in pmf.Values()}


def conceptuallyClearSolution(pmf, x):
    print '*** Conceptually clear solution ***'
    # 1
    cohort = generateFakeCohortAsDict(pmf, 1000)
    print 'cohort', cohort
    # 2
    cohortGtEqX = {lengthToCount[0]: 0 if lengthToCount[0] < x else lengthToCount[1] for lengthToCount in
                   cohort.items()}
    print 'cohort with lengths >= ', x, cohortGtEqX
    # 3
    conditionalPmf = Pmf.MakePmfFromDict(cohortGtEqX, pmf.name + ' with pregnancy length >= {0}'.format(x))
    # 4
    print 'PMF({2}): {0} \nConditional PMF(39): {1}'.format(pmf.Prob(x), conditionalPmf.Prob(x), x)


def ConditionalPmfMoreEfficient(pmf, x):
    # print '*** More efficient solution ***'

    conditionalPmf = pmf.Copy(pmf.name + " with pregnancy length >= x weeks")
    for length in pmf.Values():
        if length < x:
            conditionalPmf.Remove(length)

    conditionalPmf.Normalize()
    return conditionalPmf
    # print 'PMF({2}): {0} \nConditional PMF({2}): {1}'.format(pmf.Prob(x), conditionalPmf.Prob(x), x)


# conceptuallyClearSolution(firstBabiesPFM(), 39)
# moreEfficientSolution(firstBabiesPFM(), 39)


pmf = firstBabiesPFM()
lengths = pmf.Values()
print 'lengths', lengths
conditionalProbs = [ConditionalPmfMoreEfficient(pmf, length).Prob(length) for length in lengths]
print 'Probabilities born at x given not born before x', conditionalProbs

import matplotlib.pyplot as pyplot

m = pyplot.bar(lengths, conditionalProbs)
pyplot.show()
