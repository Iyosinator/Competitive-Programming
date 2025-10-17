t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if n == 1:
        print(a[0])
        continue

    m_score = a[-1]
    s_score = 0

    for i in range(n-1):        
        if a[i] > b[i + 1]:
            m_score += a[i]
            s_score += b[i + 1]

    print(m_score - s_score)
