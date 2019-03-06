#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>
using namespace std;
struct node {
    int l,r;
}p[5005];

bool cmp (node a,node b){
    if(a.l == b.l){
        return a.r < b.r;
    }
    return a.l < b.l;
}


int a[50005];
int main() {
    int n,m;
    cin >> n >> m;
    for(int i = 0 ; i < m ; i++){
        cin >> p[i].l >> p[i].r;
    }
    memset(a,0, sizeof(a));
    int ll = p[0].l,rr = p[0].r;
    for(int i = ll; i <= rr; i++){
        a[i] = 1;
    }
    p[0].l = 0;p[0].r = 0;
    int ans = rr - ll + 1,cnt = 0;
    sort(p,p+m,cmp);
    for(int i = 1; i < m;i++){
        if(p[i].l == ll){
            cnt ++;
            ans += p[i].r - rr ;
            for(int i = rr + 1; i <= p[i].r ;i++){
                a[i] = 1;
            }
            ll = p[i].l; rr = p[i].r;
            p[i].l = 0;p[i].r = 0;
        }else if(p[i].l > rr){
            ans += p[i].r - p[i].l + 1;
            ll = p[i].l;rr = p[i].r;
            p[i].l = 0;p[i].r = 0;
            for(int i = ll; i <=rr;i++ ){
                a[i] = 1;
            }
        }
    }
    sort(p,p + m,cmp);
    int k = 0;
    for(;k < m; k++){
        if(p[k].l != 0)
            break;
    }
    if(k == m){
        cout << ans << endl;
        return 0;
    }
    if(cnt >= 2){
        for(;k < m; k++){
            for(int i = p[k].l ;i <= p[k].r ;i++){
                a[i] = 1;
            }
        }
        int tt = 0;
        for(int i = 1; i <= n; i++){
            if(a[i])
                tt++;
        }
        cout << tt << endl;
    } else {

    }
    /*int k1= 6000,k2 = 6000,tmp = 0;
    for(int i = 0 ;i < m; i++){
        cin >> p[i].l >> p[i].r;
        tmp = p[i].r - p[i].l;
        if(tmp < k1){
            k1 = tmp;
        }else if(tmp < k2){
            k2 = tmp;
        }
    }
    sort(p,p + m,cmp);
    int ans = 0,flag = 0,t1 = 6000,t2 = 6000,ss = 0;
    int ll = p[0].l,rr = p[0].r;
    ans = rr - ll;
    int t = 0;
    int cnt = 0;
    for(int i = 1; i < m; i++){
        if(p[i].l == ll){
            cnt ++;
            ans += p[i].r - rr ;
        }else if(p[i].l <= rr){
            if(p[i].r <= rr){
                cnt++;
                continue;
            }
            ans += p[i].r - rr;
            tmp = min((p[i].r - rr),(p[i].l - ll));
            if(tmp < t1){
                t1 = tmp;
            }else if(tmp < t2){
                t2 = tmp;
            }
        }else{
            ans += p[i].r - p[i].l;
        }
        ll = p[i].l;
        rr = p[i].r;
    }
    if(cnt >= 2){
        cout << ans << endl;
    }else if(cnt >= 0){
        if(t1 != 6000){
            cout << ans -
        }
    }*/
    return 0;
}