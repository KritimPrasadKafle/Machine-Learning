def star(n):
    star1 = "*"
    for i in range(0, n):
        for j in range(0,i):
            print(star1, end = " ")
        print()

if __name__ == "__main__":
    star(5)