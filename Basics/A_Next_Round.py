n,k = map(int,input().split())
scores = list(map(int,input().split()))


ans = 0
x = scores[k-1]

for i in range(n):
    if scores[i]>= x and scores[i]>0:
        ans += 1

print(ans)



