#include <iostream>
#include <map>
#include <string>
#include <vector>

#include "utils.hpp"

#include "Days.hpp"

Day01::Day01(string path) : AdventDay(path) {
    day = 1;
    title = "Historian Hysteria";
}

void Day01::part1(vector<string> lines) {
  vector<long> left, right;

  for(const string& line : lines) {
      vector<long> lr = extractLongs(line);
      left.push_back(lr[0]);
      right.push_back(lr[1]);
  }

  sort(left.begin(), left.end());
  sort(right.begin(), right.end());

  long res = 0;
  for(unsigned int i = 0; i < left.size(); i++) {
    res += abs(left[i] - right[i]);
  }

  printLongResult(res);
}

void Day01::part2(vector<string> lines) {
  vector<long> left;
  map<long, long> rightCount;

  for(const string& line : lines) {
      vector<long> lr = extractLongs(line);

    left.push_back(lr[0]);

    long right = lr[1];

    if(rightCount.contains(right)) {
      rightCount[right]++;
    } else {
      rightCount[right] = 1;
    }
  }

  long res = 0;
  for(const long& l : left) {
    if(rightCount.contains(l)) {
      res += l * rightCount[l];
    }
  }

  printLongResult(res);
}
