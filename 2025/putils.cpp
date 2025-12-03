#include "putils.h"

vector<int> splitStringToVectorInt(const string& s, char delim) {
    vector<int> result;
    stringstream ss(s);
    string item;
    while(getline(ss, item, delim)) {
        if(!item.empty()) {
            result.push_back(stoi(item));
        }
    }
    return result;
}