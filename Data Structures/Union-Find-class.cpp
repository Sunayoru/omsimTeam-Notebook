class DisjointSet
{
    // put this in main()
    //vector<int> univ;
    //for (int i = 1; i <= n; i++) univ.push_back(i);
    //DisjointSet ds;
    //ds.makeSet(univ);
  
    unordered_map<int, int> parent;
    unordered_map<int, int> rank;
    unordered_map<int, int> members;
 
public:
    void makeSet(vector<int> const &universe)
    {
        for (int i: universe)
        {
            parent[i] = i;
            rank[i] = 0;
            members[i] = 1;
        }
    }

    int Find(int k)
    {
        if (parent[k] != k)
        {
            parent[k] = Find(parent[k]);
        }
 
        return parent[k];
    }
 
    void Union(int a, int b)
    {
        int x = Find(a);
        int y = Find(b);

        if (x == y) {
            return;
        }
 
        if (rank[x] > rank[y]) {
            parent[y] = x;
            members[x] += members[y];
        }
        else if (rank[x] < rank[y]) {
            parent[x] = y;
            members[y] += members[x];
        }
        else {
            parent[x] = y;
            rank[y]++;
            members[y] += members[x];
        }
    }

    int GetMembers(int a)
    {
        // get the number of members of the disjoint set where a is included
        int x = Find(a);
        return members[x];
    }
};
