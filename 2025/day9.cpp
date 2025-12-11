#include <iostream>
#include <array>
#include <vector>


#include "p2dmap.h"
#include "pchrono.h"
#include "pfile.h"
#include "ptypes.h"

using namespace std;

int main(int argc, char** argv) {
    cout << "Running Day number > " << DAY_NUM << std::endl;
    PChrono apptiming("Main");
    PFile file(PFile::getDataPathFromArgs(argc, argv, DAY_NUM));
    vector<u64> nums = file.getDataOfNumbers();
    u64 numcount = nums.size() / 2;

    // u64 maxx, maxy;

    PChrono* p1timing = new PChrono("Problem1");
    u64 res = 0;
    u64 area;
    for(u64 a = 0; a < numcount-1; a++) {
        for(u64 b = a+1; b < numcount; b++) {
            i64 ax = nums[a*2];
            i64 ay = nums[(a*2)+1];
            i64 bx = nums[b*2];
            i64 by = nums[(b*2)+1];

            area = (abs(ax-bx)+1) * (abs(ay-by)+1); // +1 because numbers are inclusive
            if(area > res) {
                res = area;
            }

            // if(ax > maxx) {
            //     maxx = ax;
            // }

            // if(ay > maxy) {
            //     maxy = ay;
            // }
        }
    }
    cout << "Result 1 : " << res << std::endl;
    delete p1timing;



    PChrono* p2timing = new PChrono("Problem2");
    res = 0;

    // Same approach, but search for pair that would be inside the 
    // current area
    area = 0;
    for(u64 a = 0; a <= numcount; a++) {
        for(u64 b = a+1; b < numcount; b++) {
            i64 ax = nums[a*2];
            i64 ay = nums[(a*2)+1];
            i64 bx = nums[b*2];
            i64 by = nums[(b*2)+1];

            if(ax < bx) {
                i64 tmp = bx;
                bx = ax;
                bx = tmp;
            }

            if(ay < by) {
                i64 tmp = by;
                by = ay;
                by = tmp;
            }

            bool areaok = true;

            // left - vertical check are odd numbers
            for(u64 c = 1; c <= numcount; c+=2) {
                u64 d = (c+1) % numcount;
                i64 cx = nums[c*2];
                i64 cy = nums[(c*2)+1];
                i64 dy = nums[(d*2)+1];


            }


            if(areaok) {
                area = (abs(ax-bx)+1) * (abs(ay-by)+1); // +1 because numbers are inclusive
                if(area > res) {
                    res = area;
                }
            }

            // we need to check from every side

            // if(ax > maxx) {
            //     maxx = ax;
            // }

            // if(ay > maxy) {
            //     maxy = ay;
            // }
        }
    }


    // // Start by creating the perimetter of the shape
    // i64* perimdata = new i64[2*(maxx+maxy)];
    // i64* lef = perimdata;
    // i64* rig = lef + maxy;
    // i64* top = rig + maxy;
    // i64* bot = top + maxx;

    // for(u64 y = 0; y < maxy; y++) {
    //     lef[y] = 0;
    //     rig[y] = maxx;
    // }
    
    // for(u64 x = 0; x < maxx; x++) {
    //     top[x] = 0;
    //     bot[x] = maxy;
    // }

    // u64 b;
    // for(u64 a = 0; a < numcount; a++) {
    //     b = a+1;
    //     if(b >= numcount) {
    //         b = 0;
    //     }

    //     i64 ax = nums[a*2];
    //     i64 ay = nums[(a*2)+1];
    //     i64 bx = nums[b*2];
    //     i64 by = nums[(b*2)+1];

    //     if(ax == bx) {
    //         //vertical
    //         if(by < ay) {
    //             i64 tmp = by;
    //             by = ay;
    //             ay = tmp;
    //         }

    //         for(u64 y = ay; y <= by; y++) {
    //             if(ax > lef[y]) {
    //                 lef[y] = ax;
    //             }

    //             if(ax < rig[y]) {
    //                 rig[y] = ax;
    //             }
    //         }
    //     } else {
    //         //horizontal
    //         if(bx < ax) {
    //             i64 tmp = bx;
    //             bx = ax;
    //             ax = tmp;
    //         }

    //         for(u64 x = ax; x <= bx; x++) {
    //             if(ay > top[x]) {
    //                 top[x] = ay;
    //             }

    //             if(ay < bot[x]) {
    //                 bot[x] = ay;
    //             }
    //         }
    //     }
    // }


    delete[] perimdata;
    cout << "Result 2 : " << res << std::endl;
    delete p2timing;

    
    return 0;
}

