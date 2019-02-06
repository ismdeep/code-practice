#include <iostream>
#include <cstring>
#include <string>
#include <algorithm>
using namespace std;

bool cmp_str(string a, string b) {
    return a > b;
}

string out_str[100000];
string usr_str[100000];

int main(int argc,char* args[]) {
    FILE * f_in   = fopen(args[1], "r"); //测试输入
    FILE * f_out  = fopen(args[2], "r"); //测试输出
    FILE * f_user = fopen(args[3], "r"); //用户输出
    int ret = 0;
    int n;
    char tmp[1024];
    fscanf(f_in, "%d", &n);
    int line_cnt = 1;
    for (int i = 1; i <= n; ++i) {
        line_cnt *= i;
    }

    for (int i = 0; i < line_cnt; ++i) {
        fgets(tmp, 1024, f_out);
        string tmp_str(tmp);
        out_str[i] = tmp_str;
    }
    for (int i = 0; i < line_cnt; ++i) {
        fgets(tmp, 1024, f_out);
        string tmp_str(tmp);
        usr_str[i] = tmp_str;
    }

    sort(out_str, out_str + line_cnt, cmp_str);
    sort(usr_str, usr_str + line_cnt, cmp_str);

    bool flag = true;
    for (int i = 0; i < line_cnt; ++i) {
        if (out_str[i] != usr_str[i]) {
            cout << out_str[i] << endl << usr_str[i] << endl << endl;
            flag = false;
        }
    }

    cout << flag << endl;

    return 0;
}