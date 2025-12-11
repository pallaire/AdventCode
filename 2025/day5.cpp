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
    vector<string> lines = file.getDataOfStrings(true);


    PChrono* p1timing = new PChrono("Problem1");
    u64 res = 0;

    vector<pair<u64, u64>> lists;
    bool inLists = true;
    for(string aline : lines) {
        if(inLists) {
            if(aline.length() == 0){
                inLists = false;
                continue;
            }

            u64 idx = aline.find('-');
            lists.push_back({stol(aline.substr(0,idx)), stol(aline.substr(idx+1))});
        } else {
            u64 id = stol(aline);
            for(auto range : lists) {
                if(id >= range.first && id <= range.second) {
                    res++;
                    break;
                }
            }
        }
    }
    cout << "Result 1 : " << res << std::endl;
    delete p1timing;



    PChrono* p2timing = new PChrono("Problem2");
    res = 0;

    sort(lists.begin(), lists.end(), [](pair<u64, u64>a, pair<u64, u64>b) {
        return a.first < b.first;
    });

    // Merge ranges 
    u64 idx = 0;
    while(idx < lists.size()-1) {
        pair<u64, u64> a = lists[idx];
        pair<u64, u64> b = lists[idx+1];

        if(b.first <= (a.second + 1)) {
            if(b.second > a.second) {
                a.second = b.second;
            }
            lists.erase(lists.begin() + (idx + 1));   
            lists[idx] = a;
        } else {
            idx++;
        }
    }

    for(auto p : lists) {
        res += (p.second - p.first) + 1;
    }

    cout << "Result 2 : " << res << std::endl;
    delete p2timing;

    return 0;
}

