t = int(input())

for i in range(t):
    grid = []
    for j in range(3):
        line = input().strip()  
        grid.append(line)

    m = len(grid)
    n = len(grid[0])
    count = 0

    for i in range(m):
        for j in range(n):
            if grid[i][j] == "?":
                #print(grid[i])
                if 'A' in grid[i] and 'B' in grid[i]:
                    print('C')
                    break
                if 'A' in grid[i] and 'C' in grid[i]:
                    print('B')
                    break
                if 'C' in grid[i] and 'B' in grid[i]:
                    print('A')
                    break
                                
    