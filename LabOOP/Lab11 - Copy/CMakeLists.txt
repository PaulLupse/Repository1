cmake_minimum_required(VERSION 4.0)
project(Lab11)

add_definitions(-DUNICODE -D_UNICODE)

set(CMAKE_CXX_STANDARD 14)

include_directories(Header)
add_executable(Lab11 main.cpp
        Source/Student.cpp
        Header/Student.h
        Header/CSVReader.h
        Source/CSVReader.cpp
        Header/ListaStudenti.h
        Source/ListaStudenti.cpp)
