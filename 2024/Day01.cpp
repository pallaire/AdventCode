#include <iostream>
#include <string>

#include "Days.hpp"

Day01::Day01(string path) : AdventDay(path) {
    day = 1;
}

void Day01::part1(vector<string> lines) {

    for(const string& line : lines) {
        cout << ">" << line << "<" << std::endl;
    }

}

void Day01::part2(vector<string> lines) {
    
}
