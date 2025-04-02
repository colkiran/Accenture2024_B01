def fun(*args):
    print(args)

fun()
fun(10)
fun(10, 20)
fun(10, 20, 30)

print("-" * 60)

#HOF - Higher Order Function
def outerFun(fnc):

    def innerFun(*args):
        print("Logging into a service....")
        print(fnc(*args))
        print("Logging out....")
        print("-" * 60)

    return innerFun


def add(x, y):
    print(f"adding {x} and {y}")
    return x + y

def sub(x, y):
    print(f"subtracting {y} from {x}")
    return x - y

addlogger = outerFun(add)
addlogger(10, 20)

sublogger = outerFun(sub)
sublogger(30, 12)


