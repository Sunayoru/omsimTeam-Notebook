distance = [-1 for _ in range(n + 1)]
distance[source] = 0
shortest_path_tree_parent = [-1 for _ in range(n + 1)]
queue = [source]
for u in queue:
    for v in adj[u]:
        if distance[v] == -1:
            distance[v] = distance[u] + 1
            shortest_path_tree_parent[v] = u
            queue.append(v)
