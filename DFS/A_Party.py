import sys
sys.setrecursionlimit(3000)
input = sys.stdin.readline

n = int(input())
p = [int(input()) for _ in range(n)]

from collections import defaultdict

tree = defaultdict(list)
roots = []


for i in range(n):
    if p[i] == -1:
        roots.append(i + 1)
    else:
        tree[p[i]].append(i + 1)
print(tree)
def dfs(u):
    depth = 1
    for v in tree[u]:
        depth = max(depth, 1 + dfs(v))
    return depth

ans = 0
for root in roots:
    ans = max(ans, dfs(root))

print(ans)
