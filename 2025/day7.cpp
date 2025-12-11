#include <iostream>
#include <map>
#include <set>
#include <string>

#include "p2dmap.h"
#include "pchrono.h"
#include "pfile.h"
#include "ptypes.h"

using namespace std;

map<pair<i64, i64>, u64> part2cache;

u64 climb(const P2DMap map, u64 w, u64 h, i64 x, i64 y) {
  pair<i64, i64> key(x, y);

  if(part2cache.contains(key)) {
    return part2cache[key];
  }

  if(map[y][x] == 'S') {
    return 1;
  } 

  if(y < 0) {
    return 0;
  }

  u64 res = 0;

  if(map[y][x+1] == '^') {
    res += climb(map, w, h, x+1, y-2);
  }

  if(map[y][x-1] == '^') {
    res += climb(map, w, h, x-1, y-2);
  }
 
  if(map[y][x] != '^') {
    res += climb(map, w, h, x, y-2);
  }

  part2cache[key] = res;

  return res;
}


int main(int argc, char** argv) {
    cout << "Running Day number > " << DAY_NUM << std::endl;
    PChrono apptiming("Main");
    PFile file(PFile::getDataPathFromArgs(argc, argv, DAY_NUM));
    P2DMap map(file.getRawData(), file.getSize());
    u64 w = map.getWidth();
    u64 h = map.getHeight();

    PChrono* p1timing = new PChrono("Problem1");
    u64 res = 0;

    // find the starting point
    u64 sx = 0;
    for(u64 x = 0; x < w; x++) {
        if(map[0][x] == 'S') {
            sx = x;
            break;
        }
    }

    set<u64> beams;
    set<u64> newbeams;
    beams.insert(sx);

    for(u64 y = 1; y < h; y++) {
        if((y&1) == 1) {
            continue;
        }

        newbeams.clear();

        for(auto b : beams) {
            if(map[y][b] == '^') {
                // split
                newbeams.insert(b-1);
                newbeams.insert(b+1);
                res++;
            } else {
                // no split, go down
                newbeams.insert(b);
            }
        }
        
        beams = newbeams;
    }
    cout << "Result 1 : " << res << std::endl;
    delete p1timing;



    PChrono* p2timing = new PChrono("Problem2");
    res = 0;

    // Start on the last line and go up for all the paths 
    for(u64 x = 0; x < w; x++) {
      res += climb(map, w, h, x, h-2);
    }

    cout << "Result 2 : " << res << std::endl;
    delete p2timing;

    
    return 0;
}

