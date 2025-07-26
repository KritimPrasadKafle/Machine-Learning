def armstrong(n):
    original  = n
    sum = 0
    while(n > 0):
        rem = n % 10
        sum = sum + (rem * rem * rem)
        n = n // 10
    print(sum)
    if original == sum:
        return True
    else: 
        return False

s = armstrong(153)
print(s)