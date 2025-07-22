def star(n):
    for i in range(0, n):
        # numbers (ascending)
        for j in range(0, i):
            print(j, end="")
        # space
        for j in range(0, 2*(n-i)):
            print(" ", end="")
        # numbers (descending)  
        for j in range(i-1, -1, -1):
            print(j, end="")
        print()

star(6)