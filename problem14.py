

def collatzSeq(n):
    yield n
    while 1:
        if n == 1:
            break
        elif n % 2 == 0:
            n = n/2
            yield n
        else:
            n = n*3 + 1
            yield n


def colatz():
    for i in range(1,1000000):
        yield sum(1 for value in collatzSeq(i))

number = 0
for value in colatz():
    if number < value:
        number = value
print number

