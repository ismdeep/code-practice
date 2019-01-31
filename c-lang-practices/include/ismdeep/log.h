//
// Created by ismdeep on 2019-01-31.
//

#ifndef ISMDEEP_LOG_H
#define ISMDEEP_LOG_H

#include <time.h>
#include <stdarg.h>
#include <string.h>
#include <stdint.h>

#define LOG_LEVEL_INFO 0
#define LOG_LEVEL_ERR  1
#define LOG_LEVEL_WARN 2

char* log_level_arr[] = {"INFO", "ERROR", "WARN"};

void write_log(char * log_file_path, int log_level, char * tag, const char *fmt, ...) {
    FILE * fp = fopen(log_file_path, "at");
    time_t timep;
    struct tm *p;
    time(&timep);
    p = localtime(&timep);
    char str[50];
    sprintf(str, "%04d-%02d-%02d %02d:%02d:%02d",
            p->tm_year + 1900,
            p->tm_mon + 1,
            p->tm_mday,
            p->tm_hour,
            p->tm_min,
            p->tm_sec);
    va_list ap;
    char buffer[4096];
    va_start(ap, fmt);
    vsprintf(buffer, fmt, ap);
    printf("[%s][%s][%s] %s\n", str, log_level_arr[log_level], tag, buffer);
    fprintf(fp, "[%s][%s][%s] %s\n", str, log_level_arr[log_level], tag, buffer);
    va_end(ap);
    fclose(fp);
}

#endif //ISMDEEP_LOG_H
