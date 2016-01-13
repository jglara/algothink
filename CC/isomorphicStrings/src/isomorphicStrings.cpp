//============================================================================
// Name        : isomorphicStrings.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    bool isIsomorphic(string s, string t) {
    	unsigned char tr[RADIX] = {0}; // mapping from s -> t
        unsigned char itr[RADIX] = {0}; // inverse mapping


        const unsigned int len=s.length();
        for (unsigned int i=0; i<len; i++) {
        	unsigned int sc=s[i];
        	unsigned int tc=t[i];
        	if (tr[sc] != 0) {

        		if (tr[sc] != t[i]) {
        			//cout << "tr[" << s[i] << "] = " << t[i] << " , " << tr[s[i]] << endl;
        			return false;
        		}

        	} else {
        		//cout << "Adding tr[" << s[i] << "] = " << t[i] << endl;
        		tr[sc] = t[i];
        	}


        	if (itr[tc] != 0) {

        		if (itr[tc] != s[i]) {
        			//cout << "itr[" << t[i] << "] = " << s[i] << " , " << itr[t[i]] << endl;
        			return false;
        		}

        	} else {
        		//cout << "Adding itr[" << t[i] << "] = " << s[i] << endl;
        		itr[tc] = s[i];
        	}

        }
    	return true;
    }

private:
    static const int RADIX=256;
};

int main(int argc, char *argv[]) {
	Solution s;


	cout << argv[1] << " and " << argv[2] << " are " << (s.isIsomorphic(argv[1], argv[2])?"":"not ") << "isomorphic" << endl;

}
