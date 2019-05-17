cmake_minimum_required(VERSION 3.14)
project(init C)
project(key_gen C)
project(test C)
project(decrypt C)

set(CMAKE_C_STANDARD 11)

include_directories("./include")

add_executable(init init.c include/matrix.c include/mceliece.c include/qc_mdpc.c include/utility.c)
add_executable(keygen key_gen.c include/qc_mdpc.c include/matrix.c include/utility.c)
add_executable(test test.c include/matrix.c include/mceliece.c include/qc_mdpc.c include/utility.c)
add_executable(decrypt decrypt.c include/matrix.c include/mceliece.c include/qc_mdpc.c include/utility.c)
add_executable(encrypt encrypt.c include/matrix.c include/mceliece.c include/qc_mdpc.c include/utility.c)