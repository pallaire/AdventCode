#include <array>
#include <iostream>
#include <string>

#include "pchrono.h"
#include "pfile.h"

using namespace std;

pair<string, string> filter(vector<string> lines, unsigned int pos) {
  if(lines.size() == 1) {
    return pair<string, string>(lines[0], lines[0]);    
  }

  if(pos >= 12) {
    return pair<string, string>("","");    
  }

  if(lines.size() == 0) {
    return pair<string, string>("","");    
  }

  vector<string> ones;
  vector<string> zeros;

  for(string s : lines)
  {
    if(s[pos] == '1') {
      ones.push_back(s);
    } else {
      zeros.push_back(s);
    }
  }

  pair<string, string> oxy;
  pair<string, string> co2;
  
  if(ones.size() >= zeros.size()) {
    oxy = filter(ones, pos+1);
    co2 = filter(zeros, pos+1);
  } else {
    oxy = filter(zeros, pos+1);
    co2 = filter(ones, pos+1);
  }

  return pair<string, string>(oxy.first, co2.second);
}

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



  pair<string, string> filtered = filter(lines, 0);

  unsigned long oxy = stoi(filtered.first, nullptr, 2);
  unsigned long co2 = stoi(filtered.second, nullptr, 2);

  cout << "Result 2 : " << (oxy * co2) << std::endl;


  return 0;
}
