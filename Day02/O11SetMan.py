
s1 = set()
print(f"s1 :{s1}")
print(type(s1))
print("-" * 60)

s2 = {0, 1, 2, 3, 4, 5.0, 6.2, 7.3, 8.1, 'nine', 'ten', 'eleven', 'thirteen', 14+2j, 15-3j, True, False}
print(f"s2 :{s2}")
print(type(s2))
print("-" * 60)

s3 = set(range(1, 11))
print(f"s3 :{s3}")
print(type(s3))
print("-" * 60)

# print(dir(s1))
s1= set()
print(f"s1 :{s1}")

print("add".center(60, "-"))
s1.add(1)
s1.add(2)
s1.add(1)
s1.add(3)
s1.add(1)
s1.add(2)
s1.add(4)
s1.add(1)

print(f"s1 :{s1}")
s1.update([1, 2, 3, 4])
s1.update([4, 3, 2, 1])
s1.update([4, 5, 6, 7])
s1.update([6, 7, 8, 9])
s1.update([5, 6, 7, 8])
s1.update([1, 2, 3, 10])

print(f"s1 :{s1}")
print("-" * 60)
dir(s1)

print("-" * 60)
# remove values of a set = pop, remove, discard
print(f"s1 :{s1}")

# pop
res = s1.pop()
print(f"res :{res}")

res = s1.pop()
print(f"res :{res}")

res = s1.pop()
print(f"res :{res}")

print("-" * 60)
# remove
s1.remove(10)
s1.remove(7)

# s1.remove(1)
print(f"s1: {s1}")

print("-" * 60)
# discard

s1.discard(4)
s1.discard(5)

s1.discard(1)
print(f"s1 :{s1}")

print("-" * 60)
A = {1, 2, 3, 4, 5, 6}
B = {5, 6, 7, 8, 9, 10}

print(f"A :{A}")
print(f"B :{B}")

print("-" * 60)
print(f"A union B :{A | B}")
print(f"B union A :{B.union(A)}")

print("-" * 60)
print(f"A intersection B :{A & B}")
print(f"B intersection A :{B.intersection(A)}")

print("-" * 60)
print(f"A difference B :{A - B}")
print(f"B difference A :{B.difference(A)}")

print("-" * 60)
print(f'A symmetric difference B :{A ^ B}')
print(f"B symmetric difference A :{B.symmetric_difference(A)}")

print("-" * 60)
# frozen sets are immutable

fs = frozenset([1, 2, 3, 4, 5])
print(f"fs :{fs}")
print(type(fs))

