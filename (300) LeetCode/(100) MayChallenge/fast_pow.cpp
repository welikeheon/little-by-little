#include <iostream>
#include <vector>

class Solution {
public:
    double myPow(double x, int n) {
      // base cases
      if(x == 0 || x == 1) return x;
      if(n == 0) return 1;
      if(n == 1) return x;
      if(n == 2) return x * x;
      if(n == -1) return 1 / x;
      if(n == -2) return 1 / (x * x);

      int n_half = n/2;
      int n_remainer = n-(2*(n/2)); // you may see this is meaningless, but acturally it isn't

      double pow_half = myPow(x, n_half);
      double pow_remainder = myPow(x, n_remainer);
      return pow_half * pow_half * pow_remainder; // dynamic programming
    }
};

int main() {
  Solution *s = new Solution();
  printf("%lf", s->myPow(2.0, -3));

  return 0;
}
