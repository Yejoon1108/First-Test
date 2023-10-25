input_word = input("")
words = input_word.upper()
words_lst = list(set(words))
cnt_lst=[]
index = 0
for r_l in words_lst:
    cnt_lst.append(int((words.count(r_l))))

if cnt_lst.count(max(cnt_lst)) == 1:
    max_index =cnt_lst.index(max(cnt_lst))
    print(words_lst[max_index])
else:
    print("?")

#chk_list
#count함수, max 함수, upper 함수 쓰임새