def open_account():
    print("새로운 계좌가 생성되었습니다.")

def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은{0}원 입니다.".format(balance + money))
    return balance + money
def withdraw(balance,money):
    if balance>=money:
        print("출금이 완료되었습니다. 잔액{}원".format(balance-money))
        return balance - money
    else:
        print("출금이 불가능합니다. 잔액이 부족합니다{}.".format(balance))
        return balance
def withdraw_night(balance,money):
    commission=100 #수수료 100원
    return commission, balance - money - commission




balance=0 #잔액
balance = deposit(balance,1000)
commission, balance = withdraw_night(balance, 500)
print("수수료{0},잔액{1}원".format(commission,balance))
#드디어 이해했다.
#money 1000 이라는 값과 지금 이미 명시된 0이라는 발란스의 값
#이 두개를 가지고 식을 수행하고
#그 수행한 값을 balance 에 넣는다는 것.
#그것이 def 이다
 #그래서

#balance = withdraw(balance,2000)

#https://www.youtube.com/watch?v=kWiCuklohdY&t=6257s
#2:38
