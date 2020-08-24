#include <bits/stdc++.h>
#define ll long long
using namespace std;
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    ll arr[] = { 0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1 };
    ll n = *(&arr + 1) - arr; 
    stack<ll>st;
    ll area=0,i=0;
    while(i<n){
        while(!st.empty() && arr[i] > arr[st.top()]){
            ll top = st.top();
            st.pop();
            if(st.empty()){
                break;
            }
            ll width = i-st.top()-1;
            ll height = min(arr[i],arr[st.top()])-arr[top];
            area += width*height;
        }
        st.push(i);
        i++;
    }
    cout<<area;
    return 0;
}