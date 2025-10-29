#ifndef __PFILE__
#define __PFILE__

#include <cstring>
#include <string>
#include <vector>

using namespace std;

class PFile {
public:
  PFile(string filepath);
  ~PFile();

  long long getSize();
  char* getRawData();
  vector<string> getDataOfStrings();
  vector<long> getDataOfNumbers();

  static string getDataPathFromArgs(int argc, char** argv);

private:
  string _filepath;
  long long _size;
  char* _data;  
};

#endif
