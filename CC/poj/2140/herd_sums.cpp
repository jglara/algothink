#include <iostream>

int
main(int argc, char *argv[])
{
  unsigned int input_n;
  
  // Read input: A single integer N
  std::cin >> input_n;

  unsigned int lo=1;
  unsigned int hi=1;
  unsigned int sum=0;

  unsigned int output_n=0;
  for (; ((hi<= input_n) || (lo <= input_n)); ) {
    if (sum == input_n) {
//      std::cout << "Found: [" << lo << ".." << hi << "]" << std::endl;
      ++output_n;
      sum -= lo;
      lo++;
    } else if (sum > input_n) {
      sum -= lo;
      lo++;
    } else {
      sum += hi;
      hi++;
    }

  }

  std::cout << output_n << std::endl;

}
