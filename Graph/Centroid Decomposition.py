import collections
def addEdge(u, v):
    tree[u].append(v)
    tree[v].append(u)
def DFS(src, visited, subtree_size, n):
    visited[src] = True
    n[0] += 1
    subtree_size[src] = 1
    for it in tree[src]:
        if not visited[it] and not centroidMarked[it]:
            DFS(it, visited, subtree_size, n)
            subtree_size[src] += subtree_size[it]
def getCentroid(src, visited, subtree_size, n):
    is_centroid = True
    visited[src] = True
    heaviest_child = 0
    for it in tree[src]:
        if not visited[it] and not centroidMarked[it]:
            if subtree_size[it] > n/2:
                is_centroid = False
            if heaviest_child == 0 or subtree_size[it] > subtree_size[heaviest_child]:
                heaviest_child = it
    if is_centroid and n - subtree_size[src] <= n/2:
        return src
    return getCentroid(heaviest_child, visited, subtree_size, n)
def getCentroidTree(src):
    visited = [False]*MAXN
    subtree_size = [0]*MAXN
    n = [0]
    DFS(src, visited, subtree_size, n)
    visited = [False]*MAXN
    centroid = getCentroid(src, visited, subtree_size, n[0])
    centroidMarked[centroid] = True
    return centroid
def decomposeTree(root):
    global arr
    cend_tree = getCentroidTree(root)
    arr.append(cend_tree)
    for it in tree[cend_tree]:
        if not centroidMarked[it]:
            decomposeTree(it)
MAXN = 10**6
tree = collections.defaultdict(list)
centroidTree = collections.defaultdict(list)
centroidMarked = [False]*MAXN
decomposeTree(1)
