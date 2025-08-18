matrix = []

for i in range(5):
    row = list(map(int, input().split()))
    matrix.append(row)

pos = []
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == 1:
            pos = [i+1,j+1]

print(abs(3-pos[0]) + abs(3-pos[1]))