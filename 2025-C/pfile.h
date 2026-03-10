#ifndef __PFILE__
#define __PFILE__

#include "plib.h"

typedef struct {
  u64 size;
  c8* data;
  c8** lines;
  u64 linesCount;
} PFile;

PFile* pfileReadAll(const char* path);
void pfileFree(PFile* file);
void pfileFixLines(PFile* pfile);

#endif //__PFILE__

