expenses = [1200,1500,1300,1700]
total = expenses[0] + expenses[1] + expenses[2] + expenses[3]
print(total)

total = 0
for expense in expenses:
    total = total + expense
print(total)

print(range(1,22))
print(list(range(1,22)))
for i in range(1,11):
    print(i)

total = 0
for i in range(len(expenses)):
    print(f"Month {i+1}, expense: {expenses[i]}")
    total += expenses[i]
print(f"Total expenses is {total}")

key_location = "chair"
locations = ["sofa", "garage", "chair", "table", "closet"]
for loc in locations:
    if loc == key_location:
        print("Key found at: ", loc)
        break
    else:
        print("Key not found in:", loc)


for i in range(11):
    if i%2 == 0:
        continue
    print(i)

num = 0
while num<=10:
    print(num)
    num=num+1