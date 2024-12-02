#include "utils.hpp"

void printRunTime(long us)
{
	if (us < 1000)
	{
		cout << "Run time: " << us << "µs" << endl;
	}
	else if (us < 1000000)
	{
		cout << "Run time: " << us / 1000.0 << "ms" << endl;
	}
	else
	{
		cout << "Run time: " << us / 1000000.0 << "s" << endl;
	}
}

vector<string> split(string toparse, string delimiter)
{
	vector<string> tokens;
	size_t pos = 0;
	string token;
	while ((pos = toparse.find(delimiter)) != string::npos)
	{
		token = toparse.substr(0, pos);
		if (token.length() > 0)
		{
			tokens.push_back(token);
		}
		toparse.erase(0, pos + delimiter.length());
	}
	tokens.push_back(toparse);

	return tokens;
}

vector<long> extractLongs(string toparse) {

  vector<long> longs;

  int idx = 0;
  int length = toparse.length();
  const char* cstr = toparse.c_str();

  bool inNumber = false;
  bool isNeg = false;
  long current = 0;

  while(idx < length) {
    const char c = cstr[idx];

    if(inNumber == false) {
      if(c == '-') {
        inNumber = true;
        isNeg = true;
      } else if (c >= '0' && c <= '9') {
        inNumber = true;
        current = c - '0';
      }
    } else {
      if(c < '0' || c > '9') {
        current *= isNeg ? -1:1;
        longs.push_back(current);
        isNeg = false;
        inNumber = false;
        current = 0;
      } else {
        current *= 10;
        current += c - '0';
      }
    }

    idx++;
  }

  if(inNumber) {
    current *= isNeg ? -1:1;
    longs.push_back(current);
  }

  return longs;
}
