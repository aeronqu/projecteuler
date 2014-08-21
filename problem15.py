x = []
matrix = [[x for i in range(21)] for j in range(21)]

for i in range(20):
    matrix[20][i] = 1
    matrix[i][20] = 1
matrix[20][20] = 0

for h in range(19,-1,-1):
    for v in range(19,-1,-1):
        matrix[h][v] = matrix[h+1][v]+matrix[h][v+1]

print matrix[0][0]


