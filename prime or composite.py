import math


def isPrime(n):
    sqrtn = int(math.sqrt(n))
    prime = True

    for divisor in range(2, sqrtn + 1):
        if n % divisor == 0:
            prime = False
            break
    return prime


n = int(input("enter a num: "))
if n > 2:
    if isPrime(n):
        print(n, "is a prime num")
    else:
        print(n, "is not a prime num,(Composite number)")
else:
    print(n, " is neither a prime nor composite")
