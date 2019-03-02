//
// Created by ismdeep on 2019-01-31.
//

#ifndef ISMDEEP_LOG_H
#define ISMDEEP_LOG_H

#include <time.h>
#include <stdarg.h>
#include <stdbool.h>
#include <string.h>
#include <stdint.h>

#define LOG_INFO 0
#define LOG_ERR  1
#define LOG_WARN 2

char* log_level_arr[] = {"INFO", "ERROR", "WARN"};
extern char *log_file_path = "log.log";
extern char *log_tag = "log";
extern bool log_with_stdout = false;

void write_log(int log_level, const char *fmt, ...) {
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
    if (log_with_stdout) {
        printf("[%s][%s][%s] %s\n", str, log_level_arr[log_level], log_tag, buffer);
    }
    fprintf(fp, "[%s][%s][%s] %s\n", str, log_level_arr[log_level], log_tag, buffer);
    va_end(ap);
    fclose(fp);
}

#endif //ISMDEEP_LOG_H
