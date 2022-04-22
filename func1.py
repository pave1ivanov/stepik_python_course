# Finds the minimal value in two
def min1(x, y):
    return x if x < y else y


# Finds the minimal value in any number of values
# * operator will pack any number of values into a tuple of values
# Main flaw: returns inf if no arguments were given
def min2(*args):  # type(args) == tuple
    res = float("inf")  # float("inf") gives the biggest possible number
    for arg in args:
        if arg < res:
            res = arg
    return res


# Finds the minimal value in any number of values, but requires at leas one argument
def min3(first, *args):
    res = first
    for arg in args:
        if arg < res:
            res = arg
    return res


# * operator also unpacks any iterable object (tuple, set, list)
min(*{-4, 241, 40, 0})


# Finds the minimal value in any number of values within given range
def bounded_min(first, *args, lo=float("-inf"), hi=float("inf")):
    res = hi
    for arg in (first, ) + args:  # putting first in a tuple and combine it with the args tuple
        if arg < res and lo < arg < hi:
            res = arg
    return max(res, lo)


# You can assign multiple values with one assignment operator
acc = []
seen = set()
# Is equal to:
(acc, seen) = ([], set())

x, y, z = "xyz"
x, y, z = 1, 2, 3  # the same as (1, 2, 3)
x, y, z = [1, 2, 3]
x, y, z = {1, 2, 3}  # As set is not hashable assignment will be unordered - you don't know where will be each value

# You can assign multiple values and pack them at the same time
_x, (first, *rest, last), _y = [range(1, 6)]*3

for a, *b in [range(4), range(2)]:
    # print(b)
    pass

# Iterate through keys and values of a dict by calling items() method which returns a collection of tuple objects
for key, value in {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}.items():
    # print(key, value)
    pass

