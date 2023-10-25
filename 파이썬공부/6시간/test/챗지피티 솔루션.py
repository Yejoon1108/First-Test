class ChickenShop:
    def __init__(self, initial_chicken):
        self.chicken = initial_chicken
        self.waiting = 1

    def order_chicken(self):
        try:
            while self.chicken > 0:
                print("현재 남은 치킨 량 : {0}".format(self.chicken))
                order = int(input("몇 마리 주문하시겠습니까?:"))
                if order > self.chicken:
                    raise SoldOutError("주문하려는 수량 {0}, 현재 치킨 잔량 {1}".format(order, self.chicken))
                elif order <= 0:
                    raise ValueError("잘못된 값을 입력하였습니다.")
                else:
                    self.chicken -= order
                    self.waiting += 1
                    print("{0}번 고객님. {1}마리 주문이 완료되었습니다.".format(self.waiting, order))
        except ValueError as ve:
            print(ve)
        except SoldOutError as soe:
            print(soe)
        finally:
            print("재고가 소진되어 더 이상 주문을 받지 않습니다.")

initial_chicken = 10
shop = ChickenShop(initial_chicken)
shop.order_chicken()