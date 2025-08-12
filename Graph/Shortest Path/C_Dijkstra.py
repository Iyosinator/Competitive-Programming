import sys
from heapq import heappop, heappush

def read_ints():
    return list(map(int, sys.stdin.readline().split()))

def dijkstra(n, graph, start):
    dist = [float('inf')] * (n + 1)
    parent = [-1] * (n + 1)
    dist[start] = 0
    heap = [(0, start)]

    while heap:
        d, u = heappop(heap)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            nd = d + w
            if dist[v] > nd:
                dist[v] = nd
                parent[v] = u
                heappush(heap, (nd, v))
    return dist, parent

def solve():
    n, m = read_ints()
    graph = [[] for _ in range(n + 1)]
    edges = {}
    for _ in range(m):
        a, b, c = read_ints()
        if a > b:
            a, b = b, a
        if (a, b) not in edges or c < edges[(a, b)]:
            edges[(a, b)] = c

    for (a, b), c in edges.items():
        graph[a].append((b, c))
        graph[b].append((a, c))

    dist, parent = dijkstra(n, graph, 1)

    if dist[n] == float('inf'):
        print(-1)
        return

    path = []
    cur = n
    while cur != -1:
        path.append(cur)
        cur = parent[cur]

    print(*path[::-1])

solve()
