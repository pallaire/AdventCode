#include <cmath>
#include <iostream>
#include <string>

#include "pchrono.h"
#include "pfile.h"
#include "ptypes.h"

using namespace std;


int main(int argc, char** argv) {
    cout << "Running Day number > " << DAY_NUM << std::endl;
    PChrono apptiming("Main");
    PFile file(PFile::getDataPathFromArgs(argc, argv, DAY_NUM));

    char* chardata = file.getRawData();
    u64 size = file.getSize();

    u64 froms[64];
    u64 tos[64];
    u64 count = 0;

    u64 work = 0;
    char c;

    for(u64 i = 0; i < size; i++) {
        c = chardata[i];

        switch(c) {
            case ',':
                tos[count] = work;
                count++;
                work = 0;
                break;
            case '-':
                froms[count] = work;
                work = 0;
                break;
            default:
                work *= 10;
                work += c - '0';
                break;
        }
    }

    // add the last pair
    tos[count] = work;
    count++;

    PChrono* p1timing = new PChrono("Problem1");
    u64 res = 0;
    u64 res2 = 0;

    for(u64 i = 0; i < count; i++) {
        u64 from = froms[i];
        u64 to = tos[i];

        for (u64 tocheck = from; tocheck <= to; tocheck++) {
            u64 digits = floor(log10(tocheck)) + 1;
            u64 maxpattern = digits/2;
            u64 divider = 10;

            for(u64 patternlen = 1; patternlen <= maxpattern; patternlen++) {
                // does the pattern fit?
                if(digits % patternlen == 0) {
                    u64 work  = tocheck;
                    u64 pattern = work % divider;
                    work /= divider;

                    u64 patterncheck;
                    u64 found = true;

                    while(work > 0) {
                        patterncheck = work % divider;

                        if(pattern != patterncheck) {
                            found = false;
                            break;
                        }

                        work /= divider;
                    }

                    if(found) {
                        res2 += tocheck;

                        // #1 embedded in #2
                        if((digits&1) == 0) {
                            // Problem one check only for the half
                            u64 onedivider  = (u64)pow(10, digits/2);
                            if((tocheck % onedivider) == (tocheck / onedivider)) {
                                res += tocheck;
                            }
                        }


                        break;
                    }
                }
                divider *= 10;
            }
        }
    }
    delete p1timing;

    cout << "Result 1 : " << res << std::endl;
    cout << "Result 2 : " << res2 << std::endl;

    return 0;
}

// Result 1 : 38158151648
// Result 2 : 45283684555
// baseline with successfull #1 and #2 : 65ms
// removed regex : 48ms
// changed the vector<pair> to double u64 arrays: 48ms
// no string using low/pow instead : 42ms
// string ref where needed : 39ms
// computational only, no str comparison : 33ms
// embed #1 into #2 : 23ms

