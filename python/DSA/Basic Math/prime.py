def prime(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count = count + 1
    if count == 2:
        return True
    else:
        return False
s = prime(13)
print(s)
        
import math        
def sqrtPrime(n):
    count = 0
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            count = count + 1
            if n // i != i:
                count = count + 1

    if count == 2:
        return True
    else:
        return False
    
s = sqrtPrime(13)
print(s)
        