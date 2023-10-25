import pickle
profile_file = open("profile.pickle","rb")
profile = pickle.load(profile_file)
print(profile)
profile_file.close() #파일에 저장하고 저장한 파일을 불러올수있는 유용한 모듈


