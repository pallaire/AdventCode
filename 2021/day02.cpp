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
  vector<string> lines = file.getDataOfStrings();



  int horizontal = 0;
  int depth = 0;

  for(string l : lines) {
    char direction = l[0];
    int movement = l[l.size()-1] - '0';

    switch(direction) {
        case 'f':
            horizontal += movement;
            break;
        case 'd':
            depth += movement;
            break;
        case 'u':
            depth -= movement;
            break;
    }
  }

  cout << "Result 1 : " << (horizontal*depth) << std::endl;



  int aim = 0;
  horizontal = 0;
  depth = 0;

  for(string l : lines) {
    char direction = l[0];
    int movement = l[l.size()-1] - '0';

    switch(direction) {
        case 'f':
            horizontal += movement;
            depth += movement*aim;
            break;
        case 'd':
            aim += movement;
            break;
        case 'u':
            aim -= movement;
            break;
    }
  }

  cout << "Result 2 : " << (horizontal*depth) << std::endl;


  return 0;
}
