import math
def dfs(u, p, memo, lev, log, g):
	memo[u][0] = p
	for i in range(1, log + 1):
		memo[u][i] = memo[memo[u][i - 1]][i - 1]
	for v in g[u]:
		if v != p:
			lev[v] = lev[u] + 1
			dfs(v, u, memo, lev, log, g)
def lca(u, v, log, lev, memo):
	if lev[u] < lev[v]:
		temp = u
		u = v
		v = temp
	for i in range(log, -1, -1):
		if (lev[u] - pow(2, i)) >= lev[v]:
			u = memo[u][i]
	if u == v:
		return v
	for i in range(log, -1, -1):
		if memo[u][i] != memo[v][i]:
			u = memo[u][i]
			v = memo[v][i]
	return memo[u][0]
for _ in range(int(input())):
    n, q = [int(x) for x in input().split()]
    log = math.ceil(math.log(n, 2))
    g = [[] for i in range(n + 1)]
    memo = [[-1 for i in range(log + 1)]
    			for j in range(n + 1)]
    lev = [0 for i in range(n + 1)]
    checker = [set() for x in range(n+1)]
    for _ in range(n-1):
        a,b = [int(x) for x in input().split()]
        if _ == 0:
            root = a
        g[a].append(b)
