#include <iostream>
#include <string>
#include <vector>

#include "pchrono.h"
#include "pfile.h"
#include "putils.h"

using namespace std;

class bingocard {
public:
    bingocard(vector<string> input, unsigned int startline) {
        for(int t = 0; t < 5; t++) {
            _linesTotal[t] = 0;
            _colsTotal[t] = 0;
        }

        for(int y = 0; y < 5; y++) {
            vector<int> cardline = splitStringToVectorInt(input[startline+y], ' ');

            for(int x = 0; x < 5; x++) {
                _card[(y*5)+x] = cardline[x];
                _linesTotal[y] += cardline[x];
                _colsTotal[x] += cardline[x];
            }
        }
    }

    void print() {
        for(int y = 0; y < 5; y++) {
            for(int x = 0; x < 5; x++) {
                cout << _card[(y*5)+x] << " ";
            }
            cout << std::endl;
        }
        cout << std::endl;
    }

    bool isBingo() {
        for(int t = 0; t < 5; t++) {
            if(_linesTotal[t] == 0 || _colsTotal[t] == 0) {
                return true;
            }
        }
        return false;
    }

    bool crossNumber(int n) {
        for(int c = 0; c < 25; c++) {
            if(_card[c] == n) {
                int x = c % 5;
                int y = c / 5;

                _linesTotal[y] -= n;
                _colsTotal[x] -= n;
                break;
            }
        }

        return isBingo();
    }


private:
    int _card[25];
    int _linesTotal[5];
    int _colsTotal[5];
};


int main (int argc, char** argv) {
  cout << "Running Day number > " << DAY_NUM << std::endl;
  
  PChrono apptiming("Main");
  PFile file(PFile::getDataPathFromArgs(argc, argv, DAY_NUM));
  vector<string> lines = file.getDataOfStrings();

  vector<int> bingoNumbers = splitStringToVectorInt(lines[0], ',');
  vector<bingocard> cards;

  unsigned int startline = 1;
  while(startline < lines.size()) {
    cards.push_back(bingocard(lines, startline));
    startline += 5;

    cards[cards.size()-1].print();
  }


  return 0;
}
