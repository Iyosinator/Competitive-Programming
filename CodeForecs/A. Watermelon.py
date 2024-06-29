# Link :- https://codeforces.com/problemset/problem/4/A
def can_divide_watermelon(w):
    if w % 2 == 0:
        return "YES"
    else:
        return "NO" 
# Read input
w = int(input())

# Print the result
print(can_divide_watermelon(w))

