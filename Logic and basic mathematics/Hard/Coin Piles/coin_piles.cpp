#include <bits/stdc++.h>
using namespace std;
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    long long int t;
    cin>>t;
    while(t--){
        long long int a,b;
        cin>>a>>b;
        if(a>b){
            swap(a, b);
        }
        if((2*a)<b){
            cout<<"NO"<<"\n";
        }
        else {
            a=a%3;
            b=b%3;
            if((a==0 && b==0) || (a==1 && b==2) || (a==2 && b==1)){
                cout<<"YES"<<"\n";
            }
            else{
                cout<<"NO"<<"\n";
            }
        }
    }
    return 0;
}