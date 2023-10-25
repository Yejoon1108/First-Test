N = int(input(""))
cnt = 0

while 1:
    if N%5 == 0: #5로 나누었을때 떨어지게 되면 그대로끝
        cnt += N//5
        print(cnt)
        break
    N -= 3 #그렇지 않은 경우에 3씩 빼고
    cnt += 1
    if (N<0):
        print(-1)
        break


