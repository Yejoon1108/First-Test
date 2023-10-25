큐 = [1,3,4,5,6]
class SoldOutError(Exception):
    def __init__(self,msg):
        SoldOutError.msg=msg
    def __str__(self):
        return self.msg
def 큐_():
    try:
        order = int(input("추가하시려는 정수를 입력해주세요:"))
        if isinstance(order, int):
            print("정수가 확인되었습니다.")
            큐.append(order)
        elif type(order)!=type(1):
            raise ValueError
            return 큐_()
    except ValueError:
        print("올바른 정수가 입력되지 않았습니다. 다시한번 확인해주세요.")
    print(큐)



큐2=[1235,"a","33"]
def 큐_2():
    try:
        while len(큐2)==3:
            정수 = int(input("정수를 입력해주세요"))
            if type(정수)==type(1):
                print("정수네요")
            else:
                raise ValueError
            return 큐_2()
    except ValueError:
        print("정수가 아니잖아 ㅇㅅㄲㅇ")


큐_2()


