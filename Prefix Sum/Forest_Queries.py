n, q = map(int, input().split())
forest = [input().strip() for _ in range(n)]
queries = [tuple(map(int, input().split())) for _ in range(q)]

prefix = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        current_cell_tree = 1 if forest[i - 1][j - 1] == '*' else 0
        top_prefix = prefix[i - 1][j]
        left_prefix = prefix[i][j - 1] 
        overlap_prefix = prefix[i - 1][j - 1]

        prefix[i][j] = (current_cell_tree + top_prefix + left_prefix - overlap_prefix)

for query in queries:
    y1, x1, y2, x2 = query

    total_area = prefix[y2][x2]
    top_strip = prefix[y1 - 1][x2]
    left_strip = prefix[y2][x1 - 1]
    overlap_corner = prefix[y1 - 1][x1 - 1]

    trees = (total_area - top_strip - left_strip + overlap_corner)
    print(trees)
    
