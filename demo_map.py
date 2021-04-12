# map, filter, reduce
# peroform functions on elements in lists
# map: generates a new list based on a function and a list
# filter: generates a new list by filtering out elments from an existing one
# reduce: computes a value based on a list and a function
from functools import reduce

g = [4, 5, 7, 1]
sg = ['hello', 'bat', 'perspecacity', 'cool']

def cube(x):
    return x**3

def big_word(s):
    return len(s) >= 5

def add2(a,b):
    return a + b


print(list(map(cube, g)))
print(list(map(big_word, sg)))
print(list(filter(big_word, sg)))
print(reduce(add2, g))

# using lambda instead of the small functions
print(list(map(lambda x: x**3, g)))
print(list(filter(lambda s: len(s) > 4, sg)))
print(reduce(lambda a, b: a+b, g))