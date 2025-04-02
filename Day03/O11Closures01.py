
def outerFun():
    gname = "Sachin"
    def innerFun():

        print("Hello World")
        print(f"Greetings Mr.{gname}")

    return innerFun

print(outerFun.__name__)
print(outerFun().__name__)

print("-" * 60)

innref = outerFun()

print("hello world \n" * 10)

innref()