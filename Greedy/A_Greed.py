n = int(input())
volume = list(map(int,input().split()))
capacities = list(map(int,input().split()))


capacities.sort(reverse=True)

if capacities[0] + capacities[1] >= sum(volume):
    print('YES')
else:
    print('NO')