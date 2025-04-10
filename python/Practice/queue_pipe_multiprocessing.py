import multiprocessing

result = []

def calc_square(numbers):
    global result
    for n in numbers:
        result.append(n*n)
    print('inside process ' + str(result))

if __name__ == "__main__":
    numbers = [2,3,5]
    result = multiprocessing.Array('i', 3)
    p = multiprocessing.Process(target=calc_square, args=(numbers, result))

    p.start()
    p.join()

