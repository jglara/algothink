#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <stdlib.h>

static const int MAX=2665;
static int primes[]={2,3,5,7,11,13,17,19,23,29,31,37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997, -1};

int
main(int argc, char *argv[])
{

  // read number of test cases
  std::string line;
  std::getline(std::cin,line);
  
  int numTests = atoi(line.c_str());

  // read lists of nth lucky numbers
  std::vector<int> nth_lucky_numbers;
  while(std::getline(std::cin,line)) {
    nth_lucky_numbers.push_back( atoi(line.c_str()) );
  }

  // precompute lucky numbers
  std::map<int,int> num_prime_factors;
  for (int i=0; primes[i]>0; i++) {
    for (int j=1; ; j++) {
      int num = j * primes[i];
      if (num > MAX) break;
      //std::cout << num << std::endl;
      ++ num_prime_factors[num];
      if (num_prime_factors[num] == 3) {
        std::cout << "Found " << num << std::endl;

      }

    }
  }


    // print wanted lucky numbers
  int num_lucky_numbers=0;
  std::vector<int>::iterator nth_lucky_number= nth_lucky_numbers.begin();
  for (int i =0; i < MAX; i ++) {
//    std::cout <<  i  << " " << num_prime_factors[i] << std::endl;
    if (num_prime_factors[i] >= 3) {

      if (++num_lucky_numbers == *nth_lucky_number) {
        std::cout <<  i << std::endl;
        if( ++nth_lucky_number == nth_lucky_numbers.end()) {
          return 0;
        };
      }
    }
  }

}
