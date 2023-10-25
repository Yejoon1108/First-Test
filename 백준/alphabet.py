# input_word = input("")
# 아크로바틱 = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
# i = 0
# cnt = 0
# while i < len(input_word):
#     if input_word[i:i+3] in 아크로바틱:
#         i+=3
#         cnt +=1
#     elif input_word[i:i+2] in 아크로바틱:
#         i+=2
#         cnt +=1
#     else:
#         i += 1
#         cnt += 1
# print(cnt)
#
#
# #실패요인
# # 문자들을 조건으로만 생각했다. 치환해서 리스트에 넣고 while문을 돌리면되는거였다

input_word = input("")
아크로바틱 = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for i in 아크로바틱:
    input_word = input_word.replace(i,"*")

print(len(input_word))