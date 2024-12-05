#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>

#include "Days.hpp"
#include "utils.hpp"

static map<long, vector<long>> grules;

static bool comp(long a, long b) {
  if (grules.contains(a)) {
    if (find(grules[a].begin(), grules[a].end(), b) != grules[a].end()) {
      return true;
    }
  }

  if (grules.contains(b)) {
    if (find(grules[b].begin(), grules[b].end(), a) != grules[b].end()) {
      return false;
    }
  }

  return a < b;
}

Day05::Day05(string path) : AdventDay(path) {
  day = 5;
  title = "Print Queue";
}

bool Day05::isValid(const vector<long>& nums) {
  set<long> seen;
  for (auto n : nums) {
    // does this update number has grules?
    if (grules.contains(n)) {
      // check all the grules numbers
      for (auto r : grules[n]) {
        if (seen.contains(r)) {
          return false;
        }
      }
    }
    seen.insert(n);
  }
  return true;
}

long Day05::updates(const vector<string>& lines, bool workOnOutOfOrder) {
  long res = 0;

  bool isrule = true;
  grules.clear();

  for (const string& line : lines) {
    if (line.length() == 0) {
      isrule = false;
      continue;
    }

    // Parse input line into longs
    vector<long> nums = extractLongs(line);

    if (isrule) {
      grules[nums[0]].push_back(nums[1]);
    } else {
      if (workOnOutOfOrder) {
        if (isValid(nums) == false) {
          sort(nums.begin(), nums.end(), comp);
          res += nums[nums.size() >> 1];
        }
      } else {
        if (isValid(nums)) {
          res += nums[nums.size() >> 1];
        }
      }
    }
  }

  return res;
}

void Day05::part1(vector<string> lines) {
  printLongResult(updates(lines, false));
}

void Day05::part2(vector<string> lines) {
  printLongResult(updates(lines, true));
}
