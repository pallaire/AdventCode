#include <algorithm>
#include <iostream>
#include <array>
#include <vector>

#include "pchrono.h"
#include "pfile.h"
#include "ptypes.h"

using namespace std;

int day9main(int argc, char** argv) {
    cout << "Running Day number > " << 9 << std::endl;
    PChrono apptiming("Main");
    PFile file(PFile::getDataPathFromArgs(argc, argv, 9));
    vector<u32> nums = file.getDataOfNumbers();
    u32 numcount = (u32)(nums.size() / 2);

    vector<array<u64, 3>> rectcache;

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

            rectcache.push_back({area, a, b});
        }
    }
    cout << "Result 1 : " << res << std::endl;
    delete p1timing;

    PChrono* p2timing = new PChrono("Problem2");
    res = 0;


    PChrono* p3timing = new PChrono("Alloc and init");
    const u32 cachesize = 100000;
    i32* left = new i32[cachesize];
    i32* right = new i32[cachesize];
    i32* top = new i32[cachesize];
    i32* bottom = new i32[cachesize];
    for(u32 i = 0; i < cachesize; i++) {
        left[i] = 1000000;
        right[i] = -1;
        top[i] = 1000000;
        bottom[i] = -1;
    }

    // find the borders
    for(u32 a = 0; a < numcount; a++) {
        u32 b = (a+1)%numcount;
        i32 ax = nums[a*2];
        i32 ay = nums[(a*2)+1];
        i32 bx = nums[b*2];
        i32 by = nums[(b*2)+1];

        if(ax > bx) {
            i32 tmp = bx;
            bx = ax;
            ax = tmp;
        }

        if(ay > by) {
            i32 tmp = by;
            by = ay;
            ay = tmp;
        }

        if(ax == bx) {
            //vertical
            for(i32 y = ay; y <= by; y++) {
                if(ax < left[y]) {
                    left[y] = ax;
                }

                if(ax > right[y]) {
                    right[y] = ax;
                }
            }
        } else {
            //horizontal
            for(i32 x = ax; x <= bx; x++) {
                if(ay < top[x]) {
                    top[x] = ay;
                }

                if(ay > bottom[x]) {
                    bottom[x] = ay;
                }
            }
        }
    }
    delete p3timing;

    // sort all the area big to small
    sort(rectcache.begin(), rectcache.end(), [](auto a, auto b) {
        return a[0] > b[0];
    });

    // check all the rect from large to small, the first valid one is good.
    for(auto rect : rectcache) {
        u64 area = rect[0];
        u64 a = rect[1];
        u64 b = rect[2];

        i32 ax = nums[a*2];
        i32 ay = nums[(a*2)+1];
        i32 bx = nums[b*2];
        i32 by = nums[(b*2)+1];


        if(ax > bx) {
            i32 tmp = bx;
            bx = ax;
            ax = tmp;
        }

        if(ay > by) {
            i32 tmp = by;
            by = ay;
            ay = tmp;
        }

        bool goodarea = true;

        //vertical
        for(i32 y = ay; y <= by; y++) {
            if(left[y] > ax) {
                goodarea = false;
                break;
            }

            if(right[y] < bx) {
                goodarea = false;
                break;
            }
        }

        if(!goodarea) {
            continue;
        }

        //horizontal
        for(i32 x = ax; x <= bx; x++) {
            if(top[x] > ay) {
                goodarea = false;
                break;
            }

            if(bottom[x] < by) {
                goodarea = false;
                break;
            }
        }

        if(goodarea) {
            res = area;
            break;
        }
    }

    cout << "Result 2 : " << res << std::endl;
    delete p2timing;

    
    return 0;
}

