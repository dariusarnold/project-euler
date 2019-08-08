#include <iostream>
#include <unordered_set>
#include <cmath>
#include <numeric>

using big_int = unsigned long int;


big_int SIGMA2(big_int n){
    /*
     * Return sum of sum of squares of the divisors of all numbers from 1 to n
     *  n: divisors
     *  1: 1
     *  2: 1 2
     *  3: 1   3
     *  4: 1 2   4
     *  5: 1       5
     *  6: 1 2 3     6
     *  7: 1           7
     *  8: 1 2   4       8
     *  9: 1   3           9
     * 10: 1 2     5         10
     * 11: 1                    11
     * 12: 1 2 3 4   6             12
     *
     *  1: 1 2 3 4 5 6 7 8 9 10 11 12
     *  2: 1 2 3 4 5 6
     *  3: 1 2 3 4
     *  4: 1 2 3
     *  5: 1 2
     *  6: 1 2
     *  7: 1
     *  8: 1
     *  9: 1
     * 10: 1
     * 11: 1
     * 12: 1
     */
    big_int result = 0;
    for (big_int i = 1; i <= n; ++i){
        result += (n / i) * i*i;
        result %= 1000'000'000;
    }
    return result;
}


int main(){
    std::cout << SIGMA2(static_cast<big_int>(std::pow(10, 15)));
}