
def outerFun(greet):

    def innerFun(sep):

        def innerMostFun(gname):

            from emojis import emojis

            emojized = emojis.encode(greet + " :" + sep + ": " + gname)

            print(emojized)

        return innerMostFun

    return innerFun

hndGrt = outerFun("Namaskar")

hndGrtTgr = hndGrt("tiger")
hndGrtLion = hndGrt("lion")

hndGrtTgr("Shroff")
hndGrtLion("Ramesh")






"""
outerFun("Greetings ")("---->")("Sachin")

print("-" * 60)

engGrt = outerFun("Hello")
hndGrt = outerFun("Namaskar")

engGrtSngArrow = engGrt("----->")
hndGrtDblArrow = hndGrt("======>>")

engGrtSngArrow("Sachin")
hndGrtDblArrow("Jadeja")
"""