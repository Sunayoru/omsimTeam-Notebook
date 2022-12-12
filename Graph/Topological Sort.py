visited = [False for _ in range(n + 1)]
in_dfs_stack = [False for _ in range(n + 1)]
topologically_sorted = []

def toposort(u):
    in_dfs_stack[u] = True
    visited[u] = True
    for v in rev_adj[u]:
        if in_dfs_stack[v]:
            report_cycle()
        elif not visited[v]:
            toposort(v)
    topologically_sorted.append(u)
    in_dfs_stack[u] = False

for u in range(1, n + 1):
    if not visited[u]:
        toposort(u)
