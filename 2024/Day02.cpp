#include <iostream>
#include <map>
#include <string>
#include <vector>

#include "utils.hpp"

#include "Days.hpp"

Day02::Day02(string path) : AdventDay(path) {
    day = 2;
    title = "Red-Nosed Reports";
}

long Day02::isGoodReport(const vector<long> report) {
    int dir = 0;
    for(unsigned int i = 1; i < report.size(); i++) {
      long delta = report[i] - report[i-1];

      if(delta==0 || abs(delta) > 3) {
        // bad step
        return 0;
      }

      int currentDir = delta<0 ? -1 : 1;
      if(dir==0) {
        dir = currentDir;
      } else if(dir != currentDir) {
        // change of direction
        return 0;
      }
    }
    return 1;
}

void Day02::part1(vector<string> lines) {
  long safeReport = 0;

  for(auto line : lines) {
    vector<long> report = extractLongs(line);
    safeReport += isGoodReport(report);
  }

  printLongResult(safeReport);
}

void Day02::part2(vector<string> lines) {
  long safeReport = 0;

  for(auto line : lines) {
    vector<long> report = extractLongs(line);

    long current = isGoodReport(report);

    if(current == 1) {
      safeReport++;
    } else {
      for(unsigned int i = 0; i < report.size(); i++) {
        vector<long> reportCopy(report);
        reportCopy.erase(reportCopy.begin() + i);
        if(isGoodReport(reportCopy)) {
          safeReport++;
          break;
        }
      }
    }
  }

  printLongResult(safeReport);
}

