#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    int singleNumber(vector<int>& nums) {
      int to_return = 0;
      for(int i=0; i<nums.size(); i++) {
          to_return ^= nums[i];
      }

      return to_return;
    }
};

int main() {
  vector<int> test_case = {4,1,2,1,2};
  Solution s;

  cout << s.singleNumber(test_case) << endl;

}
