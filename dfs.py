graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

graph_copy = {}

def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        #print(visited)
        vertex = stack.pop()
        #print(vertex)
        print(vertex)
        if vertex not in visited:
            visited.add(vertex)
            graph_copy[vertex] = set(graph[vertex])
            print(vertex)
            print(graph[vertex])
            stack.extend(graph[vertex] - visited)
    return visited

dfs(graph, 'A') # {'E', 'D', 'F', 'A', 'C', 'B'}

print(graph_copy)
