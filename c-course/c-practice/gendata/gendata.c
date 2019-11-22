/*
Usage: gendata [min=1] [max=100] [seed=1] [count=10] [output-count=1]
Default:
	min=1
	max=10
	seed=-1
	count-min=10
    count-max=10
	output-count=1
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

/* 简单字符串搜索 */
int str_find(const char *str, const char *p) {
	int len_str = strlen(str);
	int len_p   = strlen(p);
	for(int i = 0; i <= len_str - len_p; i++) {
		bool found = true;
		for (int j = 0; found && j < len_p; j++) {
			if (str[i+j] != p[j]) {
				found = false;
			}
		}
		if (found) {
			return i;
		}
	}
	return -1;
}

/* 根据 = 进行字符串拆分成两个 */
char **split(const char *str) {
    char **list = (char **) malloc(2 * sizeof(char *));

    int index   = str_find(str, "=");
    if (index < 0) {
        list[0] = malloc(2 * sizeof(char));
        list[1] = malloc(2 * sizeof(char));
        memset(list[0], 0, 2 * sizeof(char));
        memset(list[1], 0, 2 * sizeof(char));
        return list;
    }

    int len_str = strlen(str);
    char *l = malloc(len_str * sizeof(char));
    char *r = malloc(len_str * sizeof(char));
    memset(l, 0, len_str * sizeof(char));
    memset(r, 0, len_str * sizeof(char));

    for (int i = 0; i < index; i++) {
        l[i] = str[i];
    }

    for (int i = index + 1; i < len_str; i++) {
        r[i - index - 1] = str[i];
    }

    list[0] = l;
    list[1] = r;

    return list;
}

/* 参数列表处理函数 */
char *parse_args(int argc, const char *argv[], const char *key) {
    for (int i = 1; i < argc; i++) {
        char **list = split(argv[i]);
        if (strcmp(list[0], key) == 0) {
            return list[1];
        }
    }
    return "";
}

/* 字符串转整数类型，如果字符串为空则返回default_value */
int parse_int(const char *str, int default_value) {
    if (strcmp(str, "") == 0) {
        return default_value;
    }
    int v;
    sscanf(str, "%d", &v);
    return v;
}

int main(int argc, const char *argv[]) {
    int min_value    = parse_int(parse_args(argc, argv, "min"         ),  1);
    int max_value    = parse_int(parse_args(argc, argv, "max"         ), 10);
    int seed         = parse_int(parse_args(argc, argv, "seed"        ), -1);
    int count_min    = parse_int(parse_args(argc, argv, "count-min"   ), 10);
    int count_max    = parse_int(parse_args(argc, argv, "count-max"   ), 10);
    int output_count = parse_int(parse_args(argc, argv, "output-count"),  1);
    
    /* 设置随机种子 */
    if (seed == -1) {
        srand((unsigned)time(NULL));
    }else{
        srand(seed);
    }

    /* 随机产生随机数量 */
    int count = rand() % (count_max - count_min + 1) + count_min;

    /* 根据output-count标记判定是否需要输出变量count的值 */
    if (1 == output_count) {
        printf("%d\n", count);
    }

    /* 输出 count 个随机数 */
    for (int i = 0; i < count; i++) {
        printf("%d ", + rand() % (max_value - min_value + 1) + min_value);
    }

    printf("\n");

	return 0;
}

