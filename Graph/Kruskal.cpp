void kruskal(vector<pair<ll, pair<ll, ll>>> &res){
    // res == minimum spanning tree vector
    // needs DisjointSet class
    DisJointSet ds;
    vector<int> univ;
    for (int i = 1; i <= n; i++)
        univ.push_back(i);
    ds.makeSet(univ);
    // edges == vector of edges, vector< weight , uv >
    // edges should be sorted.
    for (auto edge : edges){
        int u = edge.second.first;
        int v = edge.second.second;
        if (ds.hasCycle(u, v))
            continue;
        ds.Union(u, v);
        res.push_back(edge);
    }
}
