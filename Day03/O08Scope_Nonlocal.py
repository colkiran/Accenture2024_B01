
# nested functions

def outerFun():
    gname = "Sachin"                # local variable
    def innerFun():
        nonlocal gname          # only local variables can be converted                         into non-local

        gname += " Tendulkar"
        print("Hello World")
        print(f"Greetings Mr.{gname}")

    innerFun()
    print(f'outerfun :{gname}')


outerFun()
