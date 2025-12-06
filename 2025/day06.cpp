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

    PChrono* p1timing = new PChrono("Problem1");
    u64 res = 0;
    u64 numbers[4][1000];
    u64 row = 0;
    u64 rowCount = 0;
    u64 col = 0;

    char* data = file.getRawData();
    u64 size = file.getSize();
    u64 idx = 0;

    u64 build = 0;
    bool building = true;
    bool inNumbers = true;
    char c;

    u64 linelength = 0;

    while(idx < size) {
        c = data[idx];

        if(inNumbers) {
            if(c>='0' && c<='9') {
                building = true;
                build *= 10;
                build += c-'0';
            } else if(c == ' ') {
                if(building) {
                    numbers[row][col] = build;
                    build = 0;
                    col++;
                    building = false;
                }
            } else if(c == '\n') {
                if(building) {
                    numbers[row][col] = build;
                    build = 0;
                    building = false;
                }

                if(linelength == 0) {
                    linelength = idx;
                }

                col = 0;
                row++;
                rowCount = row;
            } else {
                // done we found an operator
                inNumbers = false;
                col = 0;
                idx--; // because we don't want to skip this operator
            }
        } else {
            if(c == '+') {
                build = numbers[0][col];
                for(u64 r = 1; r < rowCount; r++) {
                    build += numbers[r][col];
                }
                res += build;
                col++;
            } else if(c == '*') {
                build = numbers[0][col];
                for(u64 r = 1; r < rowCount; r++) {
                    build *= numbers[r][col];
                }
                res += build;
                col++;
            }
        }
        idx++;
    }
    cout << "Result 1 : " << res << std::endl;
    delete p1timing;


    PChrono* p2timing = new PChrono("Problem2");
    res = 0;
    u64 oplinestart = rowCount * (linelength+1);
    u64 start = oplinestart;
    idx = start + 1;
    char op = data[start];

    while(idx <= size) {

        if(data[idx]!=' ' || idx == size) {
            u64 w = idx - start - 1;

            if(idx == size){
                w++; // there is no space to remove on last column
            }

            // build numbers and compute here
            u64 compute = 0;
            for(u64 n = 0; n < w; n++) {
                u64 x = (start - oplinestart) + n;
                build = 0;
                for(u64 y = 0; y < rowCount; y++) {
                    c = data[(y * (linelength+1)) + x];

                    if(c != ' ') {
                        build *= 10;
                        build += c-'0';
                    }
                }
                if(n == 0) {
                    compute = build;
                } else {
                    if(op == '+') {
                        compute += build;
                    } else {
                        compute *= build;
                    }
                }
            }
            res += compute;

            //start new search
            start = idx;
            op = data[start];
        }
        idx++;
    }


    cout << "Result 2 : " << res << std::endl;
    delete p2timing;

    return 0;
}

