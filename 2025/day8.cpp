#include <iostream>
#include <limits>
#include <map>
#include <set>
#include <string>
#include <tuple>
#include <vector>

#include "pchrono.h"
#include "pfile.h"
#include "ptypes.h"

using namespace std;

class Pos3D {
public:
    Pos3D(char* in, u64 size, u64* pIDX) {
        x = 0;
        y = 0;
        z = 0;
        scanInput(in, size, pIDX);
    };

    ~Pos3D() {};

    void scanInput(char* in, u64 size, u64* pIDX) {
        u64 work = 0;
        for(u64 i = *pIDX; i < size; i++) {
            if(in[i] >= '0' && in[i] <= '9') {
                work *= 10;
                work += (in[i] - '0');
            } else if(in[i] == '\n') {
                in[i] = 0;
                name = string(in + *pIDX);
                z = work;
                *pIDX = i + 1;
                return;
            }
            else {
                if(x == 0) {
                    x = work;
                } else {
                    y = work;
                }
                work = 0;
            }
        }

        // for the last line of the file.
        name = string(in + *pIDX);
        z = work;
        *pIDX = size + 1;
    }

    string concat(const Pos3D& b) {
        if(name < b.name) {
            return name + "_" + b.name;
        } else {
            return b.name + "_" + name;
        }
    }

    u64 distance(const Pos3D& b) {
        u64 dx = x - b.x;
        u64 dy = y - b.y;
        u64 dz = z - b.z;
        return dx*dx + dy*dy + dz*dz;
    }

    void print() {
        cout << name << "   [ " << x << ", " << y << ", " << z << " ]" << std::endl;
    }

    string name;
    u64 x, y, z;

};


int main(int argc, char** argv) {
    cout << "Running Day number > " << DAY_NUM << std::endl;
    PChrono apptiming("Main");
    PFile file(PFile::getDataPathFromArgs(argc, argv, DAY_NUM));

    bool isTest = file.getIsTestFile();

    PChrono* p1timing = new PChrono("Problem1");
    u64 res = 1;

    // Parse all the position
    char* data = file.getRawData();
    u64 size = file.getSize();
    u64 idx = 0;
    vector<Pos3D> positions;

    while(idx < size) {
        positions.push_back(Pos3D(data, size, &idx));
    }

    u64 shortestCount = isTest ? 10 : 1000;

    vector<tuple<u64, Pos3D*, Pos3D*>> distances;

    // Get all the distances
    for(u64 a = 0; a < positions.size()-1; a++) {
        for(u64 b = a+1; b < positions.size(); b++) {
            u64 d = positions[a].distance(positions[b]);
            distances.push_back(make_tuple(d, &positions[a], &positions[b]));
        }
    }

    // Sort all the distances to have them from small to large
    sort(distances.begin(), distances.end(), [](const tuple<u64, Pos3D*, Pos3D*>& a, const tuple<u64, Pos3D*, Pos3D*>& b) {
        return get<0>(a) < get<0>(b);
    });


    // Now gather only 1000 ( 10 for the test ) of the smallest connections
    set<string> connected;
    vector<tuple<u64, Pos3D*, Pos3D*>> limited;
    u64 found = 0;

    for(auto d : distances) {
        if( (connected.contains(get<1>(d)->name) == false) && (connected.contains(get<2>(d)->name) == false)) {
            found++;

            limited.push_back(d);
                        
            if(found == shortestCount) {
                // we have enough
                break;
            }
        }
    }

    // now create circuit
    vector<u64> circuitsizes;

    while(limited.size() > 0) {
        connected.clear();

        auto tail = limited.back();
        limited.pop_back();
        connected.insert(get<1>(tail)->name); 
        connected.insert(get<2>(tail)->name); 

        bool found = true;

        while(found) {
            found = false;

            for(u64 l = 0; l < limited.size(); l++) {
                string from = get<1>(limited[l])->name;
                string to = get<2>(limited[l])->name;

                if(connected.contains(from) || connected.contains(to)) {
                    found = true;
                    connected.insert(from);
                    connected.insert(to);

                    limited.erase(limited.begin() + l);
                    l--; // so that we don't skip an element, because of the deleted one.
                }
            }
        }

        // cout << "Circuit size: " << connected.size() << std::endl;

        circuitsizes.push_back(connected.size());
    }

    sort(circuitsizes.begin(), circuitsizes.end(), [](u64 a, u64 b) { return a > b; });
    res = 1;
    for(u64 i = 0; i < 3; i++) {
        res *= circuitsizes[i];
    }



    // for(u64 i = 0; i < shortestCount; i++) {
    //     cout << get<0>(limited[i]) << "  " << get<1>(limited[i])->name << "  " << get<2>(limited[i])->name << std::endl;
    // }




    cout << "Result 1 : " << res << std::endl;
    delete p1timing;



    PChrono* p2timing = new PChrono("Problem2");
    res = 0;
    cout << "Result 2 : " << res << std::endl;
    delete p2timing;

    
    return 0;
}

