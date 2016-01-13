//============================================================================
// Name        : 2136.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <map>
using namespace std;

int main() {
	map<char,int> histogram;

	const static int NUM_LINES=4;

	int max_value=0;
	for (int i=0; i<NUM_LINES; i++) {
		string line;
		getline(cin, line);

		//cout << "line: " << line << endl;

		for (string::iterator it=line.begin(); it != line.end(); ++it) {
			//cout << *it << " = " << histogram[*it] << endl;
			if (isalpha(*it)) {
				int value = histogram[*it] ++;
				if (value > max_value) {
					max_value= value;
				}
			}
		}
	}

//	for (char c='A'; c != 'Z'; c++) {
//		cout << c << " = " <<histogram[c] << endl;
//	}

	for (int i=max_value;i>0;i--) {
		int count_whites=0;
		bool first=true;
		for (char c='A'; c <= 'Z'; c++) {
			if (histogram[c]>=i) {
				cout << string((count_whites*2)+(first?0:1), ' ') << "*";
				count_whites=0;
				first=false;
			} else {
				++count_whites;
			}
		}
		cout << endl;
	}

	cout << "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z" << endl;



}
