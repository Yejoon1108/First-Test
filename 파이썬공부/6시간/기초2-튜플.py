#튜플이란?? 리스트지만 추가,및 삭제가 안됨
#그래서 고정값을 쓰는데, 이유는 리스트보다 속도가 빠르기때문
menu = ("돈까스","치즈까스")
print(menu[0])
print(menu[1])

# menu.add("생선까스") # 튜플은 add가 안됨

#name = "김종국"
#age = 20
#hobby = "코딩"
#print(name,age,hobby)
(name, age, hobby) = ("김종국",20,"코딩") #이렇게 집단 선언가능
print(name,age,hobby)