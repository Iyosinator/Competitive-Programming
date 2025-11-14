k,n,w = map(int,input().split())


total = int(w/2 * (2*k + (w-1)*k)) 

if n > total:
    print(0)
else:
    print(total -n)