from collections import defaultdict
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.Time = 0
    def addEdge(self, u, v):
        self.graph[u].append(v)
    def SCCUtil(self, u, low, disc, stackMember, st):
        disc[u] = self.Time
        low[u] = self.Time
        self.Time += 1
        stackMember[u] = True
        st.append(u)
        for v in self.graph[u]:
            if disc[v] == -1:
                self.SCCUtil(v, low, disc, stackMember, st)
                low[u] = min(low[u], low[v])
            elif stackMember[v] == True:
                low[u] = min(low[u], disc[v])
        w = -1
        temp = set()
        if low[u] == disc[u]:
            while w != u:
                w = st.pop()
                if w != 0:
                    temp.add(w)
                stackMember[w] = False
        if len(temp) != 0:
            strong.append(temp)
    def SCC(self):
        disc = [-1] * (self.V)
        low = [-1] * (self.V)
        stackMember = [False] * (self.V)
        st = []
        for i in range(self.V):
            if disc[i] == -1:
                self.SCCUtil(i, low, disc, stackMember, st)
n, m = [int(x) for x in input().split()]
g = Graph(n+1)
g.SCC()
