def corret_sentece(sentence):
    sentence = sentence[0].upper() + sentence[1:]

    if sentence != ".":
        sentence = sentence + "."

    print(sentence)

corret_sentece("greetings, freind")


#몰랐던 점
#str 의 index 지정하는 법
#upper 처리 하면 그걸 함수에 다시 지정해줘야하는것 