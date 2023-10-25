#큐의 개념
#https://www.daleseo.com/python-queue/
#fifo(first in first out)

#1. 공백 큐 생성. front 와 rear 를 -1 로 설정
#2. 큐가 공백인지 아닌지 확인.
#3. 큐가 포화상태인지 확인
#4. 큐의 rear 원소를 삽입하는 삽입연산(enqueue)
#5. 큐의 front에 있는 원소를 삭제하는 연산(Dequeue)

data=[1,2,3,4,5]
queue=[0]*10
front=rear=-1




for now in range(0,5):
    if rear == len(queue) - 1:
        print("포화상태")
    rear+=1
    queue[rear]=data[now]
    print (data[now])

while front!=rear:
    front+=1
    print(queue[front])
#<<여기까지가 순차큐
#>>> queue = [4, 5, 6]
#>>> queue.append(7)
#>>> queue.append(8)
#>>> queue
#[4, 5, 6, 7, 8]
#>>> queue.pop(0)
#4
#>>> queue.pop(0)
#5
#>>> queue
#[6, 7, 8]

#원형큐 > rear=(rear+1) mod n , front =(front+1) mod n
#원형큐에서 초기 공백상태일때 front , rear 값 0
# 공백 상태, 포화상태 구분을 위해 자리 하나 비워둠
#원형큐에서의 공백상태 조건 front==rear

#((rear+1)"리어의 위치"%len(data)"나누기 리어의 사이즈"==front 즉 0일때
# 이건 포화상태라는 것이다.

# size=6
# c_q=[0]*size
# front=rear=0
# Data=[1,2,3,4,5]
#
# for now in range(5):
#     if((rear+1)%size) == front:
#         print("포화")
#         break
#     else:
#         rear=(rear+1)%size
#         c_q[rear]=Data[now]
# print(c_q)
# while front!=rear:
#     front=(front+1)%size
#     print(c_q)
#     print(c_q[front])
#
# print(c_q)
#
# #deque 는 que 하나를 뒤집어서 올바른 que와 이어붙이는것. 양옆 출력 삽입가능
#
# queue=[0]*1000
# front=rear=-1
#
# peopleno=41
#
# for who in range(1,peopleno+1):
#     rear+=1
#     queue[rear]=who
#
# while front+2!=rear:
#     front+=1; alive1=queue[front]
#     front += 1; alive2 = queue[front]
#     front += 1; dead = queue[front]
#     rear+=1; queue[rear]=alive1
#     rear += 1; queue[rear] = alive2
#
# print(queue[front+1],queue[front+2])