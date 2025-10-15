t = int(input())

for i in range(t):
    input()
    grid = [input() for i in range(8)]
    red_last = any(row == 'RRRRRRRR' for row in grid)
    

    if red_last:
        print('R')
    else:
        for col in range(8):
            if all(grid[row][col] == 'B' for row in range(8)):
                print('B')
                break
