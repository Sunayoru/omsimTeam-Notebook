component_index = [-1 for _ in range(n + 1)]
def dfs(u, c):
    component_index[u] = c
    for v in adj[u]:
        if component_index[v] == -1:
            dfs(v, c)

num_components = 0
for u in range(1, n + 1):
    if component_index[u] == -1:
        dfs(u, num_components)
        num_components += 1
