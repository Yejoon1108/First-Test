#직접 에러 정의하기

class BigNumberError(Exception):
    def __init__(self,msg):
        self.msg=msg
    def __str__(self):
        return self.msg

try:
    print("한 자리 숫자 나누기 전용 계산기.")
    num1=int(input("첫번째 숫자:"))
    num2=int(input("두번째 숫자:"))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("입력값 : {0},{1}".format(num1,num2)) #이걸 일으켜라
    print("{0}/{1}={2}".format(num1,num2,int(num1/num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한자리 숫자만 입력하시오.")
except BigNumberError as err:
    print("에러발생. 한자리 숫자만 입력하시오.")
    print(err)
finally: #프로그램의 성공유무를 떠나 출력하는 것.
    print("계산기를 이용해 주셔서 감사합니다.")