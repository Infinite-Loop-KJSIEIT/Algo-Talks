#include <bits/stdc++.h>
#define ll long long
using namespace std;
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    ll t;
    stack<string>s;
    string st;
    cin>>t;
    while(t--){
        int c;
        cin>>c;
        if(c==1){
            string str;
            cin>>str;
            s.push(st);
            st=st+str;
        }
        else if(c==2){
            int k;
            cin>>k;
            s.push(st);
            st.erase(st.size()-k);
        }
        else if(c==3){
            int k;
            cin>>k;
            cout<<st[k-1]<<"\n";
        }
        else{
            st = s.top();  
            s.pop();
        }
    }
    return 0;
}