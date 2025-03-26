book = {}

book['tom'] = {
    'name': 'tom',
    'address': '1 red street, NY',
    'phone': 98989898
}

book['bob'] = {
    'name': 'bob',
    'address': '1 green street NY',
    'phone': 234567
}

import json
s = json.dumps((book))
# print(s)
with open("D:\hustle\Python\Practice\ook.txt", "w") as f:
    f.write(s)

f = open("D:\hustle\Python\Practice\ook.txt", "r")
s = f.read()
print(s)

import json
bookk = json.loads(s)
print(bookk)

type(bookk)