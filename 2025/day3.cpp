#include <iostream>
#include <regex>
#include <string>

#include "pchrono.h"
#include "pfile.h"
#include "ptypes.h"

using namespace std;


int main(int argc, char** argv) {
    cout << "Running Day number > " << DAY_NUM << std::endl;
    PChrono apptiming("Main");
    PFile file(PFile::getDataPathFromArgs(argc, argv, DAY_NUM));
    vector<string> lines = file.getDataOfStrings();


    PChrono* p1timing = new PChrono("Problem1");
    u64 res = 0;
    u64 llength = lines[0].length();

    for(string line : lines) {
        // find the max first number
        char fn = line[0];
        u64 fnpos = 0;
        for(u64 f = 1; f < llength - 1; f++) {
            if(line[f] > fn) {
                fn = line[f];
                fnpos = f;

                if(fn == '9') {
                    break;
                }
            }
        }

        // find the max second number
        char sn = line[llength-1];
        for(u64 s = llength-2; s > fnpos; s--) {
            if(line[s] > sn) {
                sn = line[s];
            }

            if(sn == '9') {
                break;
            }
        }

        res += (fn-'0')*10 + (sn-'0');
    }
    cout << "Result 1 : " << res << std::endl;
    delete p1timing;



    PChrono* p2timing = new PChrono("Problem2");
    res = 0;
    for(string line : lines) {
        u64 pos = 0;
        u64 battery = 0;
        char c;
        char maxc;

        for(u64 n = 0; n < 12; n++) {
            maxc = '0' - 1;

            for(u64 idx = pos; idx < (llength - 12 + 1 + n); idx++) {
                c = line[idx];

                if(c > maxc) {
                    maxc = c;
                    pos = idx+1;
                }

                if(c == '9') {
                    break;
                }
            }

            battery *= 10;
            battery += maxc - '0';
        }

        res += battery;
    }
    cout << "Result 2 : " << res << std::endl;
    delete p2timing;

    return 0;
}
