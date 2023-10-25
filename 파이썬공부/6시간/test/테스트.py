환영 = input("어서오세요. 처음이신가요?(Y/N):")

while 환영=="Y":
    id_file=open("id.txt","a",encoding="utf8")
    id_input = input("아이디를 입력해주세요: ")
    id_file.write(id_input+"\n")

    ps_file = open("ps.txt", "a", encoding="utf8")
    ps_input = input("비밀번호를 입력해주세요: ")
    ps_file.write(ps_input+"\n")
    if not 환영=="Y":
        break
    id_file.close()
    ps_file.close()
    break

id_file=open("id.txt","r",encoding="utf8")
ps_file=open("ps.txt","r",encoding="utf8")
고객리스트={}
고객리스트[id_file.read()]=ps_file.read()

id=input("ID:")
ps=input("Password:")

if id in 고객리스트 and 고객리스트[id]==ps:
    print("로그인에 성공하셨습니다.")
else:
    print("회원이 아니시거나, 아이디 및 비밀번호가 틀렸습니다.")

id_file.close()
ps_file.close()