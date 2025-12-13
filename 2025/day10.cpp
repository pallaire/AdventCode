#include <iostream>
#include <bitset>
#include <map>
#include <vector>

#include "pchrono.h"
#include "pfile.h"
#include "ptypes.h"

using namespace std;

const u64 maxval = 0xFFFFFFFFFFFFFFF;

class Machine {
public:
    Machine(string data) {
        lightsTarget = 0;
        lightsMask = 0;
        bitcount = 0;

        // scan line for data
        u64 scanmode = 0; // 0=lights 1=buttons 2=jolts
        u16 work = 0;
        for(char c : data) {
            
            if(scanmode == 0) {
                if(c == '[') {
                    continue;
                }

                if(c == ']') {
                    scanmode = 1;
                    continue;
                }

                lightsTarget = (lightsTarget << 1) | (c=='#' ? 1 : 0);
                lightsMask = (lightsMask << 1) | 1;
                bitcount++;
            } else if(scanmode == 1) {
                switch(c) {
                    case '{':
                        scanmode = 2;
                        continue;

                    case '(':
                        work = 0;
                        break;

                    case ')':
                        buttons.push_back(work);
                        break;

                    case ',':
                        break;

                    default:
                        work |= 1 << ((bitcount-1) - (c-'0'));
                        break;
                }
            } else {
                // jolts
                break;
            }
        }
    }

    void print() {
        cout << "bits:"<< bitcount;

        bitset<10> bitlightsTarget(lightsTarget);
        bitset<10> bitlightsMask(lightsMask);

        cout << "   target:" << bitlightsTarget << "   mask:" << bitlightsMask << std::endl;
        for(u16 b : buttons) {
            bitset<10> bitb(b);
            cout << "    button: " << b << "   " << bitb << std::endl;
        }
    }

    u64 turnOnLights() {
        u64 res = maxval;
        u64 tmp;

        cache.clear();

        for(u16 b : buttons) {
            tmp = tryLightButton(0 , b);
            if(tmp != 0) {
                if(tmp < res) {
                    res = tmp;
                }
            }
        }
        return res;
    }

    u64 tryLightButton(u16 lights, u16 flip) {
        // loop detection and early exit
        u32 key = (lights<<10) + flip;
        if(cache.find(key) != cache.end()) {
            return cache[key];
        }

        lights ^= flip;

        if(lights == lightsTarget) {
            cache[key] = 1;
            return 1;
        } else if (lights == 0) {
            cache[key] = 0;
            return 0;
        }

        // temporary val in the cache
        // using max value, it will be updated below 
        // with the real value, this is to stop loops
        cache[key] = maxval;


        u64 res = maxval;
        u64 tmp;

        for(u16 b : buttons) {
            tmp = tryLightButton(lights, b);

            if(tmp != 0) {
                if(tmp+1 < res) {
                    res = tmp+1;
                }
            }
        }

        if(res == maxval) {
            // invalid path
            res = 0;
        }

        cache[key] = res;
        return res;
    }

    u16 lightsTarget;
    u16 lightsMask;
    u64 bitcount;
    vector<u16> buttons;
    map<u32, u64> cache;
};

int main(int argc, char** argv) {
    cout << "Running Day number > " << DAY_NUM << std::endl;
    PChrono apptiming("Main");
    PFile file(PFile::getDataPathFromArgs(argc, argv, DAY_NUM));


    PChrono* p1timing = new PChrono("Problem1");
    u64 res = 0;

    vector<string> lines = file.getDataOfStrings();
    vector<Machine> machines;

    for(string& aline: lines) {
        machines.push_back(Machine(aline));
    }

    for(Machine& m: machines) {
        res += m.turnOnLights();
    }

    cout << "Result 1 : " << res << std::endl;
    delete p1timing;




    PChrono* p2timing = new PChrono("Problem2");
    res = 0;
    cout << "Result 2 : " << res << std::endl;
    delete p2timing;

    
    return 0;
}

