import heapq as hq
def topologicalSort():
    V = len(adj)
    in_degree = [0] * V
    for u in range(V):
        for x in adj[u]:
            in_degree[x] += 1
    s = []
    for i in range(V):
        if in_degree[i] == 0:
            hq.heappush(s, -i)
    cnt = 0
    top_order = []
    while s:
        u = -hq.heappop(s)
        top_order.append(u)
        for x in adj[u]:
            in_degree[x] -= 1
            if in_degree[x] == 0:
                hq.heappush(s, -x)
        cnt += 1
    if cnt != V:
        print("IMPOSSIBLE")
        return
    ans = []
    for i in range(len(top_order)):
        ans.append(top_order[i])
    ans.pop()
    print(*ans)
for x in range(int(input())):
    done = False
    n, m = [int(x) for x in input().split()]
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = [int(x) for x in input().split()]
        adj[u].append(v)
    topologicalSort()
