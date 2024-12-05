#ifndef __DAYS__
#define __DAYS__

#include <map>
#include <string>
#include <vector>
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

class Day05 : public AdventDay {
  public:
    Day05(string path);
    void part1(vector<string> lines);
    void part2(vector<string> lines);
  private:
    bool isValid(const vector<long>& nums);
    long updates(const vector<string>& lines, bool workOnOutOfOrder);
};

#endif //__DAYS__
