
d1 = dict()
print(f"d1 :{d1}")
print(type(d1))

print("-" * 60)
d2 = {'name': 'sachin', 'age': 36, 'runs': 120, 'oppn': 'SA'}
print(f"d2 :{d2}")
print(type(d2))

print("-" * 60)
d3 = dict([('name', 'rahul'), ('age', 33), ('runs', 135), ('oppn', 'Eng')])
print(f"d3 :{d3}")
print(type(d3))

print("-" * 60)
d4 = dict(name='Virat', age=29, runs=105, oppn='Aus')
print(f"d4 :{d4}")
print(type(d4))

print("-" * 60)
# CRUD
player = {'name': 'Sachin', 'age': 36, 'runs': 98, 'oppn': 'AUS'}
print(f"Player :{player}")

print("-" * 60)
# read
print(f"Name: {player['name']}")
print(f"Runs: {player['runs']}")

print("-" * 60)
# iterate
for i in player:
    print(i, "=>", player[i])

print("-" * 60)
# update - modify, add new key and value
player['name'] = 'Tendulkar'
player['runs'] = 120

player['year'] = ('2001')
player['venue'] = 'MCB'
print(f"player :{player}")

print("-" * 60)
# delete
print(f"player :{player}")

del player['age']
del player['year']

print(f"player :{player}")

print("-" * 60)
print(dir(player))
