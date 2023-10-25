#import sys
#print("Python", "java", file=sys.stdout)
#print("Python", "java", file=sys.stderr) # 빨간색이네 ;; 에러 색으로 된다는건가

##socre={"수학":0,"영어":50,"코딩":100}
#for subject, score in socre.items(): #subject= 키 score  밸류
#    #print(subject,score)
#    print(subject.ljust(4), str(score).rjust(4), sep=":") #왼쪽 정렬 8칸 공간 두기

#대기 순번표
# 001, 002, 003 ...
#for num in range(1,21):
#    print("대기번호".ljust(4),str(num).zfill(3), sep=":") #값이 없는곳에는 0으로채워달라는것

answer = input("아무 값이나 입력하세요:") #input을 넣으면 str 로 뽑히기떄문에 int로 뽑으려면 따로 설정해줘야함

print("입력하신 값은"+answer+"입니다")