#include <array>
#include <iostream>
#include <string>

#include "pchrono.h"
#include "pfile.h"

using namespace std;

int main (int argc, char** argv) {
  cout << "Running Day number > " << DAY_NUM << std::endl;
  
  PChrono apptiming("Main");
  PFile file(PFile::getDataPathFromArgs(argc, argv, DAY_NUM));
  vector<string> lines = file.getDataOfStrings();

  int bitcount = lines[0].size();
  array<unsigned int, 16> counter = {0};

  for(string l : lines) {
    for(int b = 0; b < bitcount; b++) {
      if(l[b] == '1') {
        counter[b]++;
      }
    }
  }

  unsigned int linecount = lines.size();

  unsigned int gamma = 0;
  unsigned int epsilon = 0;

  for(int b = 0; b < bitcount; b++) {
    gamma <<= 1;
    epsilon <<= 1;

    if(counter[b] >= linecount/2) {
      // more 1s
      gamma += 1;  
    } else {
      epsilon += 1;
    }
  }

  cout << "Result 1 : " << (gamma*epsilon) << std::endl;


  return 0;
}
