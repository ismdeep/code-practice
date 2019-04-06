cmake_minimum_required(VERSION 3.13)
project(get_pid)
project(fork_test)

set(CMAKE_C_STANDARD 99)

add_executable(get_pid get_pid.c)
add_executable(fork_test fork_test.c)