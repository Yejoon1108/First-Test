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
    n_v, v=list(), list()

    n_v.append(start_node)

    while n_v:
        node=n_v.pop()
        if node not in v:
            v.append(node)
            n_v.extend(graph[node])
    return v

print(dfs(graph,'A'))