//============================================================================
// Name        : reverse-words-in-a-string.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>
#include <sstream>
#include <iterator>
using namespace std;

class Solution {
public:
    void reverseWords(string &s) {
    	vector<string> words;

    	istringstream instr(s);
    	while (!instr.eof()) {
    		string word;
    		instr >> word;

    		if (word.size() > 0) {
    			words.push_back(word);
    		}
    	}

    	s.clear();
    	bool first = true;
    	for (vector<string>::reverse_iterator it = words.rbegin(); it != words.rend(); ++it) {
    		if (first) {
    			first = false;
    		} else {
    			s.push_back(' ');
    		}
    		s.append(*it);
    	}

    	//copy(words.begin(), words.end(), ostream_iterator<string>(cout, ","));



    }
};

int main() {

	Solution s;
	//string str("the sky is blue");
	string str("a");

	//std::getline(cin,str);
	s.reverseWords(str);

	cout << "'" << str << "'" << endl;

}
