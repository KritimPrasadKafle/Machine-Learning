def forLoopName(i,n):
    for i in range(i, n+1):
        print("Kritim - printNames.py:3")
def printNames(i, n):
    if i > n:
        return
    print("Kritim - printNames.py:7")
    printNames(i+1, n)

if __name__ == "__main__":
    printNames(0,4)
    forLoopName(1, 5)
