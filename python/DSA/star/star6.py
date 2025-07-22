def star(n):
    for i in range(0, n):
        for j in range(0, n-i):
            print(j, end = " ")
        print()

if __name__ == "__main__":
    star(6)