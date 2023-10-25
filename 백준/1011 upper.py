words=input().upper()
u_words= list(set(words))
print(u_words)
cnt_list=[]
for W in u_words:
    cnt = words.count(W)
    cnt_list.append(cnt)
print(cnt_list)

a_c = {}

if cnt_list.count(max(cnt_list)) > 1:
    print("?")
else:
    max_index=cnt_list.index(max(cnt_list))
    print(u_words[max_index])


