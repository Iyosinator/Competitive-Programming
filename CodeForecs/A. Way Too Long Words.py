#Link:- https://codeforces.com/problemset/problem/71/A
def abbreviate_word(word):
    if len(word) > 10:
        return (word[0] + str((len(word)-2)) + word[-1])
    else:
        return word

n = int(input())

for i in range(n):
    word = input()
    print(abbreviate_word(word))
