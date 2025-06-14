nums = [1,2,3,4,5]
for num in nums:
    if num == 3:
        print('Found!')
        break
    print(num)


nums = [1,2,3,4,5]
for num in nums:
    if num == 3:
        print('Found!')
        continue
    print(num)

for num in nums:
    for letter in 'abc':
        print(num, letter)


for i in range(1, 10):
    print(i)

for i in enumerate(nums, start=1):
    print(i)

x = 0
while x < 10:
    print(x)
    x += 1

x = 1
while x < 10:
    if x == 5:
        break
    print(x)
    x+=1


print("Continue")
s = 1
while s < 10:
    if s == 7:
        # print('Found')
        continue
    print(s)
    s += 1