t = int(input())

for _ in range(t):
    num_elements = int(input())
    array = [0] + list(map(int, input().split()))
    group_tags = input()
    num_queries = int(input())

    group_1_xor = 0
    group_0_xor = 0

    for i in range(num_elements):
        if group_tags[i] == '1':
            group_1_xor ^= array[i + 1]
        else:
            group_0_xor ^= array[i + 1]

    for i in range(1, num_elements + 1):
        array[i] ^= array[i - 1]

    result = []

    for _ in range(num_queries):
        query = list(map(int, input().split()))

        if query[0] == 1:
            left = query[1]
            right = query[2]
            xor_value = array[right] ^ array[left - 1]
            group_1_xor ^= xor_value
            group_0_xor ^= xor_value

        elif query[0] == 2:
            group_type = query[1]
            if group_type == 1:
                result.append(group_1_xor)
            else:
                result.append(group_0_xor)

    print(*result)
