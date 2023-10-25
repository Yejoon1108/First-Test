class ThailandPackage:
    def detail(self):
        print("[태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만원")

if __name__ == "__main__":  # name 이 main 이면 즉 이 구문은 이게 모듈을 직접실행하는건지 불러오는건지 보는거임
    print("Thailand 모듈을 직접 실행")
    print("이 문장은 모듈을 직접 실행할 떄만 실행되요")
    trip_to = ThailandPackage()
    trip_to.detail()
else:
    print("모듈 호출")
