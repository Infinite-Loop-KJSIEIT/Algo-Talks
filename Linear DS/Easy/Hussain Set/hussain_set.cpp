#include <bits/stdc++.h>
#define ll long long
using namespace std;
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
        ll n,m;
        cin>>n>>m;
        ll arr[n];
        for(int i=0;i<n;i++){
            cin>>arr[i];
        }
        sort(arr, arr+n); 
        queue<ll> q1;
        queue<ll> q2;
        ll ans[63000005];
        for(int i=n-1;i>=0;i--){
            q1.push(arr[i]);
        }
        for (ll i=1; i<=63000000;i++){
            if(q2.empty()){
                if(q1.empty()){
                    break;
                }
                    ll x=q1.front();
                    q1.pop();
                    q2.push(x/2);
                    ans[i]=x;
            }
            else if(q1.empty()){
                ll x=q2.front();
                q2.pop();
                q2.push(x/2);
                ans[i]=x;
            }
            else{
                ll x =q1.front();
                ll y =q2.front();
                if(x>y){
                    q1.pop();
                    q2.push(x/2);
                    ans[i]=x;
                }
                else{
                    q2.pop();
                    q2.push(y/2);
                    ans[i]=y;
                }
            }
        }
        while(m--){
            ll q;
            cin>>q;
            cout<<ans[q]<<"\n";
        }
}