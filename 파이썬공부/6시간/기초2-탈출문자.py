# \n 줄바꿈
#print("백문이 불여일견\n백견이 불여일타")

#저는 "나도코딩"입니다.
#
#print('저는 "나도코딩" 입니다.') # 방법 1
#print("저는 \"나도코딩\" 입니다.") # 방법 2 \"abcd\" 따옴표 앞으로 와야함

# \\ : 문장 내에서 하나의 \로 바뀜
#print("C:\\Users\\qmdl5\\PycharmProjects\\pythonProject\\venv\\Scripts\\python.exe C:\\Users\\qmdl5\\PycharmProjects\\pythonProject\\파이썬공부\\6시간\\탈출문자.py")

#\r:커서를 맨앞으로 이동
#\뒤의 문장만 출력

#print("Red  Apple\rPine")

# \b : 백스페이스 (한글자 삭제)
#print("Redd\bApple")

#\t :탭
#print("1\t2\t3\t4")
#for n in range(0,2):
#    주소=input("http:// 를 포함한 주소를 입력하시오:")
#    메인주소=주소.strip("http://"".com""www")
#    print(f"password : {메인주소[0:3]}{len(메인주소)}{메인주소.count('e')}!")

#모범답안
url="http://www.naver.com"
my_add=url.replace("http://www.","")
my_add=my_add[:my_add.index(".")]
print(my_add)
password=my_add[:3]+str(len(my_add))+str(my_add.count("e"))+"!"
print("{0}의 비밀번호는 {1} 입니다.".format(url,password))



