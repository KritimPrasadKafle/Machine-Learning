if True:
    print("Conditional was True")

if False:
    print("Conditional was False")


language = ':Java'

if language == 'Python':
    print("Language is Python")
elif language == ':Java':
    print("Language is Java")
else:
    print("No match")


user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
    print('admin Page')
else:
    print('Bad Creds')
logged_in1 = False


if user == 'Admin' or logged_in1:
    print('admin Page')
else:
    print('Bad Creds')


if not logged_in:
    print('Please log in')
else:
    print('welcome')

a = [1,2,3,4]
b = [1,2,3]

print(a==b)

print(a is b)

print(id(a))
print(id(b))

print(a == b)
c = b
print(id(c))
print(c==b)

s = 0
if s:
    print("True")
else:
    print("False")

s = 1
if s:
    print("True")
else:
    print("False")

dict = {}
if dict:
    print("true")
else:
    print("false")