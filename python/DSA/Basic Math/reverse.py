def reverse(n):
    ans = 0
    while(n > 0):
        rem = n % 10
        ans = ans * 10 + rem
        n = n // 10
    return ans

s = reverse(9876)
print(s)