#ifndef __UTILS__
#define __UTILS__

#include <chrono>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

// Time functions
void printRunTime(long us);

// String functions
vector<string> split(string toparse, string delimiter);
vector<long> extractLongs(string toparse); 


#endif // __UTILS__
