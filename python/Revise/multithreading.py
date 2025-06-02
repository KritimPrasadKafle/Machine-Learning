import time
import threading

square_result = []

def calc_square(numbers):
    print("calculate square numbers")
    for n in numbers:
        time.sleep(0.2)
        print('square: ' + str(n*n))
        square_result.append(n*n)

def calc_cube(numbers):
    print("Calculate cube of numbers")
    for n in numbers:
        time.sleep(0.2)
        print('cube: ', n*n*n)

arr = [2,3,8,9]

t = time.time()
# calc_cube(arr)
# calc_square(arr)

t1 = threading.Thread(target=calc_square, args=(arr, ))
t2 = threading.Thread(target=calc_cube, args=(arr, ))
t1.start()
t2.start()

t1.join()
t2.join()

print("done in :", time.time()-t)
print("Hah.. I am done with all my work now!")