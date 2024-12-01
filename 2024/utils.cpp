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