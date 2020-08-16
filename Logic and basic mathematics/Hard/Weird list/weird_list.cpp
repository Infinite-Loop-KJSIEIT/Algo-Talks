#include <bits/stdc++.h> 
using namespace std; 

int main(){

    ios_base::sync_with_stdio(false); 
    cin.tie(NULL); 
  
// #ifndef ONLINE_JUDGE 
//     freopen("input.txt", "r", stdin); 
//     freopen("error.txt", "w", stderr); 
//     freopen("output.txt", "w", stdout); 
// #endif 
    int t;
    cin >> t;
    while(t--){
        int n, i, index,q;
        double a, b, c, m;
        string s;
        cin >> n;
        cin >> a >> b >> c;
        int * arr = new int[10];
        for(i=0; i<10; i++){
            arr[i] = -1;
        }
        vector<int> v;
        v.push_back(n);
       
        while(1){
           
            if(n  < 10){
                if(arr[n] !=-1){
                    break;
                }else{
                    arr[n] = v.size();
                }
            }
            
            m = ((double)n)/a;
            s = to_string(m);
            
            for(int i = 0; i < s.length(); i++){
                if(s[i] == '.'){
                    if(s[i+1] == '0'){
                        n = (int)s[0] - 48;
                    }
                    else{
                        n = (int)s[i+1] - 48;
                    }
                }
            }
            
            v.push_back(n);
            m = ((double)n)/b;
            s = to_string(m);
            
            for(int i = 0; i < s.length(); i++){
                if(s[i] == '.'){
                    if(s[i+1] == '0'){
                        n = (int)s[0] - 48;
                    }
                    else{
                        n = (int)s[i+1] - 48;
                    }
                }
            }
            
            v.push_back(n);
            m = ((double)n)/c;
            s = to_string(m);;
            for(int i = 0; i < s.length(); i++){
                if(s[i] == '.'){
                    if(s[i+1] == '0'){
                        n = (int)s[0] - 48;
                    }
                    else{
                        n = (int)s[i+1] - 48;
                    }
                }
            }
            
            v.push_back(n);
            
        }
        int * new_arr = new int[arr[n]];
        int * repeat = new int[v.size() - arr[n]];
        for(i =0 ; i < arr[n]; i++){
                new_arr[i] = v[i];
        }
        int count = 0;
        for(i = arr[n]; i < v.size(); i++){
            repeat[i - arr[n]] = v[i];
            count++;
        }
        cin >> q;
        while(q--){
                cin >> index;
                if(index < arr[n]){
                    cout << new_arr[index] << endl;
                }
                else{
                    index -= arr[n];
                    cout << repeat[index%count] << endl;
                }
        }
    }
    return 0;
}
