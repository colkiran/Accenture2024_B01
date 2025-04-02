
def funLogger(fnc):
    def helper():
        print("Myinfo logged into a service....")
        fnc()   # callback
        print("My info logger channel closed....")

    return helper

def normalFun():
    print("Call me normal function.....")

print("-" * 60)

funLogger(normalFun)()

print("-" * 60)

normalFun = funLogger(normalFun)
normalFun()         # calls the helper

print("-" * 60)

print(normalFun.__name__)


print("-" * 60)

@funLogger              # decorator   basicFun = funLogger(basicFun)
def basicFun():
    print("Call me Basic Function.....")

basicFun()      