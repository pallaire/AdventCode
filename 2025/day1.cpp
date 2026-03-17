#include <iostream>
#include <string>
#include "pchrono.h"
#include "pfile.h"
#include "ptypes.h"

using namespace std;


int main (int argc, char** argv) {
  
  PChrono apptiming("");
  PFile file(PFile::getDataPathFromArgs(argc, argv, DAY_NUM));
  char* bytes = file.getRawData();
  u64 len = file.getSize();

  char b = 0;
  char dir = 0;
  i64 num = 0;
  i64 pos = 50;
  i64 startpos = 50;
  i64 turns;

  i64 res  = 0;
  i64 res2 = 0;

  for(u64 i = 0; i < len; i += 1) {
      b = bytes[i];

      if(b == 'L' || b == 'R') {
          dir = b;
          continue;
      } else {
          if(b >= 48 && b <= 57) {
              num *= 10;
              num += (b - 48); // 48 is ASCII value of '0'
          }
      }

      if(b == '\n' || i == len - 1) {

          turns = num /100;
          res2 += turns;
          num -= turns * 100;

          if(dir == 'L') {
              if (num >= pos && startpos != 0) {
                  res2 += 1;
              }
              pos = pos + 100 - num;
          } else {
              pos += num;
              if(pos >= 100) {
                  res2 += 1;
              }
          }
          
          if(pos >= 100) {
              pos -= 100;
          }
          
          if(pos == 0) {
              res += 1;
          }
          
          startpos = pos;
          num = 0;
      }
  }

  cout << "Running Day number > " << DAY_NUM << std::endl;
  cout << "Result 1 : " << res << std::endl;
  cout << "Result 2 : " << res2 << std::endl;

  return 0;
}
