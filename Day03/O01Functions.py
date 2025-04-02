
# variable length arguments

def prodAll(*numbers):
    print(numbers)
    print(*numbers)
    prod = 1
    for number in numbers:
        prod *= number
    return prod

print(prodAll(1, 2, 3, 4, 5))

print("-" * 60)
def extractDetails(**details):
    print(details)
    for k, v in details.items():
        print(k, "=>", v)

extractDetails(name='Sachin', age=36, runs=125, oppn='Aus', venue='Gabba')

print("-" * 60)
# functions can return values
def multiplyMe(x, y):
    return x * y

a = 10
b = 15

print(f"The product of {a} and {b} :{multiplyMe(a, b)}")

print("-" * 60)
def arithCalc(x, y):
    sum = x + y
    diff = x - y
    prod = x * y
    quot = x / y
    return sum, diff, prod, quot

res = arithCalc(20, 8)
print(f'res :{res}')

print("-" * 60)
# python supports recursive calls - function calling itself
# docstring

def fun():
    # this is a comment
    "This is a doc string"
    print("Hello World....")

fun()

print("-" * 60)
print(fun.__doc__)

print("-" * 60)

def fun1(x, y):
    """
    fun1(x, y)
    ----------
    1. if x and y are integers then we get the sum of the numbers
    2. if x and y are strings then we get a concatenated string
    3. if x and y are two different data types then throws an error
    """
    return x + y

print(fun1(10, 20))
print(fun1("hello ", "world"))

# print(fun1(10, "hello"))

print("-" * 60)
help(fun1)

