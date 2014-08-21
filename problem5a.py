
from euler import isPrime

def highestExp(x,n):
    result = x
    count = 0
    while result <= n:
        count += 1
        result *= x
    return count

output = 1
for i in range(2,20):
    if isPrime(i):
        exponent= highestExp(i,20)
        output *= i**exponent

print output



