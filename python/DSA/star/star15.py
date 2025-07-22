def star(n):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for i in range(0, n):
        for j in range(0, i+1):
            print(alphabet[i], end="")
        print()

star(6)