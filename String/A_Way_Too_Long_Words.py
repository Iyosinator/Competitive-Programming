t = int(input())

for i in range(t):
    word = input()

    if len(word) <= 10:
        print(word)

    first_letter = word[0]
    last_letter = word[-1]

    if len(word) > 10:
        print(first_letter + str(len(word) - 2) + last_letter)
