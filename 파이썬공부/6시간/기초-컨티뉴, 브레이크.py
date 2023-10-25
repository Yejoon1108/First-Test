absent=[2,5] #결석
no_book=[7]
for student in range(1,11):
    print("{0}, 출석했니?".format(student))
    if student in absent:
        print("{0}, 는 결석했는데요?".format(student))
        continue
    elif student in no_book:
        print("수업 끝. {}는 따라와".format(no_book))
        break
    else:
        print("네")
    print("{0}, 책읽어줘".format(student))

