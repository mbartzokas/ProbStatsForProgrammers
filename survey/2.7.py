import first
import Pmf


def firstBabiesPFM():
    all, firsts, others = first.MakeTables()
    first.ProcessTables(all, firsts, others)
    return Pmf.MakePmfFromList(firsts.lengths, "First Babies")


def firstAlgorithm(pmf):
    # 1
    prgLengthToNumberOfPregnancies = [(prgLength, int(1000 * pmf.Prob(prgLength))) for prgLength in pmf.Values()]
    # 2
    gtEq39 = [prgLength[1] for prgLength in prgLengthToNumberOfPregnancies if prgLength[0] >= 39]
    print gtEq39
    # 3
    conditionalPmf = Pmf.MakePmfFromList(gtEq39)
    # 4
    print pmf.Prob(39)
    print 'PMF(39): {0} \nConditional PMF(39): {1}'.format(pmf.Prob(39), conditionalPmf.Prob(39))


firstAlgorithm(firstBabiesPFM())
