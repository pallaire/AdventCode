#include <iostream>
#include <set>
#include <string>
#include <vector>

#include "p2dmap.h"
#include "pchrono.h"
#include "pfile.h"
#include "ptypes.h"

using namespace std;

// int walkmap(const P2DMap map, u64 w, u64 h, u64 x, u64 y) {
//     if(y >= h-1) {
//         return 1;
//     }

//     u64 res = 0;

//     if(map[y][x] == '^') {
//         res += walkmap(map, w, h, x-1, y+1);
//         res += walkmap(map, w, h, x+1, y+1);
//     } else {
//         res += walkmap(map, w, h, x, y+1);
//     }

//     return res;
// }


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
    // res = walkmap(map, w, h, sx, 0);
    beams.clear();
    beams.insert(sx);

    // set<pair<u64, u64>> timelines;
    // timelines.insert({sx, 0});
    vector<pair<u64, u64>> timelines;
    timelines.push_back({sx, 0});

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
                // timelines.insert({b-1, y});
                // timelines.insert({b+1, y});
                timelines.push_back({b-1, y});
                timelines.push_back({b+1, y});
            } else {
                // no split, go down
                newbeams.insert(b);
            }
        }
        
        beams = newbeams;
    }

    res = timelines.size();



    cout << "Result 2 : " << res << std::endl;
    delete p2timing;

    return 0;
}

