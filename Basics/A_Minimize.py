t = int(input())

for i in range(t):
    a,b = map(int,input().split())
    
    print(max(a,b) - min(a,b))