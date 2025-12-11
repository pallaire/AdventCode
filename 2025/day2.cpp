#include <iostream>
#include <regex>
#include <string>

#include "pchrono.h"
#include "pfile.h"
#include "ptypes.h"

using namespace std;

bool findBySkipping(const string s, const u64 length, const char c, u64 start, u64 skip) {
    u64 pos = start;
    while (pos < length) {
        if (s[pos] != c) {
            return false;
        }
        pos += skip;
    }
    return true;
}

bool findRepeating(const string s, const u64 length, const u64 patternlength) {
    for (u64 skip = 1; skip <= patternlength; skip++) {
        if (length % skip != 0) {
            continue;
        }

        for (u64 pos = 0; pos < skip; pos++) {
            if (findBySkipping(s, length, s[pos], pos, skip)) {
                if (pos == skip - 1) {
                    return true;
                }
            } else {
                break;
            }
        }
    }
    return false;
}

int main(int argc, char** argv) {
    cout << "Running Day number > " << DAY_NUM << std::endl;
    PChrono apptiming("Main");
    PFile file(PFile::getDataPathFromArgs(argc, argv, DAY_NUM));
    vector<string> lines = file.getDataOfStrings();

    string range;
    stringstream ss(lines[0]);

    regex pattern("(\\d+)-(\\d+)");
    smatch matches;

    u64 from, to;
    vector<pair<u64, u64>> data;
    while (getline(ss, range, ',')) {
        if (std::regex_search(range, matches, pattern)) {
            data.push_back(pair<u64, u64>(stol(matches[1]), stol(matches[2])));
        }
    }

    PChrono* p1timing = new PChrono("Problem1");
    u64 res = 0;
    for (auto range : data) {
        from = range.first;
        to = range.second;

        for (u64 tocheck = from; tocheck <= to; tocheck++) {
            string s = std::to_string(tocheck);

            if (tocheck > 10) {
                u64 l = s.length();

                // if even length
                if ((l & 1) == 0) {
                    u64 hl = l >> 1;
                    bool same = true;

                    for (u64 i = 0; i < hl; i++) {
                        if (s[i] != s[i + hl]) {
                            same = false;
                            break;
                        }
                    }

                    if (same) {
                        res += tocheck;
                    }
                }
            }
        }
    }
    cout << "Result 1 : " << res << std::endl;
    delete p1timing;

    PChrono* p2timing = new PChrono("Problem2");
    res = 0;
    for (auto range : data) {
        from = range.first;
        to = range.second;

        for (u64 tocheck = from; tocheck <= to; tocheck++) {
            string s = std::to_string(tocheck);
            u64 maxpattern = s.length() / 2;

            if (findRepeating(s, s.length(), maxpattern)) {
                res += tocheck;
            }
        }
    }

    cout << "Result 2 : " << res << std::endl;
    delete p2timing;

    return 0;
}
