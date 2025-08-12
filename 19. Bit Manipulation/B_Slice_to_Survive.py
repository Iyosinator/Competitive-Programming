t = int(input())
for _ in range(t):
    rows, cols, start_row, start_col = map(int, input().split())

    dist_row = min(start_row, rows - start_row + 1)
    dist_col = min(start_col, cols - start_col + 1)

    def bit_length_minus_one(x):
        return 0 if x <= 1 else (x - 1).bit_length()

    cuts_horizontal = 1 + bit_length_minus_one(cols) + bit_length_minus_one(dist_row)
    cuts_vertical = 1 + bit_length_minus_one(rows) + bit_length_minus_one(dist_col)

    print(min(cuts_horizontal, cuts_vertical))
