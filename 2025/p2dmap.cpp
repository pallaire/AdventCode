#include <iostream>
#include "p2dmap.h"
#include "ptypes.h"

using namespace std;

P2DMap::P2DMap(char* rawdata, u64 size) {
	map = rawdata;
    w = -1;
    h = 0;

    // find width
    for(u64 i = 0; i < size; i++) {
        if(map[i] == '\n') {
            w = i;
            break;
        }
    }

    // find height
    for(u64 i = w; i < size; i += (w+1)) {
        if(map[i] == '\n') {
            h++;
        }
    }

    // + 1 line since we don't support empty lines
    h++;
}

P2DMap::~P2DMap() {
}


i64 P2DMap::getWidth() {
    return w;
}

i64 P2DMap::getHeight() {
    return h;
}

char P2DMap::get(i64 x, i64 y) {
    return map[(y*(w+1)) + x];
}

void P2DMap::set(i64 x, i64 y, char c) {
    map[(y*(w+1)) + x] = c;
}

// char* P2DMap::operator[] (i64 y) {
//     return map + (y*(w+1));
// }

void P2DMap::print() {
    for(i64 y = 0; y < h; y++) {
        for(i64 x = 0; x < w; x++) {
            cout << map[(y*(w+1)) + x];
        }        
        cout << std::endl;
    }
    cout << "Width: " << w << std::endl;
    cout << "Height: " << h << std::endl;
}

