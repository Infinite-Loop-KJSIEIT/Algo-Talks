#include <bits/stdc++.h>
#define ll long long
using namespace std;
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    ll t;
    cin>>t;
    while(t--){
        string s;
        cin>>s;
        ll flag=1;
        char x;
        stack<char>st;
        for(ll i=0;i<s.size();i++){
            if(s[i]=='(' || s[i]=='{' || s[i]=='['){
                st.push(s[i]);
            }
            if(st.empty()){
                flag=0;
            }
            else{
                switch(s[i]){
                    case ')':
                        x=st.top();
                        st.pop();
                        if(x=='[' || x=='{'){
                            flag=0;
                        }
                        break;
                    case ']':
                        x=st.top();
                        st.pop();
                        if(x=='(' || x=='{'){
                            flag=0;
                        }
                        break;
                    case '}':
                        x=st.top();
                        st.pop();
                        if(x=='[' || x=='('){
                            flag=0;
                        }
                        break;
                }
            }
        }
        if(flag==1 && st.empty()){
            cout<<"YES"<<"\n";
        }
        else{
            cout<<"NO"<<"\n";
        }
    }
    return 0;
}