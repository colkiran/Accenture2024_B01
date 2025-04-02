
def fun(x, y):
    print(f"Before :{x, y}")
    y += 10
    x += y
    print(f"After :{x, y}")

a = 100
b = 85

print(f"before func call :{a, b}")

fun(a, b)

print(f"after func call :{a, b}")
