indian = ["somasa", "daal", "naan"]
chinese = ["egg role", "pot sticker", "fried rice"]
italian = ["pizza", "pasta", "risotto"]
cusine = input("Enter the cuisine name: ")

if cusine in indian:
    print("It's a indian dish", cusine)
elif cusine in chinese:
    print("It's a chinese dish", cusine)
elif cusine in italian:
    print("It's a italian dish", cusine)
else:
    print("Based on little knowledge I dont have which dish you are trying to search for.")