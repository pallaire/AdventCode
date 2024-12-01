#include <chrono>
#include <cstdlib>
#include <format>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include "utils.hpp"

#include "AdventDay.hpp"

using namespace std;

AdventDay::AdventDay(string path)
{
	day = 0;
	title = "NA interface class";
	dirPath = path;
}

AdventDay::~AdventDay()
{
}

void AdventDay::printHeader(unsigned int partNumber, unsigned int dataType)
{
	if (day == 0)
	{
		cout << "ERROR, you are trying to run an Advent Code Day that hasn't been initialized properly" << endl;
	}
	else
	{
		cout << endl << "Advent Code 2024 - Day " << day << " - " << (dataType == AdventDay::kRunData ? "RUNNING" : "TESTING") << " - Part " << partNumber << endl << "---  " << title << "  ---" << endl << endl; 
	}
}

void AdventDay::printLongResult(long res)
{
	cout << "\x1B[30m\x1B[102m   Result: " << res << "   \033[0m" << endl << endl;
}

void AdventDay::part1(vector<string> /*lines*/)
{
	cout << "ERROR - Part 1 is not implemented" << endl;
}

void AdventDay::part2(vector<string> /*lines*/)
{
	cout << "ERROR - Part 2 is not implemented" << endl;
}

long long AdventDay::run(unsigned int partNumber)
{
	printHeader(partNumber, AdventDay::kRunData);
	vector<string> lines = loadData(AdventDay::kRunData, 1);

	auto startClock = chrono::high_resolution_clock::now();
	switch (partNumber)
	{
	case AdventDay::kPart1:
		part1(lines);
		break;
	case AdventDay::kPart2:
		part2(lines);
		break;
	default:
		cout << "ERROR - Invalid part number ( " << partNumber << " )" << endl;
		break;
	}
	long long delta = chrono::duration_cast<chrono::microseconds>(chrono::high_resolution_clock::now() - startClock).count();
	printRunTime(delta);
	return delta;
}

long long AdventDay::runAll()
{
	long long totalDelta = 0;
	totalDelta = run(AdventDay::kPart1);
	totalDelta += run(AdventDay::kPart2);
	cout << endl << "TOTAL run time" << endl << "---------------" << endl;
	printRunTime(totalDelta);
	return totalDelta;
}

void AdventDay::test(unsigned int partNumber, unsigned int testID)
{
	printHeader(partNumber, AdventDay::kTestData);
	vector<string> lines = loadData(AdventDay::kTestData, testID);
	switch (partNumber)
	{
	case AdventDay::kPart1:
		part1(lines);
		break;
	case AdventDay::kPart2:
		part2(lines);
		break;
	default:
		cout << "ERROR - Invalid part number ( " << partNumber << " )" << endl;
		break;
	}
}

void AdventDay::testAll(unsigned int testCount)
{
	for (unsigned int i = 1; i <= testCount; i++)
	{
		test(AdventDay::kPart1, i);
		test(AdventDay::kPart2, i);
	}
}

vector<string> AdventDay::loadData(unsigned int dataType, unsigned int dataSequence)
{
	filesystem::path filename(format("day{:02}{}{:02}.txt", day, (dataType == AdventDay::kRunData) ? "data" : "test", dataSequence));
	filesystem::path path = dirPath / filename;
	ifstream inputFile(path);

	if (inputFile.is_open() == false)
	{
		cout << "ERROR file error could not open file : " << path << endl;
		exit(EXIT_FAILURE);
	}

	string line;
	vector<string> lines;
	while (getline(inputFile, line))
	{
		lines.push_back(line);
	}

	return lines;
}
