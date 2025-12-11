#include <iostream>
#include <vector>

#include "p2dmap.h"
#include "pchrono.h"
#include "pfile.h"
#include "ptypes.h"

using namespace std;

i64 kDX[8] = {1, 1, 0, -1, -1, -1, 0, 1};
i64 kDY[8] = {0, 1, 1, 1, 0, -1, -1, -1};


bool isAccessible(const P2DMap map, i64 w, i64 h, i64 x, i64 y) {
  // we need to check only paperroll positions.
  if(map[y][x] != '@') {
    return false;
  }

  u64 count = 0;
  
  for(i64 c = 0; c < 8; c++) {
    i64 cx = x + kDX[c];
    i64 cy = y + kDY[c];

    if(cx<0 || cx>=w || cy<0 || cy>=h){
      continue;
    }

    if(map[cy][cx] == '@') {
      count++;

      if(count == 4) {
        break;
      }
    }
  }  

  return (count < 4);
}

int main(int argc, char** argv) {
    cout << "Running Day number > " << DAY_NUM << std::endl;
    PChrono apptiming("Main");
    PFile file(PFile::getDataPathFromArgs(argc, argv, DAY_NUM));
    P2DMap map(file.getRawData(), file.getSize());
    apptiming.print();

    PChrono* p1timing = new PChrono("Problem1");
    u64 res = 0;
    i64 w = map.getWidth();
    i64 h = map.getHeight();

    for(i64 y = 0; y < h; y++) {
      for(i64 x = 0; x < w; x++) {
        if(isAccessible(map, w, h, x, y)) {
          res++;
        }
      }
    }
    cout << "Result 1 : " << res << std::endl;
    delete p1timing;

  
    
    PChrono* p2timing = new PChrono("Problem2");
    res = 0;

    vector<pair<i64, i64>> rechecks;

    // check all the map first
    for(i64 y = 0; y < h; y++) {
      for(i64 x = 0; x < w; x++) {
        if(isAccessible(map, w, h, x, y)) {
          res++;
          map[y][x] = '.';

          // recheck all around
          for(i64 c = 0; c < 8; c++) {
            i64 cx = x + kDX[c];
            i64 cy = y + kDY[c];

            if(cx<0 || cx>=w || cy<0 || cy>=h){
              continue;
            }

            rechecks.push_back({cx, cy});
          }
        }
      }
    }

    // Check only the potential changes
    pair<i64, i64> pos;
    i64 x, y;
    while(rechecks.size()) {
      pos = rechecks.back();
      rechecks.pop_back();

      x = pos.first;
      y = pos.second;

      if(isAccessible(map, w, h, x, y)) {
        res++;
        map[y][x] = '.';

        // recheck all around
        for(i64 c = 0; c < 8; c++) {
          i64 cx = x + kDX[c];
          i64 cy = y + kDY[c];

          if(cx<0 || cx>=w || cy<0 || cy>=h){
            continue;
          }

          rechecks.push_back({cx, cy});
        }
      }
    }
    cout << "Result 2 : " << res << std::endl;
    delete p2timing;

    return 0;
}
