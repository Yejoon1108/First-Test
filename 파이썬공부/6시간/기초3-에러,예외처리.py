try: #try 안의 문장을 실행하다가 except 뒤의 오류가 발생했을때 그 아래의 행을 실행한다.
    print("나누기 전용 계산기")
    nums=[]
    nums.append(int(input("첫 번째 숫자를 입력하세요 :")))
    nums.append(int(input("두 번째 숫자를 입력하세요 :")))
    #nums.append(int(nums[0]/nums[1]))
    print("{0} / {1} = {2}".format(nums[0],nums[1],nums[2]))
except ValueError:
    print("에러가 발생했읍니다.")
except ZeroDivisionError as err: #err 문구를 그대로 출력할수있다.
    print(err)
except Exception as err: 
    print("알수없는 오류 발생.")
    print(err)