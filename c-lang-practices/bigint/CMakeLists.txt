cmake_minimum_required(VERSION 3.13)

project(bigint_test)
project(bigint)

set(CMAKE_C_STANDARD 11)
include_directories("./")

add_executable(bigint bigint.c)
add_executable(bigint_test bigint_test.c)
