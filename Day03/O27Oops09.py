
class Animal:

    def __init__(self):
        print("Animal Ctor.....")
        self.age = '1 year'

    def eat(self):
        print("Animals eat.....")

class Bird(Animal):

    def fly(self):
        print("Bird fly......")

class Fish(Animal):

    def swim(self):
        print("Fish swim.....")


cuckoo = Bird()
cuckoo.eat()
cuckoo.fly()

print("-" * 60)

dolphin = Fish()
dolphin.eat()
dolphin.swim()

print("-" * 60)
print(cuckoo.__dict__)
print(dolphin.__dict__)

print("-" * 60)
print(f"isinstance(cuckoo, Bird) :{isinstance(cuckoo, Bird)}")
print(f"isinstance(cuckoo, Animal) :{isinstance(cuckoo, Animal)}")
print(f"isinstance(cuckoo, object) :{isinstance(cuckoo, object)}")
print(f"isinstance(cuckoo, Fish) :{isinstance(cuckoo, Fish)}")
