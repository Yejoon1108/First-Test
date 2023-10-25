From=["a","b","c","d","e","f"]
spare=[]
to=[]

def HnT(a):
    if not len(From)==1:
        spare.append(From.pop())
        HnT(a - 1) #1.spare 을 n=[a] 가 될때까지 채우고
        to.append(spare.pop()) # 3. to=[a] 인 상태에서 spare 에서 하나씩 꺼내서 더함
        print(to)  # to = ['a', 'b', 'c', 'd', 'e', 'f']
    else: #HnT(1) 일때 실행
        to.append(From.pop()) #2. to에 마지막 a를 더해줌
        print(to)
        return #함수를 끝내겠습니다.
HnT(len(From))

