def first_word(sentence):
    index = 0
    for word in sentence:
        if word == " " or word == "," or word == ".":
            f_w = sentence[0:index]
            break
        index += 1
    print(f_w)

first_word("greet, . a")

#실수 했던것 만약 두 변수가 연달아서 나오면 인덱스는 그대로 더 올라간다.
#그걸 마주치면 바로 break 되게 해야함