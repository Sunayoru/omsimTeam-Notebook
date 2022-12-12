void prim(int start, vector<pair<ll, pair<ll, ll>>> &res){
    // res == minimum spanning tree vector
    priority_queue<pair<ll, pair<ll, ll>>> pq;
    vector<bool> vis(n+1, false);
    vis[start] = true;
  
    for (auto &[v, w] : graph[start]){
        pq.push({w, {start, v}});
    }
    
    while (!pq.empty()){
        auto edge = pq.top();
        pq.pop();
        ll u = edge.second.second;
        if (vis[u]) continue;
        vis[u] = true;
        res.push_back(edge);
        for (auto &[v, w] : graph[u])
          if (!vis[v]) pq.push({w, {u, v}});
    }
}
