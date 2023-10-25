#모듈이란 필요한 것들끼리 잘 만들어진 파일 이라고 보면됨
# 자동차 를 예로 든다
# 타이어가 마모되거나 펑크가 나면 타이어만 교체하면 된다. 한 부분만 교체하면 된다는 뜻이다.
# 소프트웨어에도 그걸 적용한다면 당연히 코드 재사용도 쉽고 뭐 이리저리 잘 쓸수있다.
# 모듈화 란 필요한 것들끼리 잘 모아둔것.
# 모듈의 확장자는 .py 이다.

# import theater_module as qq #모듈명을 설정가능함
# qq.price(3) # 3명이서 영화보러 갔을 때 가격
# qq.price_morning(4) #4명이서 조조할인
# qq.price_soldier(5) #5명 군인

# from theater_module import *  # 저 모듈로부터 *(모든것)을 추출하겠다. 이경우에는
# price(3) # 이렇게 모듈명이 필요가없는거임

# from theater_module import price, price_morning #이렇게 함수만 지정할수있음
# price(5)
# price_morning(6)

from theater_module import price_soldier as price
price(5) # 실제 모듈의 price 가 아니라 soldier 를 price로 쓰는것이다.