from itertools import combinations

n,k = map(int,input().split())


possible = []

for i in range(1,n):
    if n < k:
        print('NO')
        break
    elif i & (i-1) == 0:
        possible.append(i)

print(possible)
