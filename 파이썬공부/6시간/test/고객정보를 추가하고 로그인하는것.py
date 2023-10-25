고객리스트 = {}  # 고객 정보를 저장할 딕셔너리

while True:  # 무한 루프
    환영 = input("어서오세요. 처음이신가요? (Y/N): ")

    if 환영 == "N":
        break  # N을 입력하면 루프 종료

    id_input = input("아이디를 입력해주세요: ")
    ps_input = input("비밀번호를 입력해주세요: ")

    # 딕셔너리에 아이디와 비밀번호 추가
    고객리스트[id_input] = ps_input

    print("계속 등록하시겠습니까?")
    계속 = input("(Y/N): ")

    if 계속 != "Y":
        break

# 딕셔너리에 저장된 고객 정보 확인
print("고객 리스트:")
for id, ps in 고객리스트.items():
    print("ID: {0} Password: {1}".format(id,ps))

# 로그인 확인
id = input("ID: ")
ps = input("Password: ")

if id in 고객리스트 and 고객리스트[id] == ps:
    print("로그인에 성공하셨습니다.")
else:
    print("로그인에 실패하셨습니다.")