from collections import Counter

t = int(input())
target = [0, 1, 0, 3, 2, 0, 2, 5]
target_counter = Counter(target)

for _ in range(t):
    n = int(input())
    bag = list(map(int, input().split()))
    
    current_counter = Counter()
    steps = 0
    
    for num in bag:
        steps += 1
        if num in target_counter:
            current_counter[num] += 1
        
        match = all(current_counter[x] >= target_counter[x] for x in target_counter)
        if match:
            print(steps)
            break
    else:
        print(0)
