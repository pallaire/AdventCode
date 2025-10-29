#include <cstring>
#include <format>
#include <iostream>
#include <string>

#include "pchrono.h"
#include "pfile.h"

using namespace std;



int main (int argc, char** argv) {
  cout << "Running Day number > " << DAY_NUM << std::endl;
  
  PChrono apptiming("Main");
  PFile file(PFile::getDataPathFromArgs(argc, argv));
  vector<long> nums = file.getDataOfNumbers();

  long prev = 10000000000;
  long res = 0;

  for(long l : nums) {
    if(l > prev) {
      res++;
    }

    prev = l;
  }

  cout << "Result 1 : " << res << std::endl;

  prev = nums[0] + nums[1] + nums[2];
  long next = prev;
  res = 0;

  for(unsigned int l = 3; l < nums.size(); l++) {
    next = prev - nums[l-3] + nums[l];
    if(next > prev) {
      res++;
    }
    prev = next;
  }
    
  cout << "Result 2 : " << res << std::endl;

  return 0;
}
