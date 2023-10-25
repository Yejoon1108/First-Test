#선택정렬이란
data=[3,6,5,4,1,2]
#이중에서 가장 작은 값을 찾아서 맨앞 인덱스시작
#이걸 하나씩 밀면서 반복
#그래서 재귀로 구현이 가능함
howmany = len(data)


def jr(now):
    if now==howmany-1: return #인덱스의 값이니까 -1해줘야함
    where=data.index(min(data[now:howmany]))
    data[now], data[where] = data[where], data[now]
    jr(now+1)
jr(0)
print(data)
mymap=[(1,2),(1,3),(1,4),(1,5),(2,1),(2,6),(2,7),(3,1),(4,1),(5,1),(5,6),(6,2),(6,5),(6,7),(7,2),(7,6)]
##DFS##
graph = dict()

graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']


def dfs(graph, start_node):
    ## 기본은 항상 두개의 리스트를 별도로 관리해주는 것
    need_visited, visited = list(), list()

    ## 시작 노드를 시정하기
    need_visited.append(start_node)

    ## 만약 아직도 방문이 필요한 노드가 있다면,
    while need_visited:

        ## 그 중에서 가장 마지막 데이터를 추출 (스택 구조의 활용)
        node = need_visited.pop()

        ## 만약 그 노드가 방문한 목록에 없다면
        if node not in visited:
            ## 방문한 목록에 추가하기
            visited.append(node)

            ## 그 노드에 연결된 노드를
            need_visited.extend(graph[node])

    return visited
print(dfs(graph,'A'))