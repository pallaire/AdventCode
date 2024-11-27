#include <string>
#include <vector>
#include <filesystem>

using namespace std;

class AdventDay
{
public:
	static const unsigned int kRunData = 1;
	static const unsigned int kTestData = 2;

	static const unsigned int kPart1 = 1;
	static const unsigned int kPart2 = 2;

	AdventDay(string path);
	virtual ~AdventDay();

	virtual void part1(vector<string> lines);
	virtual void part2(vector<string> lines);

	void printHeader(unsigned int partNumber, unsigned int dataType);
	long long run(unsigned int partNumber);
	long long runAll();
	void test(unsigned int partNumber, unsigned int testID);
	void testAll(unsigned int testCount);

protected:
	unsigned int day;
	filesystem::path dirPath;

	vector<string> loadData(unsigned int dataType, unsigned int dataSequence);
};
