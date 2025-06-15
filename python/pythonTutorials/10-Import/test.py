import my_module
courses = ['History', 'Math', 'Physics', 'CompSci']

index = my_module.find_index(courses, 'Math')

print(index)

import random

random_choices = random.choice(courses)

print(random_choices)

import math

rads = math.radians(90)
# print(math.sins(rads))
print(rads)

import datetime

today = datetime.date.today()
print(today)

import os

print(os.getcwd())

print(os.__file__)