"""
print(data, sep=, end="\n")
"""

for i in range(1, 11):
    print(i, end=" ")
print()             # just prints a new line

print("-" * 60)

for i in range(3, 31, 3):
    print(i, end=" ")
print()
"""
1. continue
2. break
3. else
"""

print("-" * 60)

for i in range(1, 21):
    # if i > 15:
    #     break               # stop the iteration
    if i % 2 == 0:
        continue            # skip the current iteration
    print(i, end=" ")
else:
    print("\nGeneration of numbers completed......")