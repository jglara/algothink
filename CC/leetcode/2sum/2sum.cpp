#include <iostream>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> twoSum_a(vector<int> &numbers, int target)
{
  map<int, int> mapping;
  vector<int> result;

  for(unsigned int i=0; i < numbers.size(); i++) {
    mapping[numbers[i]] = i;
  }

  for (unsigned int i=0; i < numbers.size(); i++) {
    int searched = target - numbers[i];
    if (mapping.find(searched) != mapping.end()) {
      result.push_back(i+1);
      result.push_back(mapping[searched]+1);
      break;
    }
  }
  return result;

}


// Node holds a reference to the value and the index
struct Node {
  int val_;
  int index_;
  Node(int val, int index) : val_(val), index_(index) { }
  bool operator<(const Node &other) const {
    return val_ < other.val_;
  }
};

vector<int> twoSum_b(vector<int> &numbers, int target)
{

  // construct the vector of nodes and sort it
  vector<Node> nodes;
  for (unsigned int i=0;  i< numbers.size(); i++) {
    nodes.push_back( Node(numbers[i], i) );
  }

  sort(nodes.begin(), nodes.end());

}

int main(int argc, char *argv[])
{
  vector<int> numbers;

  int num=0;
  while(cin >> num) {
    numbers.push_back(num);
  }

  int target=numbers.back();
  numbers.pop_back();

  vector<int> result = twoSum_a(numbers,target);

  if (result.size() == 2) {
    cout << "index1=" << result[0]
         << ",index2=" << result[1] << endl;
  }
}
