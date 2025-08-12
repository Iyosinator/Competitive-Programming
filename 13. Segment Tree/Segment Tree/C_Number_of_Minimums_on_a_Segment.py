n, m = map(int, input().split())
arr = list(map(int, input().split()))

tree = [(float('inf'), 0)] * (4 * n)

for i in range(n):
    tree[n + i] = (arr[i], 1)

for i in range(n - 1, 0, -1):
    left = tree[2 * i]
    right = tree[2 * i + 1]
    
    if left[0] < right[0]:
        tree[i] = left
    elif left[0] > right[0]:
        tree[i] = right
    else:
        tree[i] = (left[0], left[1] + right[1])

def update(idx, value):
    idx += n
    tree[idx] = (value, 1)
    while idx > 1:
        idx //= 2
        left = tree[2 * idx]
        right = tree[2 * idx + 1]
        
        if left[0] < right[0]:
            tree[idx] = left
        elif left[0] > right[0]:
            tree[idx] = right
        else:
            tree[idx] = (left[0], left[1] + right[1])

def query(l, r):
    l += n
    r += n
    min_value = float('inf')
    count = 0
    
    while l < r:
        if l % 2 == 1:
            if tree[l][0] < min_value:
                min_value = tree[l][0]
                count = tree[l][1]
            elif tree[l][0] == min_value:
                count += tree[l][1]
            l += 1
        
        if r % 2 == 1:
            r -= 1
            if tree[r][0] < min_value:
                min_value = tree[r][0]
                count = tree[r][1]
            elif tree[r][0] == min_value:
                count += tree[r][1]
        
        l //= 2
        r //= 2
    
    return min_value,count

for _ in range(m):
    operation = list(map(int, input().split()))
    if operation[0] == 1:
        i, v = operation[1], operation[2]
        update(i, v)
    elif operation[0] == 2:
        l, r = operation[1], operation[2]
        result = query(l, r)
        print(result[0],result[1])
