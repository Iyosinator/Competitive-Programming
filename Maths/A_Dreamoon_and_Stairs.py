'''

10 2  2 4 6 8 10 - 5 step  
10 3  3 6 9 5/3 == 1.5 
10 4   4 8 
10 5   5 10

29//2 

'''

n,m = map(int,input().split())

x = (n+1)//2

for k in range(x,n+1):
    if k%m == 0:
        print(k)
        break
else:
    print(-1)