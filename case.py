"""Case-study #4 Text analysis
Developer:
Balabanov M.A.

"""


text = input()

count_sentences = text.count('.')
count_words = len(text.split())
count_syllables = 0
for i in text:
    letter = i.lower()
    if letter == "а" or letter == "о" or letter == "и" or letter == "е" or letter == "ё" or letter == "э" or \
            letter == "ы" or letter == "у" or letter == "ю" or letter == "я":
        count_syllables += 1
ASL = count_words / count_sentences
ASW = count_syllables / count_words
FRE = 206.835 - (1.3 * ASL) - (60.1 * ASW)

print(count_sentences)
print(count_words)
print(count_syllables)
print(ASL)
print(ASW)
print(FRE)
