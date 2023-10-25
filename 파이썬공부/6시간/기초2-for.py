for waiting_no in range(1,6):
    print("대기번호: {}".format(waiting_no))

starbucks=[["아이언맨"],["토르"],["아이엠그루트"]]
customers=[]
for n in range(1,4):
    customers+=starbucks[n-1]
    print("{a}번째 고객 {b}님 커피가 준비되었습니다.".format(a=n,b=customers[n-1]))