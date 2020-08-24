#include <bits/stdc++.h>
#define ll long long
using namespace std;
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    ll n;
    cin>>n;
    string arr1[n];
    for(ll i=0;i<n;i++){
        cin>>arr1[i];
    }
    ll q;
    cin>>q;
    string arr2[q];
    for(ll i=0;i<q;i++){
        cin>>arr2[i];
    }
    ll arr[q]={0};
    for(ll i=0;i<q;i++){
        for(ll j=0;j<n;j++){
            if(arr2[i]==arr1[j]){
                arr[i]++;
            }
        }
    }
    for(ll i=0;i<q;i++){
        cout<<arr[i]<<"\n";
    }
    return 0;
}