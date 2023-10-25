#우리가 사용하고있는 데이터를 파일형태로 저장하는것
#pickle 을 이용해서, 데이터를 가져와서 또 코드에서 이용할수있는것
#import pickle
#profile_file = open("profile.pickle","wb") #피클을 이용하기위해서 바이너리 타입(b)를 선언하는것
#profile={"이름":"박명수","나이":30, "취미":["축구","골프","코딩"]}
#print(profile)
#pickle.dump(profile, profile.pickle) #profile 에 있는 정보를 file에 저장
#profile_file.close()

import pickle

profile_file = open("profile.pickle", "wb") # 피클을 이용하기 위해서 바이너리 타입(b)를 선언하는 것
profile = {"name": "park", "age": 30, "hpbby": ["soccer", "golf", "code"]}
print(profile)

# 파일 객체를 사용하여 pickle.dump 함수 호출
pickle.dump(profile, profile_file)
# 파일을 닫음
profile_file.close()