from abc import ABC, abstractmethod

class Account(ABC):

    def __init__(self):
        print("ABC Ctor.....")

    def deposit(self):
        pass

    def withdraw(self):
        pass

    @abstractmethod
    def get_balance(self):
        pass

class Savings(Account):

    def get_balance(self):
        print("Balance in the account is ######.##")

sav1 = Savings()
sav1.get_balance()
