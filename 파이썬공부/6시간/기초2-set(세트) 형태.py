#set 는 집합
#중복안됨, 순서없음
my_set = {1,2,3,3,3} #이러면 세트가 되는것 dict 도 {}를 쓰는데 그건 밸류가 있음
print(my_set)
#https://www.youtube.com/watch?v=kWiCuklohdY
#1:44

java={"유재석","김태호","양세형"}
python={"유재석","박명수"}
print(java&python)
#or
print(java.intersection(python))

# 합집합 (java도 할수있거나 pyhton 도 할수있는 개발자)
print(java|python)
print(java.union(python))

#차집합 (java 는 할수있지만 python 몬하는 개발자)
print(java-python)
print(java.difference(python))

#세트에 넣기
python.add("김태호")
print(python)

#세트에서 빼기
java.remove("김태호")
print(java)