word = input("").upper()
word_Alpahbet = list(set(word))
print(word)
print(word_Alpahbet)
word_Count = []


for w in word_Alpahbet:
    word_Count.append(word.count(w))
print(word_Count)

if word_Count.count(max(word_Count)) > 1:
    print("?")
else:
    max_index = word_Count.index(max(word_Count))
    print(word_Alpahbet[max_index])
    print(max(word_Count))