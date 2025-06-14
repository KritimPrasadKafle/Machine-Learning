#Tuples are immutable and list are mutable.
#Tuples are not changeable whereas the list are changeable.
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

tuple_1[0] = '__ART__'
print(tuple_1)
print(tuple_2)