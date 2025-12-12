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

    i64 maxx = 0;
    i64 maxy = 0;

    PChrono* p1timing = new PChrono("Problem1");
    u64 res = 0;
    u64 area;
    for(u64 a = 0; a < numcount-1; a++) {
        for(u64 b = a+1; b < numcount; b++) {
            i64 ax = nums[a*2];
            i64 ay = nums[(a*2)+1];
            i64 bx = nums[b*2];
            i64 by = nums[(b*2)+1];

            rect++;

            area = (abs(ax-bx)+1) * (abs(ay-by)+1); // +1 because numbers are inclusive
            if(area > res) {
                res = area;
            }

            if(ax > maxx) {
                maxx = ax;
            }

            if(ay > maxy) {
                maxy = ay;
            }
        }
    }
    cout << "Result 1 : " << res << std::endl;
    delete p1timing;

    cout << "rect count : " << rect << std::endl;

    PChrono* p2timing = new PChrono("Problem2");
    res = 0;

    maxx++;
    maxy++;

    PChrono* p3timing = new PChrono("Alloc and init");
    const u64 cachesize = 100000;
    i32* left = new i32[cachesize];
    i32* right = new i32[cachesize];
    i32* top = new i32[cachesize];
    i32* bottom = new i32[cachesize];
    for(u64 i = 0; i < cachesize; i++) {
        left[i] = 1000000;
        right[i] = -1;
        top[i] = 1000000;
        bottom[i] = -1;
    }

    // find the borders
    for(u64 a = 0; a < numcount; a++) {
        u64 b = (a+1)%numcount;
        i64 ax = nums[a*2];
        i64 ay = nums[(a*2)+1];
        i64 bx = nums[b*2];
        i64 by = nums[(b*2)+1];

        if(ax > bx) {
            i64 tmp = bx;
            bx = ax;
            ax = tmp;
        }

        if(ay > by) {
            i64 tmp = by;
            by = ay;
            ay = tmp;
        }

        if(ax == bx) {
            //vertical
            for(i64 y = ay; y <= by; y++) {
                if(ax < left[y]) {
                    left[y] = ax;
                }

                if(ax > right[y]) {
                    right[y] = ax;
                }
            }
        } else {
            //horizontal
            for(i64 x = ax; x <= bx; x++) {
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



    for(u64 a = 0; a < numcount-1; a++) {
        for(u64 b = a+1; b < numcount; b++) {
            i64 ax = nums[a*2];
            i64 ay = nums[(a*2)+1];
            i64 bx = nums[b*2];
            i64 by = nums[(b*2)+1];
            bool goodarea = true;


            area = (abs(ax-bx)+1) * (abs(ay-by)+1); // +1 because numbers are inclusive
            if(area > res) {
                // checking only potential larger areas

                if(ax > bx) {
                    i64 tmp = bx;
                    bx = ax;
                    ax = tmp;
                }

                if(ay > by) {
                    i64 tmp = by;
                    by = ay;
                    ay = tmp;
                }

                //vertical
                for(i64 y = ay; y <= by; y++) {
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
                for(i64 x = ax; x <= bx; x++) {
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
                }
            }
        }
    }



    cout << "Result 2 : " << res << std::endl;
    delete p2timing;

    
    return 0;
}

