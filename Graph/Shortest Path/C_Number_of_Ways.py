'''

Array: [0, 1, -1, 0, 1, -1, 0]

Total Sum = 0
Target = 0/3

Running Sum = 0 1 0 0 1 0 0 

1,3,4,6

Running Suffix Sum =  0 -1 0 0 -1 0 0
counter sum == target 1  0 1 1  0 1 1
reverse it  = 1 1 0 1 1 0 1 

1,2,4,5,7

counter sum == target 1  0 1 1  0 1 1
sums[i] = [1,1,2,3,3,4,5]

total_ways += sums[i+2]


'''
import sys

def read_ints():
    return list(map(int, sys.stdin.readline().strip().split()))

def count_three_equal_parts(a):
    n = len(a)
    total = sum(a)

    if total % 3 != 0:
        return 0

    target = total // 3

    cnt = [0] * n
    suffix_sum = 0

    for i in range(n - 1, -1, -1):
        suffix_sum += a[i]
        if suffix_sum == target:
            cnt[i] = 1

    sums = [0] * n
    sums[-1] = cnt[-1]
    for i in range(n - 2, -1, -1):
        sums[i] = sums[i + 1] + cnt[i]

    prefix_sum = 0
    answer = 0
    for i in range(n - 2):  # leave space for second and third part
        prefix_sum += a[i]
        if prefix_sum == target:
            answer += sums[i + 2]

    return answer

n = int(sys.stdin.readline())
a = read_ints()

print(count_three_equal_parts(a))
