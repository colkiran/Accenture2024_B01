

def greet():
    print("Greetings Mr.Sachin Welcome to the event.....")

def greetGst(gname):
    print(f"Greetings Mr.{gname}, Welcome to the event.....")


# city is called default argument, gname is called non default argument
def greetGstCty(gname, city='Mumbai', x = 10):
    print(f"Greetings Mr.{gname} from {city}, Welcome to the event.....")



greet()

print("-" * 60)
greetGst('Rahul')
greetGst('Sourav')

print("-" * 60)
greetGstCty('Rohit')
greetGstCty('Shreyas')
greetGstCty("Rahul", "Bangalore")

print("-" * 60)

def admsn(fnm, lnm, dob, qlf, gender, cno, city, email, address):
    print(f"Name :{fnm} {lnm}")
    print(f"DOB  :{dob}")
    print(f"Qualification :{qlf}")
    print(f"Gender :{gender}")
    print(f"Contact No. :{cno}")
    print(f"City :{city}")
    print(f"Mailid :{email}")
    print(f"Address :{address}")

# args
admsn('Kevin', 'Peter', '12/10/1989', 'Mtech', 'Male', '8323042390', 'Los Angeles', 'kevin@gmail.com', '5th Avenue, 3rd street')

print("-" * 60)
# kwargs
admsn(cno='923942329', email='bob@gmail.com', city='Newyork', fnm='Bob', qlf='MS', address='downhill 4th lane, 6th floor', lnm='Marsh', dob='25/03/1988', gender='Male')



