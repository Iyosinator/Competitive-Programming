t = int(input())
for _ in range(t):
    n = int(input())
    rows = [input().strip() for _ in range(n)]

    result = []
    for row in rows:
        result.append(row.index('#') + 1)

    print(*result[::-1])