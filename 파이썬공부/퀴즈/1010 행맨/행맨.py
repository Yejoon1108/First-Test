import random
word_list=["mega","terara","zeroo"]
word = random.choice(word_list)
print("answer:",word)
letters = "" #사용자로부터 지금까지 입력받은 모든 알파벳

while True:
    succeed = True
    print()
    for w in word: #선택된 단어 범위 안의 w
        if w in letters: #입력한 알파벳을 모아둔 리스트에 w가 있으면
            print(w,end=" ") #w 를 프린트
        else:               #없으면 그자리에 _ 를 프린트
            print("_",end=" ")
            succeed=False
    print()

    if succeed:#(==True):
        print("success")
        break

    letter = input("Input Letter > ")
    if letter not in letters:
        letters += letter

    if letter in word:
        print("Correct")
    else:
        print("Wrong")

