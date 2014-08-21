
allSeq = [0] *1000000
allSeq[1] = 1
maxN = 0

for i in range(2, 1000000):
    number = i;
    k = 0;
    while number >= i:
        k += 1
        if number % 2 == 0:
            number = number / 2
        else:
            number = number * 3 + 1

    allSeq[i]=k + allSeq[number]

print allSeq.index(max(allSeq))
