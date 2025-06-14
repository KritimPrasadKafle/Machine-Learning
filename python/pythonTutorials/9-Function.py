def hello():
    pass
print(hello)

def hello_fun():
    print('Hello World')

hello_fun()


print('Hello World')

print('Hello World')
print('Hello World')
print('Hello World')
print('Hello World')

def hello():
    for i in range(4):
        print('Hello')
    
hello()

hello_fun()

hello_fun()
hello_fun()
hello_fun()
hello_fun()

def hey():
    return 'Hello'

print(hey().upper())

print(len('Hellllo'))

def greeting(hello,name):
    return '{} {} Function.'.format(hello, name)

s = greeting('Hi','Kritim')
print(s)

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

student_info('Math', 'Art', name= 'John', age = 22)

courses = ('Math', 'Art')
info = {'name': 'John', 'age': 22}
student_info(*courses, **info)


month_days = [0,31,28,31,30,31,30,31,31,30,31,30,31]

def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    if not 1 <= month <= 12:
        return 'Invalid Month'
    if month == 2 and is_leap(year):
        return 29
    return month_days(month)
print(is_leap(2020))