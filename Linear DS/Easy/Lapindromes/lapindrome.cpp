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
        string str,str1,str2;
        cin>>str;
        int n=str.length();
        if(n%2==0){
            str1=str.substr(0,n/2);
            str2=str.substr(n/2,n/2);
        }
        else{
            str1=str.substr(0,n/2);
            str2=str.substr((n/2)+1,n/2);
        }
        sort(str1.begin(),str1.end());
        sort(str2.begin(),str2.end());
        if(str1==str2){
            cout<<"YES"<<"\n";
        }
        else{
            cout<<"NO"<<"\n";
        }
    }
    return 0;
}