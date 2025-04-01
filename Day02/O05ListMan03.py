
# add new values into the list
print("append".center(60, "-"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 :{l1}")

l1.append(6)
l1.append(7)
l1.append(8)

print(f"l1 :{l1}")
l1.append([9, 10, 11, 12, 13])
print(f"l1 :{l1}")

# append can add one element at a time

# extend
print("extend".center(60, "-"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 :{l1}")

l1.extend([6, 7, 8, 9])
print(f"l1 :{l1}")

l1.extend([10])
print(f"l1 :{l1}")

# insert
print("insert".center(60, "-"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 :{l1}")

l1.insert(1, 1.5)
l1.insert(3, 2.5)
l1.insert(5, 3.5)
l1.insert(7, 4.5)

print(f"l1 :{l1}")

# sort
"""
sort - sorts the original list
sorted - takes a copy of the list sorts it and returns it as a result
"""
print("sort".center(60, "-"))
l1 = [9, 5, 8, 10, 2, 4, 6, 1, 7, 3]
print(f"l1 :{l1}")

res_asc = sorted(l1)
res_desc = sorted(l1, reverse=True)
print(f"Ascending Order :{res_asc}")
print(f"Descending Order :{res_desc}")

print("-" * 60)
l1 = [9,'zebra', 5, 'xray', 8, 'yellow', 10, 'blue', 2, 'white', 4, 'violet', 6, 'green', 1, 'maroon', 7, 'pink', 3, 'orange', 'apple', 'cat', 'elephant', 'dog', 'queen', 190, 1234, 28, 265, 2018]

print(f"l1 :{l1}")

print("-" * 60)
res = sorted(l1, key=ascii)
print(f"res :{res}")

print("-" * 60)
print(sorted([i for i in l1 if type(i)==str])+sorted([i for i in l1 if type(i)==int]))

print("-" * 60)
for i in range(0, len(res)):
    if type(res[i]) == int:
        # print(i)
        break

print(f"{res[:i] + sorted(res[i:])}")

print("-" * 60)
cities = ['vishakapatnam', 'thiruvananthapuram', 'bangalore', 'chennai', 'mumbai', 'pune', 'delhi', 'hyderabad', 'ooty', 'kolkata']
print(f"cities :{cities}")

print("-" * 60)
# sorted

res_asc = sorted(cities, key=len)
print(f"Ascending Order :{res_asc}")
