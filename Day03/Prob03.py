
def fun():
    print("This is normal function.......")

def out(fnc):

    def innerFun():

        fnc()

    return innerFun



def test():
    print("This is printed from inner fun.....")

fun = out(test)
fun()

print("-" * 60)

def add(x, y):
    return x + y

a = add
print(a(10, 20))

def sub(x, y):
    return x - y

a = sub
print(a(20, 12))

print("-" * 60)

lst = []
def fun(arg):
    for i in range(1, arg):
        for j in range(1, i + 1):
            lst.append(j ** 2)


fun(8500)


import time
st = time.perf_counter()
et = time.perf_counter()
