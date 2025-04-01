
l1 = list()
print(f"l1 :{l1}")
print(type(l1))

print("-" * 60)
l2 = [1, 2, 3, 4, 5.0, 6.2, 7.5, 8.1, 'nine', 'ten', 'eleven', 'twelve', 13+2j, 14-3j, True, False]
print(f"l2 :{l2}")
print(type(l2))

print("-" * 60)
l3 = list(range(1, 11))
print(f"l3 :{l3}")
print(type(l3))

print("-" * 60)
#CRUD
# create a list
l1 = [1, 2, 3, 'q', 4, 5]
print(f"l1 :{l1}")
print(type(l1))

print("-" * 60)
# read
print(f"l1[0] :{l1[0]}")
print(f"l1[3] :{l1[3]}")
print(f"l1[-1] :{l1[-1]}")

for i in l1:
    print(i, end=" ")
print()

for i in range(0, len(l1)):
    # print(l1[i], end=" ")
    if type(l1[i]) == str:
        print(i)
        break
print()

res = [i for i in l1 if type(i) == str]
print(res)

print("-" * 60)
# update - replace, add new value
# replace
print(f"l1 :{l1}")
l1[0] = 100
l1[3] = 'queen'
print(f"l1 :{l1}")
# add a new value
l1[4] = 'four'
print(f"l1 :{l1}")          # static so we cannot add a new value manually

print("-" * 60)
# delete
print(f"l1 :{l1}")
del l1[0]
del l1[3]

print(f"l1 :{l1}")
