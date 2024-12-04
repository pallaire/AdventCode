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

class Day03 : public AdventDay {
  public:
    Day03(string path);
    void part1(vector<string> lines);
    void part2(vector<string> lines);
};

class Day04 : public AdventDay {
  public:
    Day04(string path);
    void part1(vector<string> lines);
    void part2(vector<string> lines);

  private:
    unsigned long searchAround(const vector<string>& lines, long w, long h, long x, long y, long dx, long dy, long position);
};

#endif //__DAYS__
