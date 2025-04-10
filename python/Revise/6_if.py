n = input("Enter a number: ")
n = int(n)
if n%2 == 0:
    print("Number is even")
else:
    print("Number is odd")

nepali = ["Momo", "Chowmein", "Dal", "Dhat"]
pakistani=["nihari","paya","karahi"]
bangladesi=["panta bhat","chorchori","fuchka"]

dish = input("Enter a dish: ")

if dish in nepali:
    print(f'The {dish} is of nepal.')
elif dish in pakistani:
    print(f'The {dish} is of pakistan.')
elif dish in bangladesi:
    print(f'The {dish} is of Bangladesh.')
else:
    print(f'The {dish} is of different country.')

#Ternary Operator
print("Ternary operator demo:")
n = input("Enter a number: ")
n = int(n)
message = "Number is even" if n%2 == 0 else "Number is odd"
print(message)