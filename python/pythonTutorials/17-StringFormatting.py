person = {'name': 'Jenn', 'age': 23}
sentence = 'My name is ' + person['name'] + ' and I am ' + str(person['age']) + ' years old.'
print(sentence)

sentence1 = 'My name is {} and I am {} years old.'.format(person['name'],person['age'])
print(sentence1)

sentence2 = 'My name is {0} and I am {1} years old.'.format(person['name'], person['age'])
print(sentence2)

sentence3 = 'My name is {0[name]} and I am {0[age]} years old.'.format(person)
print(sentence3)
person = {'name':'Jenn', 'age': 23}

sentence4 = 'My name is {name} and I am {age} years old.'.format(**person)
tag = 'h1'
text = 'This is a headline'
sentence = '<{0}>{1}</{0}>'.format(tag, text)
print(sentence)


#list

l = ['Jenn', 23]
sentence = 'My name is {0[0]} and I am {0[1]} years old.'.format(l)
print(sentence)


class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person('Jack', '33')
sentence = 'My name is {0.name} and I am {0.age} years old.'.format(p1)
print(sentence)

pi = 3.14159265
for i in range(1,11):
    sentence = 'The value is {:03}'.format(pi)
    print(sentence)

sentence = '1 MB is equal to {:,.2f} bytes'.format(1000**2)
print(sentence)

import datetime
my_date = datetime.datetime(2016,9,24,12,30,45)
print(my_date)