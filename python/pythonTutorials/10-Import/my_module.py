print('Imported my_module....')

test = 'Test String'

def find_index(to_search, target):
    for i, value in enumerate(to_search):
        if value == target:
            return i
        
    return  -1

s = find_index([1,2,34,5,6,],6)
print(s)

