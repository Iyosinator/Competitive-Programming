n,k = map(int,input().split())

i = 0


while i < k:
    if str(n)[-1] == "0":
        n//= 10
    else:
        n-=1
    i+= 1

print(n)