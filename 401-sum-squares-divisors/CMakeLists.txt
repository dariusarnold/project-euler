cmake_minimum_required(VERSION 3.10)
project(401-sum-squares-divisors)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_FLAFS "-Wall -Wextra")
set(CMAKE_CXX_FLAGS "-fconstexpr-loop-limit=1000000000")
set(CMAKE_CXX_FLAGS_DEBUG "-g")
set(CMAKE_CXX_FLAGS_RELEASE "-O3")

add_executable(main main.cpp)