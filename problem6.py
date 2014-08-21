
sum1 = 0
sum2 = 0

def sumOfSqure(n):
    global sum1
    for i in range(1,n+1):
         sum1 += i**2
    return sum1

def squreOfSum(n):
    global sum2
    for i in range(1,n+1):
        sum2 += i
    return sum2 ** 2

x = sumOfSqure(100)
y = squreOfSum(100)
print y-x

