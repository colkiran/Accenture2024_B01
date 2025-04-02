
def outerFun():
    gname = "Sachin"
    def innerFun():

        print("Hello World")
        print(f"Greetings Mr.{gname}")

    innerFun()

outerFun()
