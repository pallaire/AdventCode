#define  _POSIX_C_SOURCE 199309L // to enable clock_gettime from time.h
#include <stdio.h>
#include <time.h>
#include "plib.h"

u64 pchronoGetMicroSeconds() {
  struct timespec ts;
  clock_gettime(CLOCK_REALTIME, &ts);
  return (u64) ((ts.tv_sec * 1000000) + (ts.tv_nsec / 1000));
}

void pchronoPrint(u64 ts, const char* label) {
  if(ts < 1000) {
    printf("Chrono : %s : Total runtime : %ldμs  ---> %0.6fs\n", label, ts, ts/1000000.0f);
  } else if (ts < 1000000) {
    printf("Chrono : %s : Total runtime : %ldms  ---> %0.3fs\n", label, ts, ts/1000.0f);
  } else {
    printf("Chrono : %s : Total runtime : %lds\n", label, ts);
  }
}
