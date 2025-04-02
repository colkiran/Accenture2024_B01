
# closure

def outerFun(greet):

    # simple curry
    def innerFun(name):

        print("Hello World")
        print(greet, name)

    return innerFun

outerFun("Hello")("Sachin")

print("-" * 60)

inref = outerFun("Greet")
inref("Sachin")
