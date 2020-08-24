#include <bits/stdc++.h>
#define ll long long
using namespace std;
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    string s,t;
    cin>>s;
    cin>>t;
    stack<char>ss;
    stack<char>tt;
    for(ll i=0;i<s.length();i++){
        if(s[i]=='#' && !ss.empty()){
            ss.pop();
        }
        else if(s[i]=='#' && ss.empty()){
            continue;
        }
        else{
            char x=s[i];
            ss.push(x);
        }
    }
    for(ll i=0;i<t.length();i++){
        if(t[i]=='#' && !tt.empty()){
            tt.pop();
        }
        else if(t[i]=='#' && tt.empty()){
            continue;
        }
        else{
            char y=t[i];
            tt.push(y);
        }
    }
    ll flag=1;
    if(ss.size()!=tt.size()){
        flag=0;
    }
    while(!ss.empty()){
        if(ss.top()==tt.top()){
            ss.pop();
            tt.pop();
        }
        else{
            flag=0;
            break;
        }
    }
    if(flag==1){
        cout<<"True"<<"\n";
    }
    else{
        cout<<"False"<<"\n";
    }
    return 0;
}