
class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        print(f"Name is {self.name}\nAge is {self.age}")

ply1 = Player('Virat', 36)
ply1.get_details()

print("-" * 60)

ply2 = Player('Rohit', 38)
ply2.get_details()

print("-" * 60)

print(f"ply1 :{ply1.__dict__}")
print(f'ply2 :{ply2.__dict__}')

print("-" * 60)
ply2.runs = 132

print(f"ply2 :{ply2.__dict__}")
print(f"ply1 :{ply1.__dict__}")


"""
self - will have the name of the object that called the method

for eg:

ply1.get_details()
ply1.name, ply1.age

"""