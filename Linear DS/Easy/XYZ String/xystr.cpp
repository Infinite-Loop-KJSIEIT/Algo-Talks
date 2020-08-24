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
        ll ans=0;
        ll n=s.length();
        for(ll i=0;i<n;i++){
            if(s[i]=='x' && s[i+1]=='y'){
                ans++;
                i++;
            }
            else if(s[i]=='y' && s[i+1]=='x'){
                ans++;
                i++;
            }
        }
        cout<<ans<<"\n";
    }
    return 0;
}