from collections import deque, defaultdict

n = int(input())
managers = [int(input()) for _ in range(n)]

subordinates = defaultdict(list)
roots = []

for i in range(n):
    if managers[i] == -1:
        roots.append(i) 
    else:
        subordinates[managers[i]-1].append(i) 

max_level = 0
queue = deque()

for root in roots:
    queue.append((root, 1))  # (employee, level)

while queue:
    emp, level = queue.popleft()
    max_level = max(max_level, level)
    for sub in subordinates[emp]:
        queue.append((sub, level + 1))  # child level = parent level + 1

print(max_level)
