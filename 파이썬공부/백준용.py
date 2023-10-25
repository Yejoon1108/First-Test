# import datetime
# from random import *
# now=datetime.datetime.now()
# A = now.strftime("%H")
# B = now.strftime("%M")
# C = randint(0,1001)
# print(type(C))
# end_time=now.strftime("%H,%M") + datetime.timedelta(minutes=C)
# print(f"{A} {B}")
# print(now + C)
# import datetime
# from random import *
# now = datetime.datetime.now()
# A = now.strftime("%H")
# B = now.strftime("%M")
# C = now + datetime.timedelta(minutes=randint(0,1001))
# print(C.strftime("%H %M"))

A,B = map(int,input().split()) # int ,
C = int(input())
if C%60>0:
    A+=C//60
    B+=C%60
    if B>=60:
        B=B-60
        A+=1
        if A >= 24:
            A = A - 24
print(A,B)

A, B = map(int, input().split())
C = int(input())
current_minutes = A * 60 + B
new_minutes = current_minutes + C
A = new_minutes // 60
B = new_minutes % 60
A %= 24

print(A, B)