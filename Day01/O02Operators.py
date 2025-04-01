"""
arithmetic
relational
logical
bitwise
ternary
"""
print("Arithmetic Operators".center(60, "-"))
print(f"Sum  10 + 3  = {10 + 3}")
print(f"Diff 10 - 3 = {10 - 3}")
print(f"Prod 10 * 3 = {10 * 3}")
print(f"Div  10 / 3 = {10 / 3}")
print(f"flrDiv 10 // 3  = {10 // 3}")       # floor division
print(f"Mod  10 % 3 = {10 % 3}")

print("Augmentor".center(60, "-"))
# ==, !=, >, <, >=, <=
x = 10
print(f"x :{x}")

x += 5
print(f"x :{x}")

x /= 3
print(f"x :{x}")

print("Comparison Operator".center(60, "-"))
# =-, !=, <=, >=, >, <
a = 10
b = 13

print(f"a == b :{a == b}")
print(f"a >= b :{a >= b}")
print(f"a <= b :{a <= b}")
print(f"a != b :{a != b}")

print("Logical Operators".center(60, "-"))
# and, or, not
print(f"1 == 1 and 2 == 2 :{1 == 1 and 2 == 2}")
print(f"1 == 1 and 2 == 1 :{1 == 1 and 2 == 1}")
print("-" * 60)

print(f"1 == 1 or 2 == 2 :{1 == 1 or 2 == 2}")
print(f"2 == 1 or 2 == 2 :{2 == 1 or 2 == 2}")
print("-" * 60)

print(f"not(1 == 1 and 2 == 1) :{not(1 == 1 and 2 == 1)}")
print(f"not(2 == 1 or 2 == 2) :{not(2 == 1 or 2 == 2)}")
print("-" * 60)

print(f"ord('a') :{ord('a')}")     # integer representation of unicode characters
print(f"ord('z') :{ord('z')}")
print(f"ord('A') :{ord('A')}")
print(f"ord('Z') :{ord('Z')}")

print(f"'apple' > 'orange' :{'apple' > 'orange'}")
print(f"'apple' < 'orange' :{'apple' < 'orange'}")

print("Bitwise Operators".center(60, "-"))
print(f"5 | 3 :{5 | 3}")
print(f"5 & 3 :{5 & 3}")
print(f"5 ^ 3 :{5 ^ 3}")
print(f"5 << 1 :{5 << 1}")
print(f"8 << 1 :{8 << 1}")
print(f"5 << 2 :{5 << 2}")
print(f"16 >> 1 :{16 >> 1}")
print(f"5 >> 1 :{5 >> 1}")

print("ternary operator".center(60, "-"))
age= 18
print("Eligible" if age > 17 else "Not Eligible")
