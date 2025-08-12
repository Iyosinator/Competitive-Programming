t = int(input())  

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    min_val = arr[0]
    max_val = arr[-1]

    if (min_val + max_val) % 2 == 0:
        print(0)
        continue

    steps_from_left = n
    for i in range(n):
        if (arr[i] + max_val) % 2 == 0:
            steps_from_left = i
            break

    steps_from_right = n
    for j in range(n - 1, -1, -1):
        if (arr[j] + min_val) % 2 == 0:
            steps_from_right = n - 1 - j
            break

    print(min(steps_from_left, steps_from_right))
