from itertools import count

def triNumber(n):
    return n*(n+1)/2

def triGenerator():
    for n in count(1):
        yield triNumber(n)

def primeFactor(n):
    p = 2

    while p*p <= n:
        if isPrime(p):
            while not n % p:
                yield p
                n //= p
        p += 1
    if n >1:
        yield n
def product(n):
    return reduce(lambda x,y: x*y, n, 1)

for number in triGenerator():
    if product(each + 1 for each in primeFactor(number).values()) >500:
        print number
        break

