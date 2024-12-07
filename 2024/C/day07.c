#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/time.h>

#include "textlines.h"

long long timeInMilliseconds(void) {
    struct timeval tv;
    gettimeofday(&tv,NULL);
    return (((long long)tv.tv_sec)*1000)+(tv.tv_usec/1000);
}

long long concatLongLong(long long a, long long b) {
  // Hardcoded smaller case because the data on the right is usually small
  if (b < 10) {
    return a * 10 + b;
  } else if (b < 100) {
    return a * 100 + b;
  } else if (b < 1000) {
    return a * 1000 + b;
  } else {
    return a * pow(10, floor(log10(b) + 1)) + b;
  }
}

long long compute(long long target, long long value, long long* nums, unsigned long count, unsigned long pos, bool useConcat) {
  if (value > target) {
    return 0;
  }

  long long res = 0;
  long long work = value + nums[pos];
  if (pos == count - 1) {
    if (work == target) {
      return target;
    }
  } else {
    res = compute(target, work, nums, count, pos + 1, useConcat);
    if (res != 0) {
      return res;
    }
  }

  work = value * nums[pos];
  if (pos == count - 1) {
    if (work == target) {
      return target;
    }
  }
  else {
    res = compute(target, work, nums, count, pos + 1, useConcat);
    if (res != 0) {
      return res;
    }
  }

  if(useConcat) {
    work = concatLongLong(value, nums[pos]);
    if (pos == count - 1) {
      if (work == target) {
        return target;
      }
    }
    else {
      res = compute(target, work, nums, count, pos + 1, useConcat);
      if (res != 0) {
        return res;
      }
    }
  }

  return 0;
}

int main(int argc, char** argv) {

  TextLines* lines = TextLinesFromFile("/home/pallaire/devs/aoc/2024/data/day07data01.txt");

  long long nums[256];
  long count;
  long long resPart1 = 0;
  long long resPart2 = 0;

  long long t1 = timeInMilliseconds();

  for(unsigned long idx = 0; idx < lines->lineCount; idx++){
    char* l = lines->lines[idx];
    // extract numbers from string
    TextLinesExtractLongLong(l, nums, &count);
    resPart1 += compute(nums[0], nums[1], &nums[1], count-1, 1, false);
  }

  long long t2 = timeInMilliseconds();

  for(unsigned long idx = 0; idx < lines->lineCount; idx++){
    char* l = lines->lines[idx];
    // extract numbers from string
    TextLinesExtractLongLong(l, nums, &count);
    resPart2 += compute(nums[0], nums[1], &nums[1], count-1, 1, true);
  }
  long long t3 = timeInMilliseconds();



  printf("Part 1 : %llu -- in %llums\n", resPart1, t2-t1);
  printf("Part 2 : %llu -- in %llums\n", resPart2, t3-t2);

  TextLinesFree(lines);

  return EXIT_SUCCESS;
}
