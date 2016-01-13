//============================================================================
// Name        : 1004.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

const static int MONTHS=12;
int main() {

	double n = 0;
	double total = 0;
	for (int m=0; m<MONTHS; m++) {
		cin >> n;
		total += n;
	}

	cout << "$" << total / MONTHS << endl;

	return 0;
}
