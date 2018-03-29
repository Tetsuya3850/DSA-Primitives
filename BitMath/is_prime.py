# Check whether number is prime.

import math

def is_prime(n):
    if n == 2:
        return True
    elif n == 1 or n % 2 == 0:
        return False
    else:
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True

print (is_prime(43))
print (is_prime(42))
print (is_prime(41))
