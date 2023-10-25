##while
#customer="토르"
#index = 5
#while index>=1:
#    print("{0},커피가 준비되었습니다..{1}번 남았어요".format(customer,index))
#    index-=1
#    if index==0:
#        print("커피 버릴게요")

customer="토르"
person="unknown"

while person!=customer:
    print("{0},커피준비됨".format(customer))
    person=input("이름이 어떻게되세요:")