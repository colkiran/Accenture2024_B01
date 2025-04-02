
def bankflow(fnc):          # HOF
    print("-" * 60)
    print("logging in....")
    res = fnc()                       # call back
    print(res)
    print("logging out.....")
    print("-" * 60)


def withdraw():
    print("debited.....")

def deposit():
    print("credited......")

def transfer():
    return "amount transfered...."

bankflow(deposit)

bankflow(withdraw)

bankflow(transfer)