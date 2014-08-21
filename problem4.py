from euler import isPalindrome
output = 0
m = 0
n = 0
for i in range(999, 100, -1):
    for j in range(999, 100, -1):
        result = i * j
        if isPalindrome(result):
            if output < result:
                output = result
                m = i
                n =j
print output, m, n
