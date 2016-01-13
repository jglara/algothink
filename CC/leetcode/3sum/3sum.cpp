#include <iostream>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

vector< vector<int> > threeSum(vector<int> &numbers)
{

  vector< vector<int> > result;

  sort(numbers.begin(), numbers.end());

  for (unsigned int i=0; i<numbers.size(); i++) {

    int target = - numbers[i];

    int start=i+1;
    int end=numbers.size() - 1;

    while (start < end) {

      int sum= numbers[start] + numbers[end];
      if (sum == target) {
        // found, add it to the list
        vector <int> solution;
        solution.push_back(numbers[i]);
        solution.push_back(numbers[start]);
        solution.push_back(numbers[end]);

        start ++; end--;
      } else if (sum < target) {
        start++;
      } else {
        end--;
      }

    }


  }

  return result;

}


////////////////////////////////////////////////////////////////////////////////
int main(int argc, char *argv[])
{
  vector<int> numbers;

  int num=0;
  while(cin >> num) {
    numbers.push_back(num);
  }

  vector< vector<int> > result = threeSum(numbers);

  for (unsigned int i=0; i< result.size(); i++) {
    vector<int> triplet = result[i];
    cout << "(" << triplet[0] << "," << triplet[1] << "," << triplet[2] << ")" << endl;
  }
}
