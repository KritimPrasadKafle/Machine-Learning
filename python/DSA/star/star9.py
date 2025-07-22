def star(n):
    star1 = "*"
    for i in range(0, n):
        for j in range(0, n-i-1):
            print(" ", end = "")
        for j in range(0, 2*i+1):
            print(star1, end = "")
        for j in range(0, n-i+1):
            print(" ", end = "")
        print()



def star1(n):
    star2 = "*"
    for i in range(0, n):
        for j in range(0, i):
            print(" ", end="")
        for j in range(0, 2*n- (2*i+1)):
            print(star2, end="")
        for j in range(0, i):
            print(" ", end="")

        print()
if __name__ == "__main__":
    star(6)
    star1(6)