n,m,k = map(int,input().split())


armies = [int(input()) for i in range(m+1)]
fedor = armies[-1]
count = 0
for i in range(m):
    diff = bin(armies[i] ^ fedor).count('1')
    if diff <= k:
        count += 1

print(count)
    


