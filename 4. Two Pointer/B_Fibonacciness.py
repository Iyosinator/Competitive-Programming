t = int(input())


for i in range(t):
    a1,a2,a4,a5 = map(int,input().split())

    a31 = a1 + a2
    a32 = a4 - a2
    a33 = a5 -a4

    candidates = [a31,a32,a33]
    
    max_fibo = 0

    for a3 in candidates:
        count = 0
        arr = [a1,a2,a3,a4,a5]
        if arr[0] + arr[1] == arr[2]:
            count += 1
        if arr[1] + arr[2] == arr[3]:
            count += 1
        if arr[2] + arr[3] == arr[4]:
            count += 1

        max_fibo = max(max_fibo, count)
    print(max_fibo)
