n,m = [int(x) for x in input().split()]
graph = [[0 for x in range(n)] for y in range(n)]
for _ in range(m):
    a,b,c = [int(x) for x in input().split()]
    graph[a-1][b-1] += c
def BFS(graph, s, t, parent):
    visited = [False] * len(graph)
    queue = []
    queue.append(s)
    visited[s] = True
    for u in queue:
        for ind in range(n):
            if visited[ind] is False and graph[u][ind] > 0:
                queue.append(ind)
                visited[ind] = True
                parent[ind] = u
    return True if visited[t] else False
def FordFulkerson(graph, source, sink):
    parent = [-1] * (len(graph))
    max_flow = 0
    while BFS(graph, source, sink, parent):
        path_flow = float("Inf")
        s = sink
        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]
        max_flow += path_flow
        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]
    return max_flow
print(FordFulkerson(graph,0,n-1))
