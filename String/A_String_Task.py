'''
1. if vowel delete it
2. inserts a character before consonant 
3. replace consonant with lowercase

'''

s = input().lower()

vowels = "aeiouy"
result = []

result = ''.join(['.' + c for c in s if c not in vowels])

print(result) 
