from euler import isDivisible
from euler import isPrime


i = 2520
while (not isDivisible(i, 20)):
    i = i + 20
print i
