//============================================================================
// Name        : 1007.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <iterator>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

unsigned int calculateInversions(string str) {
	unsigned int inversions=0;
	for (size_t i=0; i< str.length(); i++) {
		for (size_t j=i; str[j]<str[j-1] && j >0; j-- ) {
			int temp= str[j];
			str[j] = str[j-1];
			str[j-1] = temp;
			inversions++;
		}
	}

	return inversions;
}



int main() {

	// read entries
	size_t num_entries=0;
	size_t len_entries=0;

	cin >> len_entries >> num_entries;

	priority_queue< pair<int,string> > q;

	for (size_t i =0; i < num_entries; i++) {
		string str;
		cin >> str;
		q.push(make_pair(- calculateInversions(str),str));
	}

	while (!q.empty()) {
		cout << q.top().second << endl;
		q.pop();
	}

	return 0;
}
