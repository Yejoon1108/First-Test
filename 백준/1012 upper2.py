word = input("").upper()
word_Alphabet = list(set(word))
word_Count = []
for w in word_Alphabet:
    word_Count.append(word.count(w))

if word_Count.count(max(word_Count)) > 1:
    print("?")
else:
    Max = max(word_Count)
    index=word_Count.index(Max)
    most_AB=word_Alphabet[index]
    print(most_AB)
    print(Max)
# if 3 > 1:
#     print("?")
# else:
#     print(max(word).upper())
