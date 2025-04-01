
print("pop".center(60, "-"))
emp2 = {'empid': 232, 'empname': 'Kevin', 'age': 32, 'desig': 'TL', 'dept': 'Finance', 'salary': 85000}

print(f"emp2 :{emp2}")

res = emp2.pop('age')
print(res)

res = emp2.pop('dept')
print(res)

print(f"emp2 :{emp2}")

print("popitem".center(60, '-'))
emp2 = {'empid': 232, 'empname': 'Kevin', 'age': 32, 'desig': 'TL', 'dept': 'Finance', 'salary': 85000}

print(f"emp2 :{emp2}")

res = emp2.popitem()
print(f"res :{res}")

res = emp2.popitem()
print(f"res :{res}")

print(f"emp2 :{emp2}")

print("update".center(60, "-"))
emp1 = {'empid': 112, 'empname': 'Mark', 'age': 34, 'desig': 'MGR', 'salary': 125000}
emp2 = {'empid': 232, 'empname': 'Kevin', 'age': 32, 'desig': 'TL', 'dept': 'Finance'}

print(f"emp1 :{emp1}")
print("-" * 60)

print(f"emp2 :{emp2}")
print("-" * 60)

emp1.update(emp2)
print(f"emp1 :{emp1}")

print("clear".center(60, "-"))
emp1 = {'empid': 112, 'empname': 'Mark', 'age': 34, 'desig': 'MGR', 'salary': 125000}
print(f"emp1 :{emp1}")

emp1.clear()
print(f"emp1 :{emp1}")
