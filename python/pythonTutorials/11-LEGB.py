'''
LEGB
Local, Enclosing, Global, Built-in
'''

x = 'global x'

def test():
    y = 'local y'
    print(y)
    print(x)

test()

# print(y) # y is local variable


def test1():
    x = 'local y'
    # print(y)
    print(x)

test1()


def test2():
    global x
    x = 'local x'
    print(x)

test2()
print(x)

def test3(z):
    x = 'local x'
    print(z)
test3('local z')

print(x)

import builtins
print(dir(builtins))
m = min([5,1,4,2,3])
print(m)

def min():
    pass


def outer():
    x = 'outer x'

    def inner():
        x = 'inner x'
        print(x)
    
    inner()
    print(x)

outer()


def hello(*args, **kwargs):
    print(args, kwargs)

hello('dfsjkfsd', 'dfsjkjsdf', 'dsfjjdsf', {'dsfj': 'dksdlfk'})

