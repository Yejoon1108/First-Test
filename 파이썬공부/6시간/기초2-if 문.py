#계절 = str(input("오늘의 날씨는?(비/미세먼지/맑음):"))
#if 계절 == "비" or 계절 == "눈":
#    print("우산을 챙기세요")
#elif 계절 == "미세먼지":
#    print('마스크를 챙기쇼')
#else:
#    print("준비물은 화창한 얼굴")

temp=int(input("오늘의 온도는?:"))
if temp>30:
    print("너무드븐디요")
elif temp>=10 and temp <30:
    print('괜챃ㄴ에여')
elif 0<= temp < 10:
    print("바람은 옷을 벗기지 못했다")
else:
    print("추버디질듯")