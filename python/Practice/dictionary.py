d = {"tom": 9876543, "rob": 23456789, "joe": 3456778}
d
print(d)

print(d["tom"])

d["sam"] = 34562345
print(d)

del d["sam"]
print(d)

for key in d:
    print("key", key, "value", d[key])

for k,v in d.items():
    print("Key: ",key, "value: ", d[key])

point=(5,9)
print(point[0])
print(point[1])

point[0] =4
print(point)
