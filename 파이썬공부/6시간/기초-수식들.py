station=["사당","신도림","인천공항"]
for n in range(0,len(station)):
    print(station[n]+"행 열차가 들어오고 있습니다.")

print(abs(-5)) # 절댓값
print(pow(4,2)) #4^2 = 4*4 = 16 제곱
print(max(5,12)) # 최대값 뽑기
print(min(5,12)) # 최소값뽑기
print(round(3.14)) #반올림
print(round(3.99)) #반올림

from math import *
print(floor(4.99)) #내림
print(ceil(3.14))# 올림
print(sqrt(16)) #제곱근 float 형태로 뜨네 ;;

from random import *
import random


day=[]

for n in range(0,4):
    day.append(int(randrange(4,29))) #randint(4,28) 도 동일


cchoice=random.choice(day)

print("스터디의 날짜는 "+str(cchoice)+" 일로 결정되었습니다")

sentence='나는 소년입니다.'
print(sentence)
sentence2="파이썬은 쉬워요?"
sentence3 = """
나는 소년이고,
파이썬은 쉽나?
"""
print(sentence3)

#슬라이싱

jumin="000209-3118112"
성별=jumin[7]
if 성별==str("3"):
    print("성별: 남자")
elif 성별==str("4"):
    print("성별: 여자")
else:
    print("-를 포함하여 입력하였는지 확인하거나, 주민등록번호 뒷자리의 값이 올바른지 확인하십시오")
년=jumin[0:2]
월=jumin[2:4]
일=jumin[4:6]
print("생년월일:"+jumin[0:6])
print("뒷 7자리:"+jumin[7:])
print("뒤 7자리 (뒤에부터)"+jumin[-1:6:-1])

#문자열 처리함수
python="python is amazing"
print(python.lower())
#https://www.youtube.com/watch?v=kWiCuklohdY
#56분
print(python[0].isupper())
print(len(python))
index=python.index("n")
#print(data.replace(0,1)) # AttributeError: 'list' object has no attribute 'replace'
index=python.index("n",index+1)
print(index)
print(python.find("java")) # 변수에 포함안될때 -1 로 변환
#print(python.index("java")) # 얘는 오류가 남
print(python.count("n"))





