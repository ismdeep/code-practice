cmake_minimum_required(VERSION 3.14)
project(server C)
project(client C)
project(client2 C)
#project(udp_demo C)

set(CMAKE_C_STANDARD 11)

add_executable(server server.c)
add_executable(client client.c)
add_executable(client2 client2.c)
