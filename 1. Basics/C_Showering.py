t = int(input())

for _ in range(t):
    n, s, m = map(int, input().split())
    
    # mark all minutes as free initially
    num = [i for i in range(1, m+1)]
    
    # remove all occupied minutes
    for _ in range(n):
        li, ri = map(int, input().split())
        for j in range(li, ri+1):
            if j in num:
                num.remove(j)
    
    # now num contains only free minutes
    counter = 1
    longest = 0
    for i in range(1, len(num)):
        if num[i] == num[i-1] + 1:   # consecutive free slots
            counter += 1
        else:
            longest = max(longest, counter)
            counter = 1
    longest = max(longest, counter)   # final check
    
    if longest >= s:
        print("YES")
    else:
        print("NO")
