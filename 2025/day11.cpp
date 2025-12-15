#include <iostream>
#include <bitset>
#include <map>
#include <vector>

#include "pchrono.h"
#include "pfile.h"
#include "ptypes.h"

using namespace std;

u64 countPath(map<string, vector<string>>& data, string& pos) {
    if(pos == "out") {
        return 1;
    }
    
    u64 res = 0;
    vector<string>& destinations = (data[pos]);
    for(string& dst : destinations) {
        res += countPath(data, dst);
    }

    return res;
}

map<string, u64> cache;
u64 countPathFromSVR(map<string, vector<string>>& data, string& pos, u64 dac, u64 fft) {
    string key(pos + to_string(dac) + to_string(fft));
    if(cache.find(key) != cache.end()) {
        return cache[key];
    }

    if(pos == "out") {
        if(dac==1 && fft==1) {
            cache[key] = 1;
            return 1;
        } else {
            cache[key] = 0;
            return 0;
        }
    }
    
    if(pos=="dac") {
        dac = 1;
    }

    if(pos=="fft") {
        fft = 1;
    }
    
    u64 res = 0;
    vector<string>& destinations = (data[pos]);
    for(string& dst : destinations) {
        res += countPathFromSVR(data, dst, dac, fft);
    }
    cache[key] = res;
    return res;
}


int main(int argc, char** argv) {
    cout << "Running Day number > " << DAY_NUM << std::endl;
    PChrono apptiming("Main");
    PFile file(PFile::getDataPathFromArgs(argc, argv, DAY_NUM));



    PChrono* p1timing = new PChrono("Problem1");
    u64 res = 0;

    map<string, vector<string>> data;
    vector<string> lines = file.getDataOfStrings();

    for(string& aline: lines) {
        string key = aline.substr(0, 3);
        data[key] = vector<string>();
        u64 idx = 5;
        while(idx < aline.length()) {
            data[key].push_back(aline.substr(idx, 3));
            idx += 4;
        }
    }

    string start("you");
    res = countPath(data, start);

    cout << "Result 1 : " << res << std::endl;
    delete p1timing;




    PChrono* p2timing = new PChrono("Problem2");
    res = 0;

    start = "svr";
    res = countPathFromSVR(data, start, 0, 0);

    cout << "Result 2 : " << res << std::endl;
    delete p2timing;

    
    return 0;
}

