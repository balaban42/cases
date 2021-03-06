"""Case-study #4 Text analysis
Developer:
Balabanov M.A.

"""
import ru_local

text = input('{}'.format(ru_local.WRITE))

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

print('{}'.format(ru_local.SENTENCES), count_sentences)
print('{}'.format(ru_local.WORDS), count_words)
print('{}'.format(ru_local.SYLLABLES), count_syllables)
print(ASL)
print(ASW)
print(FRE)
if FRE >= 81:
    print('{}'.format(ru_local.TYPE1))

elif 80 >= FRE >= 51:
    print('{}'.format(ru_local.TYPE2))

elif 50 >= FRE >= 26:
    print('{}'.format(ru_local.TYPE3))

elif FRE <= 25:
    print('{}'.format(ru_local.TYPE4))

