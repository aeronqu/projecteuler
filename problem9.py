

def pythagorean(n):

    "Generate a Pythagorean triplet so that a<b<c<n, and a**2 +b**2 = c**2"

    for i in range(1,n+1):
        for j in range(i+1,n+1):
            x = i**2 + j**2
            h = int(x**.5)
            if h**2 ==x  and h <= n:
                yield i,j,h

for a,b,c in pythagorean(1000):
    if a+b+c == 1000:
        print a*b*c
        break


