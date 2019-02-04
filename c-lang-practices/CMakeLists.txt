cmake_minimum_required(VERSION 3.13)
project(argv_test)
project(ismdeep_log_test)
project(ismdeep_util_test)
project(ismdeep_time_test)
project(ismdeep_argv_test)

set(EXECUTABLE_OUTPUT_PATH "bin")
set(CMAKE_C_STANDARD 99)

include_directories("include")

add_executable(argv_test src/argv_test.c)
add_executable(ismdeep_log_test test/ismdeep_log_test.c)
add_executable(ismdeep_util_test test/ismdeep_util_test.c)
add_executable(ismdeep_time_test test/ismdeep_time_test.c)
add_executable(ismdeep_argv_test test/ismdeep_argv_test.c)