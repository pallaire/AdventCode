#define _POSIX_C_SOURCE 199309L

#include "plib.h"


#include <time.h>
u64 ustimestamp() {
  struct timespec ts;
  clock_gettime(CLOCK_REALTIME, &ts);
  return (u64) ((ts.tv_sec * 1000000) + (ts.tv_nsec / 1000));
}

void printtimestamp(u64 t, const char* name) {
  if(t < 1000) {
    printf("Chrono : %s : Total runtime : %ldμs  ---> %0.6fs\n", name, t, t/1000000.0f);
  } else if (t < 1000000) {
    printf("Chrono : %s : Total runtime : %ldms  ---> %0.3fs\n", name, t, t/1000.0f);
  } else {
    printf("Chrono : %s : Total runtime : %lds\n", name, t);
  }
}

int main(int /*argc*/, char** /*argv*/) {
  u64 start = ustimestamp();

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
        pos -= num;
        if(pos < 0) {
          // If we started at 0, then we didnt cross it
          if(startpos != 0) {
            res2++;
          }
          pos += 100;
        }
      } else {
        pos += num;
        if(pos >= 100) {
          // 100 will be handled by 0 below
          if(pos > 100) {
            res2++;
          }
          pos -= 100;
        }
      }

      if(pos == 0) {
        res++;
        if(num != 0) {
          res2++;
        }
      }

      startpos = pos;
    }

    printf("problem 1 : %ld\n", res);
    printf("problem 2 : %ld\n", res2);
    printtimestamp(ustimestamp()-start, "Total");
  }



  pfileFree(pfile);

  return 0;
}
