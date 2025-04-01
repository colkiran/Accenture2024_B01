
print("keys".center(60, "-"))
player = {'name': 'rohit', 'age': 34, 'runs': 134, 'oppn': 'Nzl'}
print(f"player :{player}")

k = player.keys()
print(f"k :{k}")

for k in player.keys():
    print(k + " => " + str(player[k]))

print('values'.center(60, "-"))
print(f"Player :{player}")

v = player.values()
print(f"v :{v}")

print("get".center(60, '-'))
print(f"Player :{player}")

print(f"Name :{player.get('name', 'Invalid key please enter a valid key')}")
print(f"Runs :{player.get('run', 'Invalid key please enter a valid key')}")

print("fromkeys".center(60, "-"))
# convert a list into a dictionary - list elements will be the dictionary keys
cities = ['blr', 'che', 'mum', 'del', 'hyd', 'kol']
print(f"cities :{cities}")

res_none = dict.fromkeys(cities)
print(f"res_none :{res_none}")

res_def = dict.fromkeys(cities, 24)
print(f"res_def :{res_def}")

print("setdefault".center(60, "-"))
# used to add new key value pairs to the dictionary

emp = {'empid': 101, 'empname': 'Mark', 'age': 34, 'desig': 'MGR'}
print(f"emp :{emp}")

emp.setdefault('empname', 'Steeve')
emp.setdefault('desig', 'TL')


emp.setdefault('dept', 'MKT')
emp.setdefault('salary', 125000)

print(f"emp :{emp}")

print("items".center(60, "-"))
# it's a combination of keys and values

emp = {
    'emp1': {'empid': 112, 'empname': 'Mark', 'age': 34, 'desig': 'MGR', 'dept': 'MKT', 'salary': 125000},
    'emp2': {'empid': 232, 'empname': 'Kevin', 'age': 32, 'desig': 'TL', 'dept': 'Finance', 'salary': 85000},
    'emp3': {'empid': 101, 'empname': 'Celene', 'age': 30, 'desig': 'SE', 'dept': 'IT', 'salary': 95000}
}

print(f"emp :{emp}")

print("-" * 60)
print(f"emp1 :{emp['emp1']}")

print("-" * 60)
print(f"emp2 :{emp['emp2']}")

print("-" * 60)
print(f"emp3 :{emp['emp3']}")

print("-" * 60)
for ky, info in emp.items():
    print(ky)
    print("-" * len(ky))
    for k, v in info.items():
        print(k, "=>", v)
    print("-" * 60)
