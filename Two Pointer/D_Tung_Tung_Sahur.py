# This program checks if a string 's' can be formed from a pattern 'p'.
# The formation rules are:
# 1. The characters in 's' must appear in the same relative order as in 'p'.
# 2. For each block of consecutive identical characters in 'p', there must be a
#    corresponding block of the same character in 's'.
# 3. The number of consecutive identical characters in 's' for any block
#    must be greater than or equal to the number of consecutive identical characters
#    in the corresponding block in 'p'.

t = int(input())

for _ in range(t):
    p = input()
    s = input()
    
    # Use two pointers, 'i' for pattern 'p' and 'j' for string 's'.
    i = 0
    j = 0
    
    n, m = len(p), len(s)
    valid = True
    
    while i < n and j < m:
        # If the characters at the current pointers don't match, it's an invalid formation.
        if p[i] != s[j]:
            valid = False
            break
        
        # Count consecutive identical characters in the current block of the pattern 'p'.
        p_count = 1
        while i + 1 < n and p[i+1] == p[i]:
            p_count += 1
            i += 1
        
        # Count consecutive identical characters in the corresponding block of the string 's'.
        s_count = 1
        while j + 1 < m and s[j+1] == s[j]:
            s_count += 1
            j += 1
            
        # The number of repetitions in 's' must be at least that in 'p'.
        if s_count < p_count:
            valid = False
            break
            
        # Move pointers to the start of the next distinct character blocks.
        i += 1
        j += 1
        
    # After the loop, both strings should be fully consumed.
    # If not, it means one string has leftover characters that don't match the other.
    if i < n or j < m:
        valid = False
    
    print("YES" if valid else "NO")
