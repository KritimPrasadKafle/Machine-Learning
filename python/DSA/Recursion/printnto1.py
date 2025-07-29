# def printNto1(i):
#     if i < 0:
#         return
#     print(i)
#     printNto1(i-1)

# # if __name__ == "__main__":
#     # printNto1(6)

# def printNto1InAnotherApproach(i,n):
#     if i < 0:
#         return
#     print(i)
#     printNto1InAnotherApproach(i-1, n)
# if __name__ == "__main__":
#     printNto1InAnotherApproach(6,6)

# def printForloop():
#     for i in range(6, 1, -1):
#         print(i)

# def printForloopIncluding1():
#     for i in range(6, 0, -1):
#         print(i)

# printForloop()

# printForloopIncluding1()


#Backtracking

# def print1toN(i,n):
#     if i < 0:
#         return 
# #     print1toN(i-1, n)
# #     print(i)

# # if __name__ == "__main__":
# #     print1toN(6,6)


def printNto1(i, n):
    if i > n:
        return 
    printNto1(i+1, n)
    print(i)

if __name__ == "__main__":
    printNto1(1, 6)