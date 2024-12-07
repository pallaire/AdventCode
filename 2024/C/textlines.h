#ifndef TEXTLINES_H
#define TEXTLINES_H

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define TEXTLINES_LINES_ALLOC 64

typedef struct TextLines {
  char** lines;
  unsigned long lineCount;
  unsigned long maxLineCount;
} TextLines;

TextLines* TextLinesAlloc();
TextLines* TextLinesFromFile(const char* filename);

void TextLinesFree(TextLines* tofree);

void TextLinesExtractLongLong(const char* line, long long* outarray, long* arraysize);

#endif
