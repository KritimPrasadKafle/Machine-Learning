rent = 8000
petrol = 500.5
groceries = 2050.5

print(rent)
total = rent+petrol+groceries
print(rent)

a = "Rajesh"
b = "Nikhil"
c = "Shree Krishna"

print("Actors in Nepali movies", a, b, c)

print(type(rent))
print(type(a))


learn_python = True
learn_fortran = False

print(type(learn_python))

foo = 5
foo = "Hello"
bar = foo
print("bar id", id(bar))
print("foo id", id(foo))

#Exercise
# 1. Create a variable called break and assign
# it a value 5. See what happens and find out the reason
# behind the behavior that you see
# break = 5


# 2. Create two variables. One to store your birth year and
# another one to store current year. Now calculate your age
# using these two variables

birth_date = 2001
new_Date = 2025
result = new_Date - birth_date
print("Result", result)

# 3. Store your first, middle and last name in three different
# variables and then print your full name using these variables
first_name = "Kritim"
middle_name = "Prasad"
last_name = "Kafle"

name = first_name + " " + middle_name + " " + last_name
print(f"My full name is {name}.")


# 4. Answer which of these are invalid variable names: "__nation,
# 1record, record1, record_one, record-one, record^one, continue"
# _nation = 2
# 1record = 4
# record1 = 5
# record_one = 6
# record-one = 7
# record^one = 8
# continue = 9