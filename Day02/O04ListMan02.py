
values = list(range(10, 31, 10))
print(f"values :{values}")

# unpack
a, b, c = values
print(a, b, c, sep=", ")

print("-" * 60)
values = list(range(10, 101, 10))
print(f"values :{values}")

print("-" * 60)
# *c can accept more than one value
a, b, *c = values
print(a, b, c, sep=", ")

print("-" * 60)
a, *b, c = values
print(a, b, c, sep=", ")

print("-" * 60)
*a, b, c = values
print(a, b, c, sep=", ")

print("-" * 60)
lst1 = [1, 2, 3, 4, 5]
lst2 = [11, 22, 33, 44, 55]

print(f"lst1 :{lst1}")
print(f"lst2 :{lst2}")

lst3 = [lst1, lst2]
print(f"lst3 :{lst3}")
print(len(lst3))

print("-" * 60)
lst4 = [*lst1, *lst2]           # unpack
print(f"lst4 :{lst4}")
print(len(lst4))

print("Enumerate".center(60, "-"))
letters = ['a', 'b', 'c', 'd', 'e', 'f']
print(f"letters :{letters}")

print("-" * 60)
for letter in letters:
    print(letter, end=" ")
print()

print("-" * 60)
for letter in enumerate(letters):
    print(letter, end=" ")
print()

print("-" * 60)
for letter in enumerate(letters):
    print(letter[0], "\t", letter[1])

print("-" * 60)
for letter, index in enumerate(letters):
    print(f"{letter} \t {index}")

print("-" * 60)
my_lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"my_lst :{my_lst}")

print("-" * 60)
for ind, lst in enumerate(my_lst):
    print(f"{ind} \t {lst}")

print("-" * 60)
for ind, lst in enumerate(my_lst):
    print(f"List({ind})")
    for idx, num in enumerate(lst):
        print(f"\t{idx}\t{num}")

print("-" * 60)
print(type(my_lst))
print(dir(my_lst))
