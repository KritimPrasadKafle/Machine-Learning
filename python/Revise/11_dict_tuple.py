captains = {
    'nepal': 'Paras',
    'pakistan': 'Babar',
    'india': 'Sachin'
}

print(type(captains))

print(captains['india'])

print(captains.keys())

print(captains.values())

captains['england'] = 'root'
print(captains)

del captains['england']

print(captains)

for team in captains:
    print(team,"==>", captains[team])

print("-------")
for team, captain in captains.items():
    print(team,"==>", captain)

s = 'india'
print(s in captains)

print(captains.clear())
print(captains)

e = {}
e['age'] = 35
e['name'] = 'rajesh'
e['id'] = 123
print(e)


#Tuple
point = (4,10)
print(type(point))

point=(4,10,20)
print(type(point))

print(point[1])

# point[1] = 67

def add_multiply(a,b):
    total = a+b
    m=a*b
    return total, m

s,m = add_multiply(4,5)
print(s)
print(m)