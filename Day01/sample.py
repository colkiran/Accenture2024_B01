#! c:\windows\python313\bin

print("Hello World")

'print("Hello World")'

"""
print("Hello World")
print("Hello World")
"""
print("-" * 60)

def fun():
    for i in range(1, 31):
        # for loop code
        if i %2 == 0:
            # if condition code
            print("if cond code...")
            print(i)
        print("for loop code...")
    print("function code....")

fun()