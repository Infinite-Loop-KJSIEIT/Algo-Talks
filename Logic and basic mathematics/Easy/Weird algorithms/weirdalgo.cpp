#include <bits/stdc++.h>
using namespace std;
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    long long int n;
    cin>>n;
    cout<<n<<" ";
    while(n!=1){
	    if((n%2)!=0){
		    n=(n*3)+1;
		    cout<<n<<" "; 	
		}
	    else{
		    n=n/2;
		    cout<<n<<" ";
        }
	}
    return 0;
}