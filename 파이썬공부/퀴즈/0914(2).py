def Hanoi(n,ffrom,to,spare):
    if n==1:
        print(ffrom+"에서"+to+"로 이동")
        return
    Hanoi(n-1,ffrom,spare,to)
    Hanoi(1,ffrom,to,spare)
    Hanoi(n-1,spare,to,ffrom)

Hanoi(3,'from','to','spare')
#fibonacci Number= 앞의 두개를 더해서 뒤에 하나를 넣는것. 점안식.
#즉 앞의 2개를 알아야 뒷수를 쓸 수 있음
#f(5)=f(4)+f(3) << 이게 필수
#f(n)=f(n-1)+f(n-2)

def f(n): #피보나치 넘버 점안식 기본
    if n==1 : return 1
    if n==2 : return 1
    return f(n-1)+f(n-2)
#memoization
#f(1),f(2)는 베이스케이스
#피보나치 값을 배열에 각각 입력해두고 f(n-1),f(n-2)를 불러오는 것임
#코드는 다음 차수에 천천히 보는걸로


##global##
#전역변수를 설명하기 위해서는 파이썬 함수가 필요하다.
#함수 안의 변수들은 지역변수로 함수 영역 밖에서는 호출하여 사용할 수 없다.
#예를 들어 아래와 같은 경우, a변수를 함수 밖에서는 사용할 수 없다.
#def test():
#    a = 3
#    b = 2

#    return a + b

#print(test())
#print(a)
#함수에 사용된 a는 지역변수이기 때문에, 함수 바깥의 영역에서는 호출하여 사용할 수 없다.
#사용을 하려면 아래와 같이 a를 전역변수로 선언해야 한다.
#def test():
#    global a
#    a = 3
#    b = 2
#
#    return a + b
#
#print(test())
#print(a)
##함수 밖에서 global로 전역변수 선언하기##
#함수 밖에서 global로 전역변수 선언을 하였어도,
#함수 안에도 전역변수 사용을 또 명시해 주어야 한다
stairs = 3
ans = 0
def solve(here):
    global stairs, ans
    if here==stairs : # base case
        ans+=1
        return
    if here > stairs : # base case
        return
    solve(here+1) #stair 이 될때까지 1씩 더하는 것.
    solve(here+2)

solve(0)
print(ans)
#solve(here+1)의 경우
#solve(0+1)>if문 충족 x 다시 solve(here+1)로 온다.
#solve(1+1) 은 또다시 충족 x 다시 solve(here+1) > solve(3)
#here 과 staris 동일. 자동적으로 밑에꺼는 리턴
#ans +1
#다시 solve(2)로 돌아가서 solve(4) > stair
#1로 돌아가서 here+2 실행
#ans+1
#다시 here 0 으로 돌아가서 +2 실행
# 0_2 에서 here+1 가능 ans+1
# 0_2 에서 here+2 가능 but here>stairs 리턴
#here=0으로 다시 돌아옴 return. def 끝남

