
# indefinite loop
# while (condition is True) keep executing the loop

i = 1
while i <= 10:
    print(i, end=" ")
    i += 1
print()

print("-" * 60)
print(f"i after the loop :{i}")

while(True):
    print(i, end=" ")
    i -= 1
    if i == 0:
        break
print()

