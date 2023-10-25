#당신은 카카오 택시 기사
#50명 승객 매칭, 총 탑승 승객 수 구하는 프로그램
#1. 승객별 운행소요시간은 5~50분 사이의 난수
#2. 소요시간 5~15분 사이의 승객만 매칭
from random import *
import random
index=0
for i in range(1,51):
    시간 = randint(5,51) #소요시간
    if 5<=시간<=15:
        print("[O] {0}번째 손님(소요시간 : {1}분)".format(i,시간))
        index+=1 #탑승시킨 손님 수
        continue
    else:
        print("[ ] {0}번째 손님(소요시간 : {1}분)".format(i,시간))
        continue
print("총 탑승 승객 : {}분".format(index))