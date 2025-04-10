basket={"orange", "apple", "mango", "apple", "orange"}
print(type(basket))
print(basket)

a = set()
a.add(1)
a.add(2)
print(a)
a.add(4)
print(a)

a={}
print(type(a))
a = {'something'}
print(type(a))
# print(a[0])

numbers = [1,2,3,4,2,3,4]
unique_numbers=set(numbers)
print(unique_numbers)

unique_numbers.add(55)
print(unique_numbers)

fs = frozenset(numbers)
print(fs)
# fs.add(5)

x = {"a", "b", "c"}
print("a" in x)

for i in x:
    print(i)

y = {"a", "g", "h"}
print(x)

print(y)

print(x|y)

print(x&y)