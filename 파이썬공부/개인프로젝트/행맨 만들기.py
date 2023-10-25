출제 = input("단어를 입력해주세요 : ")
알파벳_입력됨 = ""
chance = 10
while True:
    성공여부=True
    print()
    for w in 출제:
        if w in 알파벳_입력됨:
            print(w,end=" ")
        else:
            print("_",end=" ") #성공여부가 여기를 타고 내려가기때문에 반복이됨
            성공여부=False
    print()
    print("남은기회 :", chance)

    if chance == 0:
        print("게임 실패")
        break
    print()
    if 성공여부==True:
        print("게임 성공")
        break

    알파벳=input("알파벳을 입력해주세요 : ")
    if 알파벳 not in 알파벳_입력됨:
        알파벳_입력됨+=알파벳

    if 알파벳 in 출제:
        print("Corret")
    else:
        print("Wrong")
        chance -= 1






