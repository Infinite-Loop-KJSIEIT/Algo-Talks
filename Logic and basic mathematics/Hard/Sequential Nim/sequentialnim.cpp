#include<bits/stdc++.h>
#define ll long long int
using namespace std;
int main()
{
    ll t;
    cin>>t;
    while(t--)
    {
        ll i, j, n;
        bool ans = true;
        cin >> n;
        ll a[n];
        for (i = 0; i < n;i++)
        {
            cin >> a[i];
        }
        for (i = 0; i < n;i++)
        {
            if(a[i]==1)
            {
                ans = !ans;
            }
            else{
                ans = !ans;
                break;
            }
        }
        if(ans==false)
        {
            cout<<"First\n";
        }
        else{
            cout << "Second\n";
        }
    }
    return 0;
}