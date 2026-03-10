#include "plib.h"


PFile* pfileReadAll(const char* path) {
  if(!path) {
    return nullptr;
  }

  FILE* file = fopen(path, "r");

  if(!file) {
    return nullptr;
  }

  PFile* pfile = (PFile*)calloc(1, sizeof(PFile));

  if(!pfile) {
    goto pfilereadcleanup;
  }

  fseek(file, 0, SEEK_END);
  pfile->size = ftell(file);
  rewind(file);

  pfile->data = (char*)malloc(pfile->size + 1);
  if(!pfile->data) {
    goto pfilereadcleanup;
  }
  pfile->data[0] = 0;
  pfile->data[pfile->size] = 0;
      
  if(fread(pfile->data, sizeof(char), pfile->size, file) != pfile->size) {
      goto pfilereadcleanup;
  }
  return pfile;

pfilereadcleanup:
  fclose(file);
  pfileFree(pfile);
  return nullptr;
}

void pfileFree(PFile* pfile) {
  if(pfile) {
    if(pfile->data) {
      free(pfile->data);
    }
    if(pfile->lines) {
      free(pfile->lines);
    }
    free(pfile);
  }
}

void pfileFixLines(PFile* pfile) {
  if(pfile->lines) {
    return;
  }

  pfile->lines = (char**)malloc(sizeof(char*) * 8192);

  if(!pfile->lines) {
    return;
  }

  u64 idx = 0;
  pfile->lines[0] = pfile->data;
  pfile->linesCount = 1;

  while(idx < pfile->size) {
    if(pfile->data[idx] == 0) {
      return;
    }

    if(pfile->data[idx] == '\n') {
      pfile->data[idx] = 0;
      pfile->lines[pfile->linesCount] = pfile->data + idx + 1;
      pfile->linesCount++;
    }
    idx++;
  }
}

