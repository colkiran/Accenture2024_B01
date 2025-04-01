
# Conversions
print("Conversions".center(60, "-"))
print("{val} {val} {val}".format(val = "A"))
print("{val!s} {val!r} {val!a}".format(val = "A"))

print("-" * 60)
print("{num} {num} {num}".format(num=36))
print("{num} {num:f} {num:b}".format(num=36))
print("{num:10} {num:f} {num:b}".format(num=36))
print("{num:5} {num:f} {num:b}".format(num=36))
print("{num:5} {num:f} {num:b}".format(num=369237293))

# alignment
print("Alignment".center(60, '-'))
print("{num:15} Tendulkar".format(num=3))
print("{num:15} Tendulkar".format(num="Sachin"))
print("{}".format("Sachin Tendulkar"))
print("{:.6}".format("Sachin Tendulkar"))

print("-" * 60)
from math import pi
print("{pi}".format(pi = pi))
print("{pi:10.2}".format(pi = pi))
print("{pi:10.3}".format(pi = pi))
print("{pi:10.4}".format(pi = pi))
print("{pi:10.5}".format(pi = pi))
print("{pi:10.6}".format(pi = pi))

print("-" * 60)
print("{pi:010.2}".format(pi = pi))
print("{pi:010.3}".format(pi = pi))
print("{pi:010.4}".format(pi = pi))
print("{pi:010.5}".format(pi = pi))

print("-" * 60)
print("{:>15} Tendulkar".format("Sachin"))          # right align
print("{:^15} Tendulkar".format("Sachin"))          # center align
print("{:<15} Tendulkar".format("Sachin"))          # left align

print("-" * 60)

print("{:-^60}".format("Sachin Tendulkar"))          # center align
print("Sachin Tendulkar".center(60, "-"))

