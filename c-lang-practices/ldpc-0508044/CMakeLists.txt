cmake_minimum_required(VERSION 3.13)
project(test_generate_matrix C)
project(ldpc_0508044 C)

include_directories("./include")

set(CMAKE_C_STANDARD 11)

add_executable(test_generate_matrix test_generate_matrix.c)
add_executable(ldpc_0508044 ldpc-0508044.c)