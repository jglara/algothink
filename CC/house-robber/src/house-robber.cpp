//============================================================================
// Name        : house-robber.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <stdlib.h>
#include <vector>
#include <iostream>
#include <iterator>
using namespace std;


class Solution {

public:
    int rob(vector<int>& nums) {
    	if (nums.size() == 0) { return 0; }
    	if (nums.size() == 1) { return nums[0]; }


    	vector<int> D(nums.size()+1);
    	D[0] = 0;
    	D[1] = nums[0];
    	D[2] = max (nums[0], nums[1]);

    	for (size_t i = 3; i<=nums.size(); i++) {


    		D[i] = max(D[i-1], nums[i-1]+D[i-2]);

    	}
    	return D[nums.size()];
    }
};

int main(int argc, char *argv[]) {

	Solution s;
	vector<int> houses;

	for (int i=1; i<argc; i++) {
		houses.push_back(atoi(argv[i]));
	}

	copy(houses.begin(), houses.end(), ostream_iterator<int>(cout, ","));

	cout << endl;

	cout << "Max rob value = " << s.rob(houses) << endl;

	return 0;
}
