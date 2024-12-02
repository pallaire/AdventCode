#ifndef __DAYS__
#define __DAYS__

#include <string>
#include "AdventDay.hpp"

class Day01 : public AdventDay {
  public:
    Day01(string path);
    void part1(vector<string> lines);
    void part2(vector<string> lines);
};


class Day02 : public AdventDay {
  public:
    Day02(string path);
    void part1(vector<string> lines);
    void part2(vector<string> lines);
  private:
    long isGoodReport(const vector<long> report);
};

#endif //__DAYS__
