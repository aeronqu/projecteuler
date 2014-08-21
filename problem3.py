from euler import isPrime
from math import sqrt

number = 600851475143
i = int(sqrt(number))

while i >= 2:
    if number % i == 0:
        if isPrime(i) == True:
            print i
            break
        else:
            i = i-1
    else:
        i = i -1


