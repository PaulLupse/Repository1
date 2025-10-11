cmake_minimum_required(VERSION 4.0)
project(Lab2)

set(CMAKE_CXX_STANDARD 17)

include_directories(header)
add_executable(Lab2 main.cpp
        header/CSVReader.h
        header/Sorter.h
        header/Student.h
        source/CSVReader.cpp
        source/Sorter.cpp
        source/Student.cpp)
