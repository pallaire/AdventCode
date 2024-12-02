#include <stdio.h>
#include <iostream>
#include <limits>

#include "Days.hpp"

void runAllDays(const char* dataPath) {
	long long totalDelta = 0;
  
  Day01* d1 = new Day01(dataPath);
  totalDelta += d1->runAll();
  delete d1;

  Day02* d2 = new Day02(dataPath);
  totalDelta += d2->runAll();
  delete d2;

}

int main(int /* argc */, char ** /* argv */)
{
	const char *defaultDataPath = "/home/pallaire/devs/AdventCode/2024/data";

	Day02 d(defaultDataPath);
	d.testAll(1);
	d.runAll();


	return EXIT_SUCCESS;
}
