/*
 * main.cc
 *
 *  Created on: Apr 29, 2015
 *      Author: ejogarv
 */

#include <vector>
#include <iostream>
using namespace std;

int main()
{

	// precalculate sum values
	vector<double> hangover_values;
	double value=0.0;
	for (int i=2; i<500; i++) {
		value += 1.0/i;
		hangover_values.push_back(value);
	}

	// read values and find them in the vector
	double input=0.0;
	cin >> input;
	while (input > 0.001) {

		// find the value
		int i=1;
		for(vector<double>::iterator it = hangover_values.begin();
				it != hangover_values.end();
				it++, i++) {

			if (*it > input) {
				cout << i << " card(s)" << endl;
				break;
			}
		}

		cin >> input;
	}
	return 0;


}




