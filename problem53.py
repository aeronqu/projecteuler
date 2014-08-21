def combinate(n,r):
    x=1
    y=1
    z=1
    for i in range(1,n+1):
        x *= i
    for j in range(1,r+1):
        y *= j
    for h in range(1,n-r+1):
        z *= h
    return x/y/z

total = 0
for i in range(0,101):
    for j in range(i+1):
        if combinate(i,j)>10**6:
            total += i-j-j+1

print total



