def sumDivisibleBy(x,y):
    n = y / x
    return x*(n*(n+1)/2)

result = sumDivisibleBy(3,999) + sumDivisibleBy(5,999) - sumDivisibleBy(15,999)
print result
