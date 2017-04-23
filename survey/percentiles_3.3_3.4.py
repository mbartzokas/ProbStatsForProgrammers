def PercentileRank(scores, your_score):
    count = 0
    for score in scores:
        if score <= your_score:
            count += 1

    percentile_rank = 100.0 * count / len(scores)
    return percentile_rank


# We call the value percentile
def Percentile(scores, percentile_rank):
    scores.sort()

    for score in scores:
        if PercentileRank(scores, score) >= percentile_rank:
            return score


scores = [66, 99, 55, 77, 88]
value = 66
print "The percentile rank for value {0} is {1}".format(value, PercentileRank(scores, value))
percentile = 30
print "The corresponding value for percentile {0} is {1}".format(percentile, Percentile(scores, percentile))
