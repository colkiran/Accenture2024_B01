
class Animal:

    def __init__(self):
        print('Animal Ctor.....')
        self.a = 10

    def eat(self):
        print("Animals eat.....")

    def fun(self):
        print("fun method of Animal Class......")

class Person:

    def __init__(self):
        print("Person Ctor......")
        self.p = 20

    def walk(self):
        print("Person walks.......")

    def fun(self):
        print("fun method of Person class.....")

class Girl(Animal, Person):

    def __init__(self):
        super().__init__()              # calls the parent class                                       constructor
        Person.__init__(self)
        print("Girl Ctor.....")
        self.g = 30

    def talk(self):
        print("Girls talk........")

grace = Girl()
grace.eat()
grace.walk()
grace.talk()

grace.fun()

print("-" * 60)
print(grace.__dict__)
