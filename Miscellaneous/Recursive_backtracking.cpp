void rec(string s){
    // n and ans are global variables
    // generate decimals up to n with 3, 5, 7 as its digits
    if (s != "" && stoll(s) > n) return;
    int a=0,b=0,c=0;
    for (auto d : s){
        if (d == '3') a++;
        else if (d == '5') b++;
        else if (d == '7') c++;
    }
    if (a && b && c) ans += 1;
    rec(s + '3');
    rec(s + '5');
    rec(s + '7');
}
