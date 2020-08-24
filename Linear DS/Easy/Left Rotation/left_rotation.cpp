#include <bits/stdc++.h>
#define ll long long
using namespace std;
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    ll n,d;
    cin>>n>>d;
    ll arr1[n],arr2[n];
    for(ll i=0;i<n;i++){
        cin>>arr1[i];
    }
    for(ll i=0;i<n;i++){
        arr2[i]=arr1[(i+d)%n];
    }
    for(ll i=0;i<n;i++){
        cout<<arr2[i]<<" ";
    }
    return 0;
}