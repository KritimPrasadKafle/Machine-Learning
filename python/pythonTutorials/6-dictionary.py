student = {'name': 'John', 'age': 25, 'courses': ['Math', 'Computer Science']}



student['phone'] = '5555-55555'
student['name'] = 'Jane'
print(student['name']) 
#student['phone] returns an error as phone key is not there but student.get('phone') returns none
print(student.get('phone'))

student.update({'name': 'dsjkdsf', 'age': 12, 'phone': '234324'})
print(student)

age = student.pop('age')
print(student)
print(age)

print(student.keys())
print(student.values())

for key in student:
    print(key)

for key,value in student.items():
    print(key, value)