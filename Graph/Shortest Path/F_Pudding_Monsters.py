import sys
input = sys.stdin.readline
sys.setrecursionlimit(1 << 25)

def read_ints():
    return list(map(int, sys.stdin.readline().strip().split()))

def solve():
    n = int(input())
    pos = [tuple(read_ints()) for _ in range(n)]

    perm = [-1] * n
    for x, y in pos:
        perm[x - 1] = y - 1

    inc_stack = [-1]
    dec_stack = [-1]

    tree_min = {}
    tree_lazy = {}
    tree_cnt = {}

    def get_min(v): return tree_min.get(v, 0) + tree_lazy.get(v, 0)
    def get_cnt(v): return tree_cnt.get(v, 1)

    def build(v, l, r):
        tree_min[v] = l
        tree_lazy[v] = 0
        tree_cnt[v] = 1
        if l == r:
            return
        m = (l + r) // 2
        build(v * 2, l, m)
        build(v * 2 + 1, m + 1, r)

    def push(v):
        if tree_lazy.get(v, 0):
            tree_lazy[v * 2] = tree_lazy.get(v * 2, 0) + tree_lazy[v]
            tree_lazy[v * 2 + 1] = tree_lazy.get(v * 2 + 1, 0) + tree_lazy[v]
            tree_lazy[v] = 0

    def pull(v):
        a = get_min(v * 2)
        b = get_min(v * 2 + 1)
        tree_min[v] = min(a, b)
        tree_cnt[v] = 0
        if a == tree_min[v]: tree_cnt[v] += get_cnt(v * 2)
        if b == tree_min[v]: tree_cnt[v] += get_cnt(v * 2 + 1)

    def modify(v, l, r, ql, qr, val):
        if ql > r or qr < l:
            return
        if ql <= l and r <= qr:
            tree_lazy[v] = tree_lazy.get(v, 0) + val
            return
        push(v)
        m = (l + r) // 2
        modify(v * 2, l, m, ql, qr, val)
        modify(v * 2 + 1, m + 1, r, ql, qr, val)
        pull(v)

    build(1, 0, n - 1)

    ans = 0

    for i in range(n):
        while len(inc_stack) >= 2 and perm[i] < perm[inc_stack[-1]]:
            modify(1, 0, n - 1, inc_stack[-2] + 1, inc_stack[-1], perm[inc_stack[-1]])
            inc_stack.pop()
        while len(dec_stack) >= 2 and perm[i] > perm[dec_stack[-1]]:
            modify(1, 0, n - 1, dec_stack[-2] + 1, dec_stack[-1], -perm[dec_stack[-1]])
            dec_stack.pop()

        inc_stack.append(i)
        dec_stack.append(i)

        modify(1, 0, n - 1, inc_stack[-2] + 1, inc_stack[-1], -perm[inc_stack[-1]])
        modify(1, 0, n - 1, dec_stack[-2] + 1, dec_stack[-1], perm[dec_stack[-1]])

        ans += tree_cnt[1]

    print(ans)

solve()
