
def fun(stud):
    print(f"before updating :{stud}")
    stud.extend(['Joe', 'Billy', 'Mike'])
    print(f"after updating :{stud}")

snames = ['Kenith', 'Peter', 'Richard', 'Ruben', 'Louis']
print(f"Names before func call :{snames}")
fun(snames)
print(f"Names after func call :{snames}")
