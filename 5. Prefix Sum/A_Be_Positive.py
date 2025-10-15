t = int(input())

for i in range(t):
    n = int(input())
    nums = list(map(int,input().split()))

    count_zero = 0
    count_minusone = 0


    for n in nums:
        if n == 0:
            count_zero += 1
        if n == -1:
            count_minusone += 1
    
    if count_minusone % 2 != 0:
        print(count_zero + 2 )
    else:
        print ( count_zero)