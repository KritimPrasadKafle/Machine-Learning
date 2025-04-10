expense1 = [20,30,45]
expense2 = [45,67,34]

total = 0
for item in expense1:
    total += item
print("Expense 1's total:", total)

total = 0
for item in expense2:
    total += item
print("Expense 2's total:", total)

def total(expense):
    sum = 0
    for i in expense:
        sum += i
    return sum

h1 = total(expense1)
h2 = total(expense2)
print(h1)
print(h2)

def cylinder_volume(radius, height=1):
    print("radius is:", radius)
    print("height is:", height)
    area = 3.14*(radius**2)*height
    return area
r = 5
h = 10
print(cylinder_volume(height=h, radius=r))

r = 5
h = 10
print(cylinder_volume(radius=r))