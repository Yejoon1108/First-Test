score_file=open("score.txt","w", encoding="utf8") #utf8 한글 인식을 위해서
print("수학점수 : 0",file=score_file)
print("영어 : 50 ",file=score_file)
score_file.close() #닫는것
score_file = open("score.txt","a",encoding="utf8") #a=append
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100") #print 로 하는건 잘 나가지만 \n 으로 하면 줄바꿈이 안됨
score_file.close()
score_file=open("score.txt","r",encoding="utf8") #reading 모드
print(score_file.read())
score_file=open("score.txt","r",encoding="utf8")
print(score_file.readline(),end="")
#print(score_file.readline(),end="")
print(score_file.readline(),end="")
print(score_file.readline(),end="")
score_file.close()
score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline() #한줄씩 읽어오는것. 즉 커서가 마지막갈때까지 하는것
    if not line:
        print("line이없음")
        break
    print(line) #줄바꿈없애기
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() #list 형태
print(lines)
for line in lines:
    print(line, end="")
score_file.close()
