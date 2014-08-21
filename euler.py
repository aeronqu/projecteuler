from math import sqrt

def isPrime(n):
    if n <2:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2,int(sqrt(n))+1):
            if n % i == 0:
                return False
        return True

def isPalindrome(number1):
    number2 = int(str(number1)[::-1])
    if number2 == number1:
        return True
    else:
        return False


def isDivisible(x,n):
    for i in range(1,n+1):
        if x % i != 0:
            return False
    return True

print isDivisible(2520,10)







