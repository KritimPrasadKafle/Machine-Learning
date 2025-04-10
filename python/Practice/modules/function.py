tom_exp_list = [2100,3400,3500]
joe_exp_list = [200,500,700]

# total = 0
# for item in tom_exp_list:
#     total = total+item
# print("Tom's total expenses: ", total)
#
# for item in joe_exp_list:
#     total = total + item
# print("Joe's total expenses: ", total)

def total(array, name):
    total = 0
    for i in array:
        total = total + i
    print(f"Total amount of {name} is: {total}")

total(tom_exp_list, "Tom")
total(joe_exp_list, "Joe")


def calculate_triangle_area(base, height):
    return 1/2*(base*height)

def calculate_square_area(length):
    return length * length;


import math
math.pow(2,3);