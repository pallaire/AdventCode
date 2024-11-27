#include <chrono>
#include <iostream>

using namespace std;

void printRunTime(long long us) {
    if(us < 1000) {
        cout << "Run time: " << us << "µs" << std::endl;
    } else if(us < 1000000) {
        cout << "Run time: " << us/1000.0 << "ms" << std::endl;
    } else {
        cout << "Run time: " << us/1000000.0 << "s" << std::endl;
    }
}