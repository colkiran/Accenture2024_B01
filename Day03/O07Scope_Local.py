
def fun(x):         # x is a local variable - lexical scope
    print(f"x :{x}")
    y = "hello world"   # local varaible
    print(y)

fun(100)

# print(f"x :{x}")
# print(f"y :{y}")