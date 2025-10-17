n, m = map(int, input().split())
arr = list(map(int, input().split()))

tree = [float('inf')] * (4 * n)

for i in range(n):
    tree[n + i] = arr[i]

for i in range(n - 1, 0, -1):
    tree[i] = min(tree[2 * i] , tree[2 * i + 1])

#print(tree)

def update(idx, value):
    idx += n
    tree[idx] = value
    while idx > 1:
        idx //= 2
        tree[idx] = min(tree[2 * idx],tree[2 * idx + 1])

def query(l, r):
    l += n
    r += n
    min_value =  float('inf')
    while l < r:
        if l % 2 == 1:
            min_value = min(min_value,tree[l])
            l += 1
        if r % 2 == 1:
            r -= 1
            min_value = min(min_value,tree[r])
        l //= 2
        r //= 2
    return min_value

for _ in range(m):
    operation = list(map(int, input().split()))
    if operation[0] == 1:
        i, v = operation[1], operation[2]
        update(i, v)
    elif operation[0] == 2:
        l, r = operation[1], operation[2]
        result = query(l, r)
        print(result)
