
def solve(a):
    xor_result = 0
    for num in a:
        xor_result ^= num

    if xor_result == 0:
        return 0

    for i in range(1, 32):
        result = 0
        for j in range(len(a)):
            result ^= (a[j] ^ i)
        if result == 0:
            return i

    return -1


