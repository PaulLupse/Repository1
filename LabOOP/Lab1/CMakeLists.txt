cmake_minimum_required(VERSION 4.0)
project(Lab1)

set(CMAKE_CXX_STANDARD 17)

include_directories(Header)

add_executable(Lab1 main.cpp
        Source/Sorting.cpp
        Header/Sorting.h)

