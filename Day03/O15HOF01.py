

def callMe():
    print(f"Apples from Ooty")


def fun(fnc):
    print("Hello")
    fnc()
    print("hi")
    print('_' * 40)

    def defineMe():
        print(f"Oranges from Kanpur")
    return defineMe


def funCallback(fnc):
    print("Mera Barath Mahan....")
    fnc()
    print("India is great......")


funCallback(fun(callMe))




"""


a = 10
b = 30

def fun(x):
    print(f"Hello World :{x}")

def add(x, y):
    return x + y

fun(add(a, b))


"""








