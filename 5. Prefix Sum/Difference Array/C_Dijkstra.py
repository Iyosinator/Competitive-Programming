n=int(input())
a=list(map(int,input().split()))
S=sum(a)
m=0
count=0

if S%3!=0:
    print(0)
else:
    s=0
    for i in range(n-1):
        s+=a[i]

        if s==2*S//3:
            count+=m

        if s==S//3:
            m+=1
    print(count)