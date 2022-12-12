import heapq
distance = [float('inf') for _ in range(n + 1)]
distance[source] = 0
shortest_path_tree_parent = [-1 for _ in range(n + 1)]
queue = [(distance[source], source)]
done = [False for _ in range(n + 1)]
while len(queue) > 0:
    _, u = heapq.heappop(queue)
    if not done[u]:
        for v, w in adj[u]:
            if distance[v] > distance[u] + w:
                distance[v] = distance[u] + w
                shortest_path_tree_parent[v] = u
                heapq.heappush((distance[v], v))
        done[u] = True
