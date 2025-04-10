n1 = input("Enter first number: ")
n2 = input("Enter second number: ")
sum = float(n1) + float(n2)
print("Sum is:", sum)

# Write a program that can find area of a triangle.
# It should take base and height as an input from user
# and using that it should print an area of a triangle

length = float(input("Enter length: "))
height = float(input("Enter height: "))
area = (1/2)*length*height
print("The area is: ", area)


# Write a program that takes file name with extension as
# an input and prints just the file name without extension
# (you can assume that file extensions are always 3 character long)

s = input("Enter filename: ")
file_name_only = s[:-4]

print(file_name_only)

