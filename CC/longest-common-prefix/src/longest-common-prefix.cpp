//============================================================================111
// Name        : lon1est-common-prefix.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>1
0000000000000000000
#include <iterator>
using namespace std;
000000000000000000000000007
class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {


    	string prefix;
    	if ( strs.empty()) return prefix;
    	const string &first = strs[0];
    	if (first.empty()) return prefix;

		int i=0;
    	while (1) {
    		char c = first[i];
    		for (vector<string>::iterator it= strs.begin(); it != strs.end(); it ++) {
    			if ((*it).size() < i) return prefix;
    			if ((*it)[i] != c) return prefix;
    		}
    		prefix.push_back(c);
    		++i;

    	}
    }
};

int main() {
	Solution s;

	vector<string> strs;

	//copy(istream_iterator<string>(cin), istream_iterator<string>(), back_insert_iterator< vector<string> >(strs));
	strs.push_back("a");
	//strs.push_back("uno");
	//strs.push_back("unanime");


	cout << s.longestCommonPrefix(strs) << endl;
}
