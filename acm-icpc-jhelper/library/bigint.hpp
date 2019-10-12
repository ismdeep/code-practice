class BigInt { //无符号整数高精度
#define MAXDIGIT 10000 //最大为10^MAXDIGIT
#define BIGINTMOD 10000 //压4位
private:
public:
    int n;        //a中n位有效
    int a[MAXDIGIT / 4 + 10]; //压4位，下标从1开始（且高位不一定为0）
    //初始化
    BigInt();      //默认设置为0
    BigInt(long long x); //设置为x
    BigInt(char *s);   //数字字符串
    BigInt(std::string str); // 数字字符串
    ~BigInt() {}

    //初始化
    int set(long long x);

    int set(char *s);

    // 显示
    int Display();   //输出,没有换行
    int trim();     //去除前缀0

    // ToString
    std::string ToString(); // ToString()


    BigInt &operator=(BigInt &bnum);

    //(1)单目加法
    int operator+=(BigInt &bnum);

    int operator+=(int bnum);

    //(2)除法
    int operator/=(int bnum); //返回值为mod bnum的值。

    int mod(int bnum);
};

//操作符重载
// (3)乘法
int operator*=(BigInt &anum, BigInt &bnum);

BigInt &operator*(BigInt &anum, BigInt &bnum);

// (4)取模
int operator%(BigInt &anum, int bnum);

// (5)双目加法
BigInt &operator+(BigInt &anum, BigInt &bnum); //中间变量使用静态变量
// (6)比较
bool operator<(BigInt &anum, BigInt &bnum);

bool operator>(BigInt &anum, BigInt &bnum);

bool operator==(BigInt &anum, BigInt &bnum);


//implementation
BigInt::BigInt() {
    set(0ll);
}

BigInt::BigInt(long long x) {
    set(x);
}

BigInt::BigInt(char *s) {
    set(s);
}

BigInt::BigInt(std::string str) {
    char *s = (char *) malloc(sizeof(char) * str.length() + 1);
    s[str.length()] = '\0';
    for (int i = 0; i < str.length(); i++) {
        s[i] = str[i];
    }
    set(s);
}

int BigInt::set(long long x) {
    n = 0;
    do {
        a[++n] = x % BIGINTMOD;
        x /= BIGINTMOD;
    } while (x);
    return 0;
}

int BigInt::set(char *s) {
    n = 0;
    int len = strlen(s) - 1;
    while (len >= 0) {
        int digits = len + 1 > 4 ? 4 : len + 1; //最多选择4位
        int num = 0;
        for (int i = len - digits + 1; i <= len; i++)
            num = num * 10 + s[i] - '0';
        a[++n] = num;
        len -= digits;
    }
    trim(); //前缀0删去
    return 0;
}

int BigInt::Display() {
    printf("%d", a[n]);
    for (int i = n - 1; i >= 1; i--) printf("%04d", a[i]);
    return 0;
}

int BigInt::trim() {
    while (n > 1 && a[n] == 0) {
        n--;
    }
    return 0;
}

std::string BigInt::ToString() {
    std::string ans;
    char ch[10];
    sprintf(ch, "%d", a[n]);
    ans += ch;
    for (int i = n - 1; i >= 1; i--) {
        sprintf(ch, "%04d", a[i]);
        ans += ch;
    }
    return ans;
}


BigInt &BigInt::operator=(BigInt &bnum) {
    n = bnum.n;
    for (int i = 1; i <= n; i++)a[i] = bnum.a[i];
    return bnum;
}

int BigInt::operator+=(BigInt &bnum) {
    n = std::max(n, bnum.n);
    int x = 0;
    for (int i = 1; i <= n; i++) {
        a[i] = a[i] + bnum.a[i] + x;
        x = a[i] / BIGINTMOD;
        a[i] %= BIGINTMOD;
    }
    a[++n] = x;
    trim();
    return 0;
}

int BigInt::operator+=(int bnum) {
    a[1] += bnum;
    int idx = 1;
    while (a[idx] >= BIGINTMOD) {
        a[idx + 1] += a[idx] / BIGINTMOD;
        a[idx] %= BIGINTMOD;
        idx++;
    }
    n = std::max(n, idx);
    return 0;
}

int operator*=(BigInt &cnum, BigInt &bnum) {     //cnum*=bnum
    static BigInt anum;
    anum = cnum;
    //cnum=anum*bnum
    for (int i = anum.n + 1; i <= bnum.n; i++) anum.a[i] = 0;
    for (int i = bnum.n + 1; i <= anum.n; i++) bnum.a[i] = 0;
    cnum.n = anum.n + bnum.n;
    for (int i = 1; i <= cnum.n; i++) cnum.a[i] = 0;
    //
    for (int i = 1; i <= anum.n; i++) {
        int x = 0;
        for (int j = 1; j <= bnum.n; j++) {
            cnum.a[i + j - 1] += anum.a[i] * bnum.a[j] + x;
            x = cnum.a[i + j - 1] / BIGINTMOD;
            cnum.a[i + j - 1] %= BIGINTMOD;
        }
        cnum.a[i + bnum.n] += x;
    }
    cnum.trim();
    return 0;
}

BigInt &operator*(BigInt &anum, BigInt &bnum) { //cnum=anum*bnum
    static BigInt cnum;
    cnum = anum;
    cnum *= bnum;
    return cnum;
}

//操作符重载
int operator%(BigInt &anum, int bnum) { //a%b
    int x = 0;
    for (int i = anum.n; i >= 1; i--) {
        x = (x * BIGINTMOD + anum.a[i]) % bnum;
    }
    return x;
}

int BigInt::operator/=(int bnum) {
    int x = 0;
    for (int i = n; i >= 1; i--) {
        int tmp = x * BIGINTMOD + a[i];
        a[i] = tmp / bnum;
        x = tmp % bnum;
    }
    trim();
    return x;
}

int BigInt::mod(int bnum) {
    int x = 0;
    for (int i = n; i >= 1; i--) {
        int tmp = x * BIGINTMOD + a[i];
        x = tmp % bnum;
    }
    return x;
}


BigInt &operator+(BigInt &anum, BigInt &bnum) {
    static BigInt cnum;                //静态函数加速
    cnum.n = std::max(anum.n, bnum.n);
    for (int i = anum.n + 1; i <= cnum.n; i++)anum.a[i] = 0;
    for (int i = bnum.n + 1; i <= cnum.n; i++)bnum.a[i] = 0;
    int x = 0;
    for (int i = 1; i <= cnum.n; i++) {
        cnum.a[i] = anum.a[i] + bnum.a[i] + x;
        x = cnum.a[i] / BIGINTMOD;
        cnum.a[i] %= BIGINTMOD;
    }
    cnum.a[++cnum.n] = x;
    cnum.trim();
    return cnum;
}

bool operator<(BigInt &anum, BigInt &bnum) { //实现<
    anum.trim();
    bnum.trim();
    if (anum.n > bnum.n) return false;
    if (anum.n < bnum.n) return true;
    for (int i = anum.n; i >= 1; i--) {
        if (anum.a[i] > bnum.a[i]) return false;
        if (anum.a[i] < bnum.a[i]) return true;
    }
    return false;
}

bool operator>(BigInt &anum, BigInt &bnum) { // anum>bnum 等价于 bnum<anum
    return bnum < anum;
}

bool operator==(BigInt &anum, BigInt &bnum) { // anum==bnum 等价于 anum<>bnum
    return (!(anum < bnum) && !(anum > bnum));
}
