t = int(input())

for i in range(t):
    n,a,b = map(int,input().split())


    if n%2 == 0:
        print(min(n*a, (n//2*b)))
    else:
        print(min(n*a,(n//2*b + a)))



1 - 1
2 - 1 1
3 - 2 1
4 - 2 2 