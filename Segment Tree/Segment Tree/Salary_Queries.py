from bisect import bisect_left, bisect_right

n, q = map(int, input().split())  # Read n (number of employees) and q (number of queries)
arr = list(map(int, input().split()))  # Read the salaries of employees

tree = [[] for _ in range(4 * n)]  # Segment tree initialized with empty lists

# Build the segment tree
def build():
    for i in range(n):
        tree[n + i] = [arr[i]]  # Each leaf node is a list containing one salary
    for i in range(n - 1, 0, -1):
        tree[i] = sorted(tree[2 * i] + tree[2 * i + 1])  # Merge and sort the left and right children

# Update the tree after a change in salary
def update(i, old_value, new_value):
    i += n
    tree[i].remove(old_value)  # Remove the old salary
    tree[i].append(new_value)  # Add the new salary
    tree[i].sort()  # Re-sort the list after the update
    while i > 1:
        i //= 2
        tree[i] = sorted(tree[2 * i] + tree[2 * i + 1])  # Recalculate and merge the children

# Query the number of employees whose salary is between l and r (inclusive)
def query(l, r):
    l += n
    r += n
    count = 0
    while l < r:
        if l % 2 == 1:
            # Count the salaries in the range [l, r]
            count += bisect_right(tree[l], r) - bisect_left(tree[l], l)
            l += 1
        if r % 2 == 1:
            r -= 1
            count += bisect_right(tree[r], r) - bisect_left(tree[r], l)
        l //= 2
        r //= 2
    return count

# Build the segment tree
build()

# Process each query
for _ in range(q):
    op, a, b = input().split()  # Read operation (either '!' or '?') and its arguments
    a, b = int(a), int(b)
    
    if op == "!":
        i, v = a - 1, b  # Convert to 0-based index for the update
        old_salary = arr[i]
        arr[i] = v
        update(i, old_salary, v)  # Update the tree with the new salary
    elif op == "?":
        x, y = a, b  # Query the range [x, y]
        print(query(x, y))  # Print the result of the query
