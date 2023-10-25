#재귀 recursion > stack
#일상에서의 recursion > 거울과 거울을 비추는 예가 있음 (엘레베이터 양쪽벽면거울)
#factorial 은
# 1!=1 2!=2*1 3!=3*2*1 > basecase
# 2!=2*1! 3!=3*2!
#코딩한다고 생각하면 식을 만들기.
#n!=n*(n-1)!
#return 이란 함수(def)의 return 과 일반 return 이있는데
#해당 문을 빠져나오라는 return, 함수의 return은 그 값을 가지고 다시 함수를 실행하라는 것이다.
def fact(n): #def 는 스택형식임
    if n==1 :return 1 # (basecase 기본 조건) n 이 1이 될때까지 함수를 실행하고, 1이 되면 이 값을 가지고
    else:               # 함수 값을 가져가라. (return) 근데 이 else 없어도되긴함
        return n*fact(n-1) #1이 될때까지 이 값을 가지고 돌아가라. 1이 되면 1을 더해서 가는것
     #리턴 뒤의 것들은 실행이 안된다.
A=[]
for n in range(1,7):
    A.append(fact(n))

print(A)

def Solve(count):
    if count==0: return
    Solve(count - 1)
    print("재귀호출",count)

Solve(6)





#def one():        one()이라는 함수를 발동시켰을때
#print("1번 첫째줄)  #1.
#two()              #2.
#print("1번 셋째줄) #5 함수 끝.
#def two():
#print("2번 첫째줄)  #2-1
#three()            #2-2
#print("2번 셋째줄)  #4  > 함수가 끝났으니 two 라는 함수를 팝시켜서 one으로 돌아감
#def three():
#print("3번 첫째줄)  #3-1 > 함수가 끝났으니 three 라는 함수를 팝시켜서 two로 돌아감
#one()            >결과 1번 첫째줄 2번 첫째줄 3번첫째줄 2번 셋째줄 1번셋째줄