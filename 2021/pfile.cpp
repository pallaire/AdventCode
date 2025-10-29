
#include <cstdlib>
#include <format>
#include <fstream>
#include <iostream>
#include <vector>

#include "pfile.h"

PFile::PFile(string filepath) {
  _filepath = filepath;
  _size = 0;
  _data = nullptr;

  ifstream file(_filepath);

  if (!file.is_open()) {
    cerr << "Error opening file! : " << _filepath << std::endl;
    exit(EXIT_FAILURE);
  }

  file.seekg(0, std::ios::end);
  _size = file.tellg();
  file.seekg(0, std::ios::beg);

  _data = new char[_size];

  if (!file.read(_data, _size)) {
    cerr << "Error reading file! : " << _filepath << std::endl;
    exit(EXIT_FAILURE);
  }

  file.close();
}

PFile::~PFile() {
  if(_data != nullptr) {
    delete[] _data;
  }
}

long long PFile::getSize() {
  return _size;
}

char* PFile::getRawData() {
  return _data;
}

string PFile::getDataPathFromArgs(int argc, char** argv) {
  string path = format("./data/day{:02d}.txt", DAY_NUM);

  for(int a = 0; a < argc; a++) {
    if(strcmp(argv[a], "-t") == 0 && a < argc-1) {
      path = format("./data/day{:02d}_test{:02d}.txt", DAY_NUM, atoi(argv[a+1]));
      break;
    }
  }

  return path;
}

vector<string> PFile::getDataOfStrings() {
  vector<string> res;

  char* start = nullptr;

  for(int i = 0; i < _size; i++) {
    if(_data[i] == '\n' || _data[i] == 0) {
      _data[i] = 0;
      res.push_back(string(start));
      _data[i] = '\n';
      start = nullptr;
    } else if (start == nullptr){
      start = _data + i;
    }
  }

  if(start != nullptr) {
    res.push_back(string(start));
  }

  return res;
}

vector<long> PFile::getDataOfNumbers() {
  vector<long> res;

  char* start = nullptr;

  for(int i = 0; i < _size; i++) {
    if(_data[i] == '\n' || _data[i] == 0) {
      _data[i] = 0;
      res.push_back(atol(start));
      _data[i] = '\n';
      start = nullptr;
    } else if (start == nullptr){
      start = _data + i;
    }
  }

  if(start != nullptr) {
    res.push_back(atol(start));
  }

  return res;
}
