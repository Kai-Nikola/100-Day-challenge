sentence = "This is a common interview question"


most_repeated_letter = {}
for (letter) in sentence:
    if letter in most_repeated_letter:
        most_repeated_letter[letter] += 1
    else:
        most_repeated_letter[letter] = 1

most_repeated_letter = sorted(most_repeated_letter.items(), key=lambda kv: kv[1], reverse=True)
print(most_repeated_letter[0])