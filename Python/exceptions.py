x = input("Enter number1: ")
y = input("Enter number2: ")
try:
    z = int(x) / int(y)
except ZeroDivisionError as e:
    print('Division by zero exception', type(e).__name__)
    z = None

print("Division is: ", z)