#key 와 밸류 형태
cabinet = {3:"유재석",100:"김태호"}
print(cabinet[3])
print(cabinet.get(3)) # 소괄호인거 주의
#print(cabinet[5]) #이거는 오류가 나지만
print(cabinet.get(5, "사용가능")) #이거는 오류가 안남

print (3 in cabinet) # key in 변수
print (5 in cabinet) # key in 변수
c={"a-3":"재슥아","b-3":"노래좋다"}

c["d-3"] ="세호야" # 이미 존재하는 키면 거기다가 업데이트하는것 키추가

del c["a-3"] #지우기 해당키를 지우는것
print(c)

#key 들만 출력
print(cabinet.keys())

#value 들만 출력
print(cabinet.values())
print(cabinet[3])

# 다 비우기
cabinet.clear()
print(cabinet)

