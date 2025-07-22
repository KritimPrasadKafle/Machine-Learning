def star(n):
    s = "*"
    for i in range(0, n):
        for j in range(0,i):
            print(" ", end = "")

        for j in range(0, 2*n - (2*i+1)):
            print(s, end = "")

        for j in range(0, i):
            print(" ", end = "")
        print()

if __name__ == "__main__":
    star(6)
