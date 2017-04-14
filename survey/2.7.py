import first
import Pmf


def firstBabiesPFM():
    all, firsts, others = first.MakeTables()
    first.ProcessTables(all, firsts, others)
    return Pmf.MakePmfFromList(firsts.lengths, "First Babies")


def firstAlgorithm(pmf):
    # 1
    lengthsToCounts = {length: int(1000 * pmf.Prob(length)) for length in pmf.Values()}
    print 'lengthsToCounts', lengthsToCounts
    # 2
    gtEq39 = {lengthToCount[0]: 0 if lengthToCount[0] < 39 else lengthToCount[1] for lengthToCount in
              lengthsToCounts.items()}
    print 'lengthsToCountGtEq39', gtEq39
    # 3
    conditionalPmf = Pmf.MakePmfFromDict(gtEq39)
    # 4
    print 'PMF(39): {0} \nConditional PMF(39): {1}'.format(pmf.Prob(39), conditionalPmf.Prob(39))


firstAlgorithm(firstBabiesPFM())
