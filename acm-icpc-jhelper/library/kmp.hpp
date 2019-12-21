
class KMP{
    string main_str;
    string pattern;
    int *next;
    void get_next();
public:
    void set_pattern(string str);
    void set_main_string(string str);
    int get_pattern_in_main();
    string get_pattern();
};

void KMP::set_pattern(string str) {
    this->pattern = str;
    this->get_next();
}

void KMP::set_main_string(string str) {
    this->main_str = str;
}

void KMP::get_next() {
    int p_len = this->pattern.length();
    int i = 0;   // P 的下标
    int j = -1;
    this->next = (int *) malloc(p_len * sizeof(int));
    next[0] = -1;

    while (i < p_len - 1)
    {
        if (j == -1 || this->pattern[i] == this->pattern[j])
        {
            i++;
            j++;
            next[i] = j;
        }
        else
            j = next[j];
    }
}

int KMP::get_pattern_in_main() {
    int i = 0;  // S 的下标
    int j = 0;  // P 的下标
    int s_len = this->main_str.length();
    int p_len = this->pattern.length();

    while (i < s_len && j < p_len)
    {
        if (j == -1 || this->main_str[i] == this->pattern[j])  // P 的第一个字符不匹配或 S[i] == P[j]
        {
            i++;
            j++;
        }
        else
            j = next[j];  // 当前字符匹配失败，进行跳转
    }

    if (j == p_len)  // 匹配成功
        return i - j;

    return -1;
}

string KMP::get_pattern() {
    return this->pattern;
}
