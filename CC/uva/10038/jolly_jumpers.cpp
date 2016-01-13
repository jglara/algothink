#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>
#include <iterator>



int main(int argc, char *argv[])
{
  std::string line;
  while (getline(std::cin, line)) {

    // read line
    std::stringstream linestream(line);

    int size = 0;
    int n = 0;

    // read size
    linestream >> size;
    std::vector<int> vecNumbers;
    vecNumbers.reserve(size);
    bool isJolly=true;

//    std::cout << line << std::endl;
    // read size integers and put in a vector
    for (int i=0; i<size; i++) {
      linestream >> n;
      vecNumbers.push_back(n);

      if (i >= 2) {
        int diff2 = abs(vecNumbers[i] - vecNumbers[i-1]);
        int diff1 = abs(vecNumbers[i-1] - vecNumbers[i-2]);
//        std::cout << "   " << diff1 << " " << diff2 << std::endl;
        if ((diff1 - diff2) != 1) {
          isJolly = false;
          break;
        }
      }
    }

    if (isJolly) {
      std::cout << "Jolly" << std::endl;
    } else {
      std::cout << "Not jolly" << std::endl;
    }
    // std::copy(vecNumbers.begin(), vecNumbers.end(), std::ostream_iterator<int>(std::cout, " "));
    // std::cout << std::endl;
  }

}
