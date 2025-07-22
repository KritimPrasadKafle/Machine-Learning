def star(n):
    start = 1
    for i in range(0, n):
        if i % 2 == 0: start = 0
        else: start = 1
        for j in range(0, i):
            print(start, end="")
            start = 1 - start
        print()

star(6)