t = int(input())
for _ in range(t):
    n = int(input())
    r = list(map(int, input().split()))
    ok = True
    a = []
    next_number = 1
    used = set()

    for i in range(n):
        if i == 0 or r[i] > r[i-1]:
            # need a new number
            while next_number in used:
                next_number += 1
            if next_number > n:
                next_number = 1  # wrap around, can reuse numbers
            a.append(next_number)
            used.add(next_number)
        else:
            # repeat any number, can pick last number
            a.append(a[-1])
        
        if r[i] < i + 1:
            ok = False
            break

    if ok:
        print("Yes")
        print(*a)
    else:
        print("No")
