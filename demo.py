X = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]

Y = [[5, 8, 1],
     [6, 7, 3],
     [4, 5, 9]]

result = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]

for x in range(0, len(X)):
    for y in range(0, len(X[0])):
        result[x][y] = X[x][y]+Y[x][y]
for z in result:
    print(z)
