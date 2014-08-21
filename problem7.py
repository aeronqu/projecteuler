
from euler import isPrime


primes = [2]
i = 3
while True:
    if isPrime(i):
        primes.append(i)
        if len(primes) == 10001:
            break
    i += 2

print primes[10000]
