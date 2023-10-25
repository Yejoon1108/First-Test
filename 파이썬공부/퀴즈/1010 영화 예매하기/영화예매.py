좌석리스트 = []

for 열 in "ABC":
    for a in range(1,21):
        좌석 = ["{}{}".format(열,a)]
        좌석리스트+=좌석
print("{0: >33}".format("SCREEN"))
print(좌석리스트[0:20:2])
print(좌석리스트[20:40:2])
print(좌석리스트[40:60:2],"\n")
선택한_좌석 = input("좌석을 선택해주세요 : ")

if 선택한_좌석 in 좌석리스트:
    print("15,000원입니다.")

