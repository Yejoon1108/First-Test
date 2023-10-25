#https://withcoding.com/88
#댓글 작성자 중 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰
#추첨프로그램 작성

#조건 1 : 편의상 댓글은 20명 아이디는 1~20
#조건2 : 댓글내용과 상관없이 무작위로 추첨하되 중복 불가
#조건3 : random 모듈의 shuffle 과 sample 을 활용

from random import *
import random
list_id=[]

for n in range(1,21):  #users=list(range(1,21)) 이렇게 해도되고
    list_id.append(n)  #print(type(users))

shuffle(list_id)
print((list_id))
print("--당첨자 발표--")
print("치킨 당첨자 :",list_id.pop(random.choice(list_id)))
print("커피 당첨자 :",sample(list_id,3))
print("--축하합니다--")
print(len(list_id))

users=list(range(1,21))
shuffle(users)
winners=sample(users, 4)
print("--당첨자 발표--")
print("치킨 당첨자 :{}".format(winners[0]))
print("커피 당첨자 :{}".format(winners[1:4]))
print("--축하합니다--")