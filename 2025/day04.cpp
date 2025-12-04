#include <iostream>
#include <regex>
#include <string>

#include "pchrono.h"
#include "pfile.h"
#include "ptypes.h"

using namespace std;


int main(int argc, char** argv) {
    cout << "Running Day number > " << DAY_NUM << std::endl;
    PChrono apptiming("Main");
    PFile file(PFile::getDataPathFromArgs(argc, argv, DAY_NUM));
    vector<string> lines = file.getDataOfStrings();


    PChrono* p1timing = new PChrono("Problem1");
    u64 res = 0;
    i64 w = lines[0].length();
    i64 h = lines.size();
    i64 cx, cy, count;
    i64 dx[8] = {1, 1, 0, -1, -1, -1, 0, 1};
    i64 dy[8] = {0, 1, 1, 1, 0, -1, -1, -1};

    for(i64 y = 0; y < h; y++) {
      for(i64 x = 0; x < h; x++) {

        // we need to check only paperroll positions.
        if(lines[y][x] != '@') {
          continue;
        }

        count = 0;
        
        for(i64 c = 0; c < 8; c++) {
          cx = x + dx[c];
          cy = y + dy[c];

          if(cx<0 || cx>=w || cy<0 || cy>=h){
            continue;
          }

          if(lines[cy][cx] == '@') {
            count++;

            if(count == 4) {
              break;
            }
          }
        }

        if(count < 4) {
          res++;
        }
      }
    }
    cout << "Result 1 : " << res << std::endl;
    delete p1timing;

  

    PChrono* p2timing = new PChrono("Problem2");
    res = 0;
    u64 prevres = 1000000000;

    while(res != prevres) {
      prevres = res;

      for(i64 y = 0; y < h; y++) {
        for(i64 x = 0; x < h; x++) {

          // we need to check only paperroll positions.
          if(lines[y][x] != '@') {
            continue;
          }

          count = 0;

          for(i64 c = 0; c < 8; c++) {
            cx = x + dx[c];
            cy = y + dy[c];

            if(cx<0 || cx>=w || cy<0 || cy>=h){
              continue;
            }

            if(lines[cy][cx] == '@') {
              count++;

              if(count == 4) {
                break;
              }
            }
          }

          if(count < 4) {
            res++;
            lines[y][x] = '.';
          }
        }
      }
    }
    cout << "Result 2 : " << res << std::endl;
    delete p2timing;

    return 0;
}
