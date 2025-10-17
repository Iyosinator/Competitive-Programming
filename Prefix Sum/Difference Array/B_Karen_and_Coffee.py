import sys
input = sys.stdin.readline

n, k, q = map(int, input().split())

MAX_TEMP = 200000

diff = [0] * (MAX_TEMP + 2)

for _ in range(n):
    l, r = map(int, input().split())
    diff[l] += 1
    diff[r + 1] -= 1


freq = [0] * (MAX_TEMP + 1)
running = 0
for i in range(1, MAX_TEMP + 1):
    running += diff[i]
    freq[i] = running

admissible = [0] * (MAX_TEMP + 1)
for i in range(1, MAX_TEMP + 1):
    admissible[i] = 1 if freq[i] >= k else 0

prefix_admissible = [0] * (MAX_TEMP + 1)
for i in range(1, MAX_TEMP + 1):
    prefix_admissible[i] = prefix_admissible[i - 1] + admissible[i]

for _ in range(q):
    a, b = map(int, input().split())
    ans = prefix_admissible[b] - prefix_admissible[a - 1]
    print(ans)
