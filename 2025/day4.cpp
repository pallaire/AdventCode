#include <iostream>

#include "p2dmap.h"
#include "pchrono.h"
#include "pfile.h"
#include "ptypes.h"

using namespace std;

i64 kDX[8] = {1, 1, 0, -1, -1, -1, 0, 1};
i64 kDY[8] = {0, 1, 1, 1, 0, -1, -1, -1};


bool isAccessible(const P2DMap& map, i64 x, i64 y) {
  // we need to check only paperroll positions.
  if(map[y][x] != '@') {
    return false;
  }

  i64 total = -map[y][x];
  char* x2 = (&map[y][x]) - 1;
  char* x1 = x2 - map.w;
  char* x3 = x2 + map.w;

  for(u64 i = 0; i < 3; i++) {
    total += *x1++ + *x2++ + *x3++;
  }

  // ascii '.' = 46
  // ascii '@' = 64
  return (total - (8*'.')) < (4 * ('@'-'.'));
}

int main(int argc, char** argv) {
    cout << "Running Day number > " << DAY_NUM << std::endl;
    PChrono apptiming("Main");
    PFile file(PFile::getDataPathFromArgs(argc, argv, DAY_NUM));
    P2DMap map(file.getRawData(), file.getSize(), '.');

    PChrono* p1timing = new PChrono("Problem1");
    u64 res = 0;
    i64 w = map.getWidth();
    i64 h = map.getHeight();

    for(i64 y = 1; y < h-1; y++) {
      for(i64 x = 1; x < w-1; x++) {
        if(isAccessible(map, x, y)) {
          res++;
        }
      }
    }

    cout << "Result 1 : " << res << std::endl;
    delete p1timing;

  
    
    PChrono* p2timing = new PChrono("Problem2");
    res = 0;

    // vector<pair<i64, i64>> rechecks;
    i64 recheckx[25000];
    i64 rechecky[25000];
    i64 rechecks = 0;

    // check all the map first
    for(i64 y = 1; y < h-1; y++) {
      for(i64 x = 1; x < w-1; x++) {
        if(isAccessible(map, x, y)) {
          res++;
          map[y][x] = '.';

          // recheck all around
          for(i64 c = 0; c < 8; c++) {
            recheckx[rechecks] = x + kDX[c];
            rechecky[rechecks] = y + kDY[c];
            rechecks++;
          }
        }
      }
    }

    // Check only the potential changes
    i64 x, y;
    while(rechecks > 0) {
      rechecks--;
      x = recheckx[rechecks];
      y = rechecky[rechecks];

      if(map[y][x] == '.') {
        continue;
      }

      if(isAccessible(map, x, y)) {
        res++;
        map[y][x] = '.';

        // recheck all around
        for(i64 c = 0; c < 8; c++) {
          recheckx[rechecks] = x + kDX[c];
          rechecky[rechecks] = y + kDY[c];
          rechecks++;
        }
      }
    }
    cout << "Result 2 : " << res << std::endl;
    delete p2timing;

    return 0;
}

// base line : 1.1 --> 1.5ms
// vector to set : 4x slower
// in recheck, check map[y][x] == '.' for early skip if it was done already : 1ms
// added a border to the map to remove the out of bound checks: 1ms
// use Luc's addition algorithm instead of ifs. : 0.6ms
// replace vector by fixed size array : 0.4ms
