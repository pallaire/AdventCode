#include "plib.h"

int main(int /*argc*/, char** /*argv*/) {
  u64 start = pchronoGetMicroSeconds();

  //PFile* pfile = pfileReadAll("data/day01_test01.txt");
  PFile* pfile = pfileReadAll("data/day01.txt");


  if(pfile) {

    pfileFixLines(pfile);

    u64 res = 0;
    u64 res2 = 0;
    i64 pos = 50;
    i64 startpos = 50;
    i64 num;

    for(u64 l = 0; l < pfile->linesCount; l++) {
      num = atol(pfile->lines[l]+1);
      res2 += num / 100;
      num = num % 100;

      if(pfile->lines[l][0] == 'L') {
        if(num >= pos && startpos != 0) {
          res2++;
        }
        pos = pos + 100 - num; 
      } else {
        pos += num;
        if(pos >= 100) {
          res2++;
        }
      }

      if(pos >= 100) {
        pos -= 100;
      }

      if(pos == 0) {
        res++;
      }

      startpos = pos;
    }

    pchronoPrint(pchronoGetMicroSeconds()-start, "Total");
    printf("problem 1 : %ld\n", res);
    printf("problem 2 : %ld\n", res2);
  }

  pfileFree(pfile);
  return 0;
}
