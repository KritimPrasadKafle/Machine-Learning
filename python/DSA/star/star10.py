def star(n):
    s = "*"
    for i in range(0, n):
        for j in range(0, i):
            print(s, end = "")

        print()

def star2(n):
    s = "*"
    for i in range(0, n):
        for j in range(0, n - i):
            print(s, end="")
        print()

if __name__ == "__main__":
    star(6)

    star2(6)


