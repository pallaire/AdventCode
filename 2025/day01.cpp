#include <iostream>
#include <string>
#include "pchrono.h"
#include "pfile.h"
#include "ptypes.h"

using namespace std;


int main (int argc, char** argv) {
  cout << "Running Day number > " << DAY_NUM << std::endl;
  
  PChrono apptiming("Main");
  PFile file(PFile::getDataPathFromArgs(argc, argv, DAY_NUM));
  vector<string> lines = file.getDataOfStrings();


  i64 pos = 50;
  i64 dir;
  i64 ticks;
  i64 res = 0;

  for(string l : lines) {
    dir = l[0] == 'R' ? 1 : -1;

    ticks = stoi(l.substr(1));
    if(dir > 0) {
      ticks = 100 - ticks;
    }

    pos += ticks;
    pos %= 100;

    if(pos == 0) {
      res++;
    }
  }

  cout << "Result 1 : " << res << std::endl;



  pos = 50;
  res = 0;

  i64 prevpos = pos;
  i64 fullturns;

  for(string l : lines) {
    dir = l[0] == 'R' ? 1 : -1;
    ticks = dir * stoi(l.substr(1));

    fullturns = ticks / 100;
    res += abs(fullturns);

    ticks -= fullturns*100;
    pos += ticks;

    if(pos == 0) {
      res++;
    } else if(pos >= 100) {
      pos %= 100;
      res++;
    } else if(pos < 0) {
      pos = 100 + pos;
      if(prevpos != 0) {
        res++;
      }
    }

    prevpos = pos;
  }

  cout << "Result 2 : " << res << std::endl;


  return 0;
}
