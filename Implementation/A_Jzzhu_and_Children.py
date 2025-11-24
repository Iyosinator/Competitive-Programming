from collections import deque

n, m = map(int, input().split())
a = list(map(int, input().split()))

queue = deque([(i+1, a[i]) for i in range(n)])
last_child = -1

while queue:
    child, need = queue.popleft()      
    need -= m                          
    if need > 0:
        queue.append((child, need))   
    else:
        last_child = child             

print(last_child)
