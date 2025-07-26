def divisors(n):
    ans = []
    for i in range(1, n+1):
        if n % i == 0:
            ans.append(i)
    return ans

s = divisors(36)
print(s)

import math

def sqrtDivisors(n):
    ans = []
    for i in range(1, int(math.sqrt(n)) +1):
        if n % i == 0:
            ans.append(i)
            if n // i != i:
                ans.append(n // i)
    return sorted(ans)

s = sqrtDivisors(36)
print(s)

        