def star(n):
    num = 1
    for i in range(1, n):
        for j in range(1, i):
            print(num, end = "")
            num = num+1
        print()

star(7)
