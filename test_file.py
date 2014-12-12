__author__ = 'daybreaklee'
############################## Note UNIT1 #######################################
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


#####################################Notes UNIT2 ##################################
# print 01 --> 8
# generator function:
def ints(start, end):
    i = start
    while i <= end:
        yield i
        i += 1

for _ in range(10):
    print 10

import string
f = 'A + B == C'
table = string.maketrans('ABC','123')
print(f.translate(table))
eval(f.translate(table))

def compile_formula(formula, verbose=False):
    """Compile formula into a function.   Also return letters found, as a str,
    in same order as parms of function. For example, 'YOU == ME**2' returns
    (lambda Y, M, E, U, O): (U+10*O+100*Y) == (E+10*M)**2), 'YMEUO' """
    letters = ''.join(set(re.findall('[A-Z]', formula)))
    parms = ', '.join(letters)
    # map(function, iterable, ...)
    # Apply function to every item of iterable and return a list of the results.
    tokens = map(compile_word, re.split('([A-Z]+)', formula))
    body = ''.join(tokens)
    f = 'lambda %s: %s' % (parms, body)
    if verbose: print f
    return eval(f), letters

def compile_word(word):
    """Compile a word of uppercase letters as numeric digits.
    E.g., compile_word('YOU') => '(1*U+10*O+100*Y)'
    Non-uppercase words unchanged: compile_word('+') => '+'"""
    if word.isupper():
        terms = [('%s*%s' % (10**i, d))
                for (i, d) in enumerate(word[::-1])]
        return '(' + '+'.join(terms) + ')'
    else:
        return word

f = lambda Y, M, E, U, O:(1*U+10*O+100*Y) == (1*E + 10*M)**2
print f(1,2,3,4,5)
print f(2,1,7,9,8)