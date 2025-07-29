def printOneToN(i,n):
    if i > n:
        return
    print(i)
    printOneToN(i+1,n)


if __name__ == "__main__":
    printOneToN(1,6)