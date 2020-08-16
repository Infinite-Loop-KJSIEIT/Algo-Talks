#include <bits/stdc++.h>

using namespace std;
string happyLadybugs(string s) {
    int count[26],i,c=0,n=s.length();
    memset(count,0,sizeof(count));
    bool ok=true;
    for(i=0;i<n;i++)
    {
        if(s[i]!='_')
            count[s[i]-'A']++;
        else
            c++;
        if( (i==0 && s[i] != s[i+1]) || 
             (i==s.size()-1 && s[i] != s[i-1]) || 
             (s[i] != s[i-1] && s[i] != s[i+1]) 
        ){
               ok=false;
           }
    }
    for(i=0;i<26;i++)
    {
        if(count[i]==1)
        {
            return "NO";
        }
    }
    if(c>0 || ok) 
    {
        return "YES";
    }
    return "NO";

}

int main()
{
    int t;
    cin >> t;
    while(t--)
    {
        int n;
        string s;
        cin >> n>> s;
        cout << happyLadybugs(s) << endl;
    }
    return 0;
}
