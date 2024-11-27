cmake_minimum_required(VERSION 3.10)
project(AdventCode2024)

set(CMAKE_COLOR_MAKEFILE ON)
set(CMAKE_COLOR_DIAGNOSTICS ON) 

# Set the compiler and standard
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -g -Wall -Wextra -pedantic") 

# Find all source files recursively
file(GLOB SOURCE_FILES "*.c" "*.cpp" "*.h" "*.hpp")

# Add the source files to the executable target
add_executable(ac2024 ${SOURCE_FILES})
