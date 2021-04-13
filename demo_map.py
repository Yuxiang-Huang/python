# map, filter, reduce
# perform functions on each element of a list
# map: creates a new list by applying a function to each element of a list
# filter: creates a new list by filtering out elements based on a boolean
#         test function
# reduce: computer a single value based on a list
from functools import reduce

g = [4, 5, 7, 1]
sg = ['hello', 'bat', 'perspecacity', 'cool']

def cube(x):
    return x**3

def big_word(s):
    return len(s) >= 5

def add2(a,b):
    print(a, b)
    return a + b
