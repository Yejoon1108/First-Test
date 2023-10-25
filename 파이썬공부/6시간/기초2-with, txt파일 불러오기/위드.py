#import pickle#
##
#with open ("profile.pickle","rb") as profile_file: #저 파일을 열어서 변수에 저장을하겠다
#    print(profile_file) #이렇게하면 피클 그 파일만 연결된채로 있는거임 그렇기에
#    print(pickle.load(profile_file)) #저 변수에 저장된 피클을 로드해줘야함
#with open("study.txt","w",encoding="utf8") as study_file:
#    study_file.write("파이썬을 열심히 공부하고 있어요")

with open("study.txt", "r", encoding="utf8") as study_file: #이런식으로 변수에 txt값을 할당해서
    print(study_file.read()) #txt를 읽어내는것.

    #close 할 필요가없다