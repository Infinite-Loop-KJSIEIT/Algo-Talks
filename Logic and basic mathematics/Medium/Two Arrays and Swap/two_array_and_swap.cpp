#include <bits/stdc++.h>
using namespace std;
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    long long int t;
    cin>>t;
    while(t--){
        long long int n,k;
        cin>>n>>k;
        long long int a[n],b[n];
        for(long long int i=0;i<n;i++){
            cin>>a[i];
        }
        sort(a, a+n); 
        for(long long int i=0;i<n;i++){
            cin>>b[i];
        }
        sort(b, b+n, greater<int>()); 
        for(long long int i=0;i<k;i++){
            if(a[i]<b[i]){
                swap(a[i], b[i]);
            }
            else{
                break;
            }
        }
        long long int sum=0;
        for(long long int i=0;i<n;i++){
            sum=sum+a[i];
        }
        cout<<sum<<"\n";
    }
    return 0;
}