def palindrome(n):
    original = n
    ans = 0
    while(n > 0):
        rem = n % 10
        ans = ans * 10 + rem
        n = n // 10
    print(ans)
    if ans == original:
        print(ans)
        return True
    else:
        return False

s = palindrome(787)
print(s)
