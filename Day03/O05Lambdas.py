
def add(x, y):
    return x + y

# res = add(10, 20)
a = add
res = a(100, 200)
print(f"res :{res}")

print("-" * 60)
x = lambda a, b: a + b
res = x(200, 400)
print(f"res :{res}")

print("-" * 60)
# map, filter, reduce
"""
map - will apply the given expression on all values passed to it
filter - expression in filters will return a True or False, if it returns a True then number is returned as result
reduce - as the name says reduce it will reduce the list into a single value
"""
print("map".center(60, "-"))
lst1 = list(range(1, 11))
print(f"lst1 :{lst1}")

squares = list(map(lambda x : x ** 2, lst1))
print(f"squares :{squares}")

print("-" * 60)
sentence = "the quick brown fox jumps over the lazy dog"
print(f"sentence :{sentence}")

word_len = list(map(lambda x : len(x), sentence.split()))
print(f"Word Length :{word_len}")

print("filter".center(60, "-"))
l1 = list(range(1, 31))

print("-" * 60)
print(f"l1: {l1}")

print("-" * 60)
res = list(filter(lambda x : x % 3 == 0, l1))
print(f"res :{res}")

print("-" * 60)
sentence = "the quick brown fox jumps over the lazy dog"
print(f"sentence :{sentence}")

print("-" * 60)
res1 = list(filter(lambda x : x != 'the', sentence.split()))
print(f"res1 :{res1}")

print("-" * 60)
res2 = list(filter(lambda x: len(x) == 3, sentence.split()))
print(f"res2 :{res2}")

print("reduce".center(60, "-"))
from functools import reduce

l1 = [9, 7, 1, 5, 10, 3, 8, 4, 2, 6]

res = reduce(lambda x, y: x if x > y else y, l1)
print(f"res :{res}")

res = reduce(lambda x, y: x + y, l1)
print(f"res :{res}")
