#include <iostream>
#include <map>

int
main(int argc, char *argv[])
{
  std::string letters("ABCDEFGHIJKLMNOPQRSTUVWXYZ");
  std::string line;
  std::map<char, int> freq;

  //
  for (std::string::iterator letter=letters.begin(); letter!=letters.end(); letter++) {
    freq[*letter] = 0;
  }

  // readlines
  int max_freq=0;
  while(getline(std::cin, line)) {
    for (std::string::iterator it=line.begin(); it!=line.end(); it++) {
      std::map<char, int>::iterator it_freq= freq.find(*it);
      if (it_freq != freq.end()) {
        if (max_freq < ++ it_freq->second) {
          max_freq = it_freq->second;
        }
      }
    }
  }

  // print rows
  for (int row= max_freq; row!=0; row--) {
    // print columns
    std::string blanks;
    for (std::string::iterator letter=letters.begin(); letter!=letters.end(); letter++) {
      if (freq[*letter] >= row) {
        std::cout << blanks << "* ";
        blanks.clear();
      } else {
        blanks.push_back(' ');
        blanks.push_back(' ');
      }
    }
    std::cout << std::endl;
  }

  // print legend
  for (std::string::iterator letter=letters.begin(); letter!=letters.end(); letter++) {
    std::cout << *letter << " ";
  }
  std::cout << std::endl;

  // for (std::map<char, int>::iterator it = freq.begin(); it != freq.end(); it++) {
  //   std::cout << it->first << ": " << it->second << std::endl;
  // }

}
