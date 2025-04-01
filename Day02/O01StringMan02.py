
# maketrans, translate

print("maketrans".center(60, "-"))
st = "mango a good fruit"
print(f"st :{st}")

print("-" * 60)
a = 'mango'
b = 'apple'
# Length of a and b should be the same
resTbl = st.maketrans(a, b)
print(resTbl)

print("translate".center(60, "-"))
res = st.translate(resTbl)
print(f"res :{res}")

print("format".center(60, "-"))
# emulate printf of C language

format = "Welcome %s, what a %s player"
print(format)

values = ("sachin", "superb")       # tuple
print(values)

print(format % values)

print("-" * 60)
format = "welcome %s your rating of %.3f, what a %s player"
print(format % ('sachin', 4, "class"))
print(format % ('sachin', 4.8, "class"))
print(format % ('sachin', 4.799999999, "class"))
print("-" * 60)
print("welcome %s, your rating of %.3f, what a %s player" % ('sachin', 4.78934, 'class'))

# emulate unix shell
from string import Template
tmpl = Template("Welcome $name, What a $adjective player")
print(f"tmpl :{tmpl}")
print(tmpl.substitute(name="Sachin", adjective="superb"))


print("-" * 60)
# format strings from python
print("Welcome {}, what a {} player for {}".format("Sachin", "class", "India"))

print("Welcome {0}, what a {1} player for {2}".format("Sachin", "class", "India"))

print("Welcome {2}, what a {0} player for {1}".format("Sachin", "class", "India"))

print("Welcome {gname} what a {adj} player for {ctry}".format(gname = "Sachin", adj = "superb", ctry="India"))

print("Welcome {gname} with a rating of {rating:.3f}, what a {adj} player".format(gname="Rahul", rating = 4.89999, adj = "class"))

print("-" * 60)
# interpolation
from math import pi, e
print(f"PI = {pi} and Eulers constant = {e}")

print("PI = {} and Eulers Constant = {}".format(pi, e))

print("PI = {} and Eulers Constant = {} magic number = {magic}".format(pi, e, magic=40585))

print("PI = {0} and Eulers Constant = {1} magic number = {magic}".format(pi, e, magic=40585))

print("-" * 60)
full_name = ['Sachin', 'Tendulkar']
print(f"Full Name :{full_name}")
print("Mr.{name}".format(name=full_name))
print("Mr.{name[0]} {name[1]}".format(name=full_name))
