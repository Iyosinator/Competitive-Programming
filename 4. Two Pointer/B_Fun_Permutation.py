t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    print(' '.join(map(str,[n + 1 - x for x in p] )))