"""
int
float
complex
"""

a = 10
b = -10
# format string or f string used for interpolation
print(f"a :{a}")
print(type(a))              # RTTI Run Time Type Identification

print(f"b :{b}")
print(type(b))

print("-" * 60)
c = 10.0
d = - 10.0

print(f"c :{c}")
print(type(c))

print(f"d :{d}")
print(type(d))

print("-" * 60)
e = +2e3
f = -2e3

print(f"e :{e}")
print(type(e))

print(f"f :{f}")
print(type(f))

print("-" * 60)
g = 3.141j
h = -3.141j

print(f"g :{g}")
print(type(g))

print(f"h :{h}")
print(type(h))

print("-" * 60)
print(10, 39, 23, 45, 30, 13, 8)
print(max(10, 39, 23, 45, 30, 13, 8))
print(min(10, 39, 23, 45, 30, 13, 8))

print("-" * 60)
x = 2 + 3.5
print(f"x :{x}")
print(type(x))

print("-" * 60)

x = 2
y = 3.5
z = x + y

print("x =", type(x))
print("y =", type(y))
print("z =", type(z))

print("Conversion".center(60, "-"))
a = 100
print(f"{type(a)}\t\t{a}")
print(f"{type(float(a))}\t\t{float(a)}")
print(f"{type(complex(a))}\t\t{complex(a)}")
print(f"{type(bool(a))}\t\t{bool(a)}")


print("Number System".center(60, "-"))
a = 100
print(f"a :{a}")
print(f"oct :{oct(a)}")
print(f"hex :{hex(a)}")
print(f"bin(a) :{bin(a)}")

