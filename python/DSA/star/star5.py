def star(n):
    star2 = "*"
    for i in range(0, n):
        for j in range(0, n-i):
            print(star2, end = " ")
        print()

if __name__ == "__main__":
    star(6)
