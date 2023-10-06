int n, m;
vector<vector<pair<int, int>>> adj;
ll dist[500010]; // MAXN
int vis[500010]; // MAXN

void spfa(int s){
    for (int u = 0; u <= n; u++){
        dist[u] = 1e18;
    }
    dist[s] = 0;
    queue<int> q;
    q.push(s);
    vis[s] = 1;
    while (!q.empty()){
        int u = q.front(); q.pop();
        vis[u] = 0;
        for (int i = 0; i < adj[u].size(); i++){
            int v = adj[u][i].first;
            int w = adj[u][i].second;
            if (dist[v] > dist[u] + w){
                dist[v] = dist[u] + w;
                if (!vis[v]){
                    q.push(v);
                    vis[v] = 1;
                }
            }
        }
    }
}
