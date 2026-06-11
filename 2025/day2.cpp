#include <cmath>
#include <future>
#include <iostream>
#include <string>

#include "pchrono.h"
#include "pfile.h"
#include "ptypes.h"

using namespace std;

inline u64 digits64(u64 v) {
    if (v >= 1000000000ULL) return 10;
    if (v >= 100000000ULL)  return 9;
    if (v >= 10000000ULL)   return 8;
    if (v >= 1000000ULL)    return 7;
    if (v >= 100000ULL)     return 6;
    if (v >= 10000ULL)      return 5;
    if (v >= 1000ULL)       return 4;
    if (v >= 100ULL)        return 3;
    if (v >= 10ULL)         return 2;
    return 1;
}

struct Result {
    u64 res1;
    u64 res2;
};

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
    u64 res1 = 0;
    u64 res2 = 0;

    const u64 kEXPONENT[8] = {0ULL, 10ULL, 100ULL, 1000ULL, 10000ULL, 100000ULL, 1000000ULL, 10000000ULL};

    std::vector<std::future<Result>> futures;

    for(u64 i = 0; i < count; i++) {
        u64 outfrom = froms[i];
        u64 outto = tos[i];

        futures.push_back(std::async(std::launch::async, [kEXPONENT](u64 from, u64 to) -> Result {
            u64 res1 = 0;
            u64 res2 = 0;
            for (u64 tocheck = from; tocheck <= to; tocheck++) {
                u64 digits = digits64(tocheck);
                u64 maxpattern = digits/2;

                for(u64 patternlen = 1; patternlen <= maxpattern; patternlen++) {
                    // does the pattern fit?
                    if(digits % patternlen == 0) {
                        u64 work  = tocheck;
                        u64 divider = kEXPONENT[patternlen];
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
                                divider = kEXPONENT[digits/2];
                                if((tocheck % divider) == (tocheck / divider)) {
                                    res1 += tocheck;
                                }
                            }
                            break;
                        }
                    }
                }
            }

            return {res1, res2};

        }, outfrom, outto));
    }

    for(auto& f : futures) {
        auto result = f.get();
        res1 += result.res1;
        res2 += result.res2;
    }

    delete p1timing;

    cout << "Result 1 : " << res1 << std::endl;
    cout << "Result 2 : " << res2 << std::endl;

    return 0;
}

// Result 1 : 38158151648
// Result 2 : 45283684555

// Timings from M4 Pro
// baseline with successfull #1 and #2 : 65ms
// removed regex : 48ms
// changed the vector<pair> to double u64 arrays: 48ms
// no string using low/pow instead : 42ms
// string ref where needed : 39ms
// computational only, no str comparison : 33ms
// embed #1 into #2 : 23ms
// IFs based digit count : 9ms
// Use of "future" to work on each interval in parallels : 3.8ms

