import survey

def NumberOfLiveBirths(table):
    sum = 0
    for r in table.records:
        if (r.outcome == 1):
            sum += 1
    return sum

table = survey.Pregnancies()
table.ReadRecords()
print 'Number of pregnancies', len(table.records)

liveBirths = [pregnancy for pregnancy in table.records if pregnancy.outcome == 1]
numberOfLiveBirths = len(liveBirths)
print 'Number of live births', numberOfLiveBirths

firstBabies = [liveBirth for liveBirth in liveBirths if liveBirth.birthord == 1]
others = [liveBirth for liveBirth in liveBirths if liveBirth.birthord != 1]
print 'First babies', len(firstBabies)
print 'Others', len(others )

avgPrgLengthFirstBabies = float(sum([firstBaby.prglength for firstBaby in firstBabies])) / len(firstBabies)
print 'Average pregnancy length (weeks) of first babies', avgPrgLengthFirstBabies

avgPrgLengthOthers = float(sum([other.prglength for other in others])) / len(others)
print 'Average pregnancy length (weeks) of others', avgPrgLengthOthers

