import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__ + " took " + str((end-start)*1000) + "mil sec")
        return result
    return wrapper
@time_it
def calc_square(numbers):
    result = []
    for number in numbers:
        result.append(number*number)
    return result
@time_it
def calc_cube(numbers):

    result = []
    for number in numbers:
        result.append(number * number * number)
    return result

array = range(1,10000)
out_square= calc_square(array)
out_cube=calc_cube(array)



def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()