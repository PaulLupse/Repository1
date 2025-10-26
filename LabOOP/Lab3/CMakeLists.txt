cmake_minimum_required(VERSION 4.0)
project(Lab3)

set(CMAKE_CXX_STANDARD 14)

include_directories(Header)
add_executable(Lab3 main.cpp
        Source/Student.cpp
        Header/Student.h
        Header/CSVReader.h
        Source/CSVReader.cpp
        Header/ListaStudenti.h
        Source/ListaStudenti.cpp)
