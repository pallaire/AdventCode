#include "textlines.h"

TextLines* TextLinesAlloc() {
  TextLines* res = (TextLines*)malloc(sizeof(TextLines));
  if (res != NULL) {
      res->lines = (char**)malloc(TEXTLINES_LINES_ALLOC * sizeof(char*));
      res->lines[0] = NULL;
      res->lineCount = 0;
      res->maxLineCount = TEXTLINES_LINES_ALLOC;
  }
  return res;
}

void TextLinesFree(TextLines* tofree) {
  if(tofree) {
    if(tofree->lines[0]) {
      free(tofree->lines);
      tofree->lines = NULL; 
    }
    tofree->lineCount = 0;
    free(tofree);
  }
}

TextLines* TextLinesFromFile(const char* filename) {

  TextLines* res = TextLinesAlloc();
  if (res == NULL) {
      return NULL;
  }

  FILE* fID = fopen(filename, "r");
  if(fID == NULL) {
    printf("ERROR, TextLinesFromFile, could not open file %s\n", filename);
    return res;
  }

  fseek(fID, 0, SEEK_END);
  long file_length = ftell(fID);
  rewind(fID);

  // file_length + 1 to add a security 0 char at in end in 
  // case the file doesn't have a final \n
  char* buffer = malloc(sizeof(char) * (file_length + 1));
  buffer[file_length] = 0;

  fread(buffer, sizeof(char), file_length, fID);
  fclose(fID);

  bool newstring = true;
  for(int c = 0; c < file_length; c++) {
    char current = buffer[c];

    if(current == 0 || current == '\n' || current == '\r') {
      newstring = true;
      buffer[c] = 0;
    } else {
      if(newstring) {
        newstring = false;

        res->lines[res->lineCount] = buffer + c;
        res->lineCount++;
        if(res->lineCount == res->maxLineCount) {
          res->maxLineCount += TEXTLINES_LINES_ALLOC;
          res->lines = (char**)realloc(res->lines, res->maxLineCount * sizeof(char*));
        }
        res->lines[res->lineCount] = NULL;
      }
    }
  }

  return res;
}

void TextLinesExtractLongLong(const char* line, long long* outarray, long* arraysize) {
  if (outarray == NULL) {
    return;
  }

  unsigned long index = 0;
  long long work = 0;
  bool innumber = false;

  for (unsigned long i = 0; line[i] != '\0'; i++) {
    if (isdigit(line[i])) {
      work = work * 10 + (line[i] - '0');  // Build the number
      innumber = true;
    } else {
      if (innumber) {
        outarray[index] = work;
        work = 0;
        index++;
        innumber = false;
      }
    }
  }

  if (innumber) {
    outarray[index] = work;
    index++;
  }

  *arraysize = index;
}