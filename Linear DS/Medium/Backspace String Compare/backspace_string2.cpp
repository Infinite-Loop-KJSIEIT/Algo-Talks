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
    ll i=s.length()-1;
    ll j=t.length()-1;
    ll flag=1;
    while(i>=0 || j>=0){
        int count=0;
        while(i>=0 && (count>0 || s[i]=='#')){
            if(s[i]=='#'){
                count++;
                i--;
            }
            else{
                count--;
                i--;
            }
        }
        while(j>=0 && (count>0 || t[j]=='#')){
            if(t[j]=='#'){
                count++;
                j--;
            }
            else{
                count--;
                j--;
            }
        }
        if(i>=0 && j>=0){
            if(s[i]!=t[j]){
                flag=0;
            }
            else{
                i--;
                j--;
            }
        }
        else{
            if(i>=0 || j>=0){
                flag=0;
            }
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