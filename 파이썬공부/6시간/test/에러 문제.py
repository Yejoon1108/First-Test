# 동네에 항상 대기 손님이 있는 맛있는 치킨집이 있습니다.
#대기 손님의 치킨 요리 시간을 줄이고자 자동 주문 시스템을 제작하였습니다.
#시스템 코드를 확인하고 적절한 예외처리 구문을 넣으시오.

#조건  1 :  1보다 작거나 숫자가 아닌 입력값이 들어올때는 ValueError 로 처리
#   출력 메시지 : "잘못된 값을 입력하였습니다."
#조건  2 :  대기 손님이 주문할 수 있는 총 치킨량은 10마리로 한정
#           치킨 소진 시 사용자 정의 에러[SoldOutError]를 발생시키고 프로그램 종료
#           출력 메시지 : "재고가 소진되어 더 이상 주문을 받지 않습니다."


# chicken = 10
# waiting = 1 #지금 웨이팅은 한명있다.

class SoldOutError(Exception):
    def __init__(self,msg):
        SoldOutError.msg=msg
    def __str__(self):
        return self.msg

def chicken_():
    chicken = 10
    waiting = 1
    try:
        while chicken!=0:
            print("현재 남은 치킨 량 : {0}".format(chicken))
            order = int(input("몇 마리 주문하시겠습니까?:"))
            if order>chicken:
                raise SoldOutError("주문하려는 수량 {0}, 현재 치킨 잔량 {1}".format(order, chicken))
            elif order <= 0:
                raise ValueError
            else:
                chicken-=order
                waiting+=1
                print("{0}번 고객님. {1}마리 주문이 완료되었습니다.".format(waiting,order))
    except ValueError:
        print("잘못된 값을 입력하였습니다.")
        # return chicken_()
    except SoldOutError as err:
        print(err)
        print("재고량보다 주문하시려는 치킨의 수가 더 많습니다.\n"
                 "수량을 확인 한 뒤 다시 주문해주십시오")
        return chicken_()
    finally:
        print("재고가 소진되어 더 이상 주문을 받지 않습니다.")

chicken_()
# try:
#     while chicken!=0:
#         print("남은 치킨 수 {0}".format(chicken))
#         order=int(input("몇 마리 주문하시겠습니까?:"))
#         if order>chicken:
#             raise SoldOutError("주문하려는 수량 {0}, 현재 치킨 잔량 {1}".format(order,chicken))
#
#         else:
#             chicken-=order
#             waiting+=1
#             print("{0}번 고객님. {1}마리 주문이 완료되었습니다.".format(waiting,order))
# except SoldOutError as err:
#       print(err)
#       print("재고량보다 주문하시려는 치킨의 수가 더 많습니다.\n"
#             "수량을 확인 한 뒤 다시 주문해주십시오")
#
#
# finally:
#     print("재고가 소진되어 더 이상 주문을 받지 않습니다.")





