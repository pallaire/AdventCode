#include <stdio.h>
#include "Days.hpp"

int main(int /* argc */, char ** /* argv */)
{
	const char *defaultDataPath = "/home/pallaire/devs/AdventCode/2024/data";

	Day01 d(defaultDataPath);
	d.testAll(1);
	d.runAll();

	return EXIT_SUCCESS;
}
