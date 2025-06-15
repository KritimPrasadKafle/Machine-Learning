nums = [1,2,3,4,5,6,7,8,9,10]

#I want 'n' for each 'n' in nums
my_list = []
for n in nums:
    my_list.append(n)
print(my_list)

#list comprehension
my_list = [n for n in nums]
print(my_list)

#I want 'n*n' for each 'n' in nums
my_list = []
for n in nums:
    my_list.append(n*n)
print(my_list)

#list comprehension
my_list = [n*n for n in nums]
print(my_list)

#Using a map + lambda
my_list = map(lambda n: n*n, nums)
print(my_list)


#I want 'n' for wach 'n' in nums if 'n' is even
my_list = []
for n in nums:
    if n%2==0:
        my_list.append(n)
print(my_list)

my_list = [n for n in nums if n%2==0]
print(my_list)

#Using a filter + lambda
my_list = filter(lambda n: n%2 == 0, nums)
print(my_list)

#I want a (letter, num) pair for each letter in 'abcd' and each number in '0123'
my_list = []
for letter in 'abcd':
    for num in range(4):
        my_list.append((letter, num))
print(my_list)

#list comprehension

my_list = [(letter, num) for letter in 'abcd' for num in range(4)]
print(my_list)

#Dictionary Comprehension
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
res = zip(names, heros)
print(list(res))

#I want a dict{'name': 'hero'} for each name, hero in zip(names, heros)
my_dict = {}
for name, hero in zip(names, heros):
    my_dict[name] = hero
print(my_dict)

#Dictionary Comprehension

my_dict = {name: hero for name, hero in zip(names, heros)}
print(my_dict)

#If name not equal to Peter
my_dict = {names: heros for names, heros in zip(names, heros) if names != 'Peter'}
print(my_dict)

#Set Comprehension
nums = [1,1,2,1,32,435,43,4,4565,46,546]
my_set = set()
for n in nums:
    my_set.add(n)
print(my_set)

#Set Comprehension

my_set = {n for n in nums}
print(my_set)