#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>
using namespace std;
int a[300];
int b[300];
int main(){
    int n,k;
    cin >> n>>k;
    int x;
    memset(a,0,sizeof(a));
    for(int i = 0 ;i < n ;i++){
        cin >> x;
        if(x < k){
            b[x%k]++;
        } else{
            a[x%k]++;
        }
    }
    if(a[0]%2)
        a[0]--;
    int ans = a[0];
    for(int i = 1; i <k;i++){
        ans += min(a[i],a[k -i]);
    }
    for(int )
    cout << ans << endl;

}