cmake_minimum_required(VERSION 3.14)
project(libpcap_demo)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_FLAGS "-lpcap")


add_executable(libpcap_demo main.cpp)