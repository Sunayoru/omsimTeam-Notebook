// comparator syntax
struct{
    bool operator()(int a, int b) const { return abs(a) < abs(b); }
} abscomp;
