
f = reduce(lambda x,y:x*y, range(1,101))
def digitSum(n):
    s = 0
    while n > 0:
        s = s + (n % 10)
        n = n / 10
    return s

print digitSum(f)


