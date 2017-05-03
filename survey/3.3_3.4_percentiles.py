"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""
import random


def PercentileRank(scores, your_score):
    """Computes the percentile rank relative to a sample of scores."""
    count = 0
    for score in scores:
        if score <= your_score:
            count += 1

    percentile_rank = 100.0 * count / len(scores)
    return percentile_rank


scores = [77, 33, 99, 66, 55, 88]
your_score = 88

print 'score, percentile rank'
for score in scores:
    print score, PercentileRank(scores, score)
print


def Percentile(scores, percentile_rank):
    """Computes the value that corresponds to a given percentile rank. """
    scores.sort()
    for score in scores:
        if PercentileRank(scores, score) >= percentile_rank:
            return score


def Percentile2(scores, percentile_rank):
    """Computes the value that corresponds to a given percentile rank.

    Slightly more efficient.
    """
    scores.sort()
    index = percentile_rank * (len(scores) - 1) / 100
    return scores[index]


def swap(one, two, list):
    list[two], list[one] = list[one], list[two]


def Percentile3(scores, percentile_rank):
    def partition(scores, left, right, pivot_index):
        pivot_value = scores[pivot_index]
        swap(pivot_index, right, scores)
        storeIndex = left
        for i in range(left, right):
            if scores[i] < pivot_value:
                swap(storeIndex, i, scores)
                storeIndex += 1
        swap(storeIndex, right, scores)
        return storeIndex

    def QuickSelect(scores, left, right, k):
        if left == right:
            return scores[left]
        pivot_index = left + int((random.random() % (right - left + 1)))
        pivot_index = partition(scores, left, right, pivot_index)

        if k == pivot_index:
            return scores[k]
        elif k < pivot_index:
            return QuickSelect(scores, left, pivot_index - 1, k)
        else:
            return QuickSelect(scores, pivot_index + 1, right, k)

    k = percentile_rank * (len(scores) - 1) / 100

    return QuickSelect(scores, 0, len(scores) - 1, k)


print 'prank, score, score, score'
for percentile_rank in [0, 20, 25, 40, 50, 60, 75, 80, 100]:
    print percentile_rank,
    print Percentile(list(scores), percentile_rank),
    print Percentile2(list(scores), percentile_rank),
    print Percentile3(list(scores), percentile_rank)
