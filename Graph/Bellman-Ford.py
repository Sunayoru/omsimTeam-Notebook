distance = [float('inf') for _ in range(n + 1)]
for k in range(1, n):
    for u in range(1, n + 1):
        for v, w in adj[u]:
            distance[v] = min(distance[v], distance[u] + w)
for u in range(1, n + 1):
    for v, w in adj[u]:
        if distance[v] > distance[u] + w:
            report_negative_cycle()
