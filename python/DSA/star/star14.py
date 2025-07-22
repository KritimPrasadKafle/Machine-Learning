def star(n):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(0,n):
        for j in range(0, i+1):
            print(alphabet[j], end="")
        print()

star(6)

def star1(n):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(0, n):
        for j in range(0, n-i):
            print(alphabet[j], end = "")
        print()
star1(6)