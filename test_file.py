__author__ = 'daybreaklee'
# Note Lesson 1
# print max([3, 4, 5]),max([3, 4, -5], key=abs)
print (7, 9, 5) > (7, 3, 2)
# ranks = ['--23456789TJQKA'.index(r) for r,s in cards]
# if ranks.count(r) == n : return r
# key = key or (lambda x: x) --> the function that maps the function to itself
def kind(n, ranks):
    """Return the first rank that this hand has exactly n of.
    Return None if there is no n-of-a-kind in the hand."""
    for r in ranks:
        if ranks.count(r) == n:
            return r
    return None
mydeck = [r+s for r in '23456789TJQKA' for s in 'SHDC']

import itertools
print [i for i in itertools.product([1,2,3],[100,200],[1000,2000])]
print [i for i in itertools.product([1],[2],[3],[4],[5],[6, 7, 8, 9, 10])]
