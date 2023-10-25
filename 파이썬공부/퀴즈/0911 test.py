#input nodenum, edgenum
#node : 트리(tree) 구조에서 데이터의 상하위 계층을 나타내는 위치의 항목.
#각 노드를 연결해 주는 것이 분기(分岐), edge 이다
# 즉 node > edge 형태로 이동하는것이다.
import sys
sys.stdin = open('../../venv/input.txt', 'r')

def dfs(start): #dfs 라는 것을 정의하는 것.
    visited=[] # 방문기록을 남기기위한 배열을 만들고
    stack = [start] # 첫 시작 값을 스택에 넣고 시작한다.
    while stack: #스택이 있는 동안에는
        here=stack.pop() # 지금 위치한 곳이 스택에서 pop한 값이다.
        if here not in visited: # here을 팝했는데 방문기록이 없으면
            visited.append(here) # here을 방문기록에 새기고
            stack.extend(sorted(MyMap[here], reverse= True)) #stack에
    return visited
NodeNum, EdgeNum = map(int, input().split())

MyMap=[[] for a in range(NodeNum+1)]

for a in range(EdgeNum):
    start, stop = map(int, input().split())
    MyMap[start].append(stop) #start, stop 은 map 에서 가져온 것. start에 해당하는 index에 stop값을 추가하라.
    MyMap[stop].append(start) #stop값의 인덱스에 start 값을 입력해라.
print(MyMap)

print(dfs(1))