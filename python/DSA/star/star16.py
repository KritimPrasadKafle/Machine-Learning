def star(n):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(0, n):
        # Print leading spaces for centering
        for j in range(0, n-i-1):
            print(" ", end="")
        
        # Print ascending letters (A to current letter)
        for j in range(0, i+1):
            print(alphabet[j], end="")
        
        # Print descending letters (current letter-1 back to A)
        for j in range(i-1, -1, -1):
            print(alphabet[j], end="")
        
        print()

star(7)