
def funlogger(fnc):
    def helper(x, y):
        print("My info Logged into the server.....")
        res = fnc(x, y)
        print(res)
        print("My info logged out......")
        print("-" * 60)

    return helper

@funlogger
def add(a, b):
    return a + b


@funlogger
def sub(a, b):
    return a - b

add(34, 63)
sub(82, 39)
