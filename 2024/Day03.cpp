#include <iostream>
#include <regex>
#include <string>

#include "utils.hpp"

#include "Days.hpp"

Day03::Day03(string path) : AdventDay(path) {
    day = 3;
    title = "Mull It Over";
}

void Day03::part1(vector<string> lines) {
  long totalMultiplications = 0;

  // mul(2,4)
  const regex rx("mul\\((\\d+,\\d+)\\)");
  smatch matches;

  for(const string& line : lines) {
    string work(line);
    while(regex_search(work, matches, rx)) {
        vector<long> nums = extractLongs(matches.str(1));
        totalMultiplications += nums[0] * nums[1];

        work = matches.suffix().str();
    }
  }

  printLongResult(totalMultiplications);
}

void Day03::part2(vector<string> lines) {
  long totalMultiplications = 0;

  // mul(2,4)   do()   don't()
  const regex rx("mul\\((\\d+,\\d+)\\)|do\\(\\)|don't\\(\\)");
  smatch matches;

  bool mulDo = true;

  for(const string& line : lines) {
    string work(line);
    while(regex_search(work, matches, rx)) {
      if(matches.str(0).compare("do()") == 0) {
        mulDo = true;
      } else if(matches.str(0).compare("don't()") == 0) {
        mulDo = false;
      } else {
        if(mulDo) {
          vector<long> nums = extractLongs(matches.str(1));
          totalMultiplications += nums[0] * nums[1];
        }
      }

      work = matches.suffix().str();
    }
  }

  printLongResult(totalMultiplications);
}

