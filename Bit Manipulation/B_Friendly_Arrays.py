t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    xor_base = 0
    for num in a:
        xor_base ^= num

    or_mask = 0
    for num in b:
        or_mask |= num

    if n % 2 == 0:
        min_x = xor_base
        max_x = xor_base
    else:
        min_x = xor_base ^ or_mask
        max_x = xor_base

    print(min(min_x, max_x), max(min_x, max_x))
