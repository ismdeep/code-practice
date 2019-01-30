cmake_minimum_required(VERSION 3.13)
project(argv_test C)

set(EXECUTABLE_OUTPUT_PATH "bin")
set(CMAKE_C_STANDARD 99)

include_directories("include")

add_executable(argv_test src/argv_test.c)