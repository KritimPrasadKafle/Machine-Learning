def countdigits(n):
    ans = 0
    while(n > 0):
        rem = n % 10
        ans = ans + 1
        n = n // 10
    return ans


n = countdigits(3423)
print(n)


from math import log10
def count(m):
    cnt = int(log10(m) + 1)
    return cnt 
s = count(234)
print(s)

#Time complexity for this one is O(log10(N))

#If the problem is about the division TC would be in logarithmic.