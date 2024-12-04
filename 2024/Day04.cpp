#include <iostream>
#include <regex>
#include <string>

#include "utils.hpp"

#include "Days.hpp"

Day04::Day04(string path) : AdventDay(path) {
    day = 4;
    title = "Ceres Search";
}

unsigned long Day04::searchAround(const vector<string>& lines, long w, long h, long x, long y, long dx, long dy, long position) {
  const char* XMAS = "XMAS";
 
  position++;
  x += dx;
  y += dy;

  if(x<0 || x>=w || y<0 || y>=h) {
    return 0;
  }

  char p = XMAS[position];
  char c = lines[y][x];

  if(c != p) {
    return 0;
  }

  if(position == 3) {
    return 1;
  }

  return searchAround(lines, w, h, x, y, dx, dy, position);
}

void Day04::part1(vector<string> lines) {
  long xmas = 0;

  unsigned long h = lines.size();
  unsigned long w = lines[0].length();

  for(unsigned long y = 0; y < h; y++) {
    for(unsigned long x = 0; x < w; x++) {
      char c = lines[y][x];
      if(c == 'X') {
        //search around
        for(long dy = -1; dy <= 1; dy++) {
          for(long dx = -1; dx <= 1; dx++) {
            if(dx==0 && dy==0){
              continue;
            }
            xmas += searchAround(lines, w, h, x, y, dx, dy, 0);
          }
        }
      }
    } 
  }

  printLongResult(xmas);
}

void Day04::part2(vector<string> lines) {
  long xmas = 0;

  unsigned long h = lines.size();
  unsigned long w = lines[0].length();

  char q1, q2, q3, q4;

  for(unsigned long y = 1; y < h-1; y++) {
    for(unsigned long x = 1; x < w-1; x++) {
      char c = lines[y][x];
      if(c == 'A') {
        //search around
        q1 = lines[y-1][x-1];
        q2 = lines[y-1][x+1];
        q3 = lines[y+1][x-1];
        q4 = lines[y+1][x+1];

        if( ((q1=='M'&&q4=='S') || (q1=='S'&&q4=='M')) &&
            ((q2=='M'&&q3=='S') || (q2=='S'&&q3=='M')) ){
            xmas++;
        }
      }
    } 
  }

  printLongResult(xmas);
}

