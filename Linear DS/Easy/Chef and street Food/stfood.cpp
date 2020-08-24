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
        ll n,max=0;
        cin>>n;
        while(n--){
            ll s,p,v,temp=0;
            cin>>s>>p>>v;
                temp=(p/(s+1))*v;
                if(temp>max){
                    max=temp;
                }
        }
        cout<<max<<"\n";
    }
    return 0;
}