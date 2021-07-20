#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    void moveZeroes(vector<int>& nums) {
      int last_zero = 0;

      // move all non-zero elements to the front
      for(int i=0; i<nums.size(); i++) {
        if(nums[i] != 0)
          nums[last_zero++] = nums[i];
      }

      // set the remaining zeros at the end
      for(int i=last_zero; i<nums.size(); i++) {
        nums[i] = 0;
      }
    }
};

int main() {
  Solution s;
  vector<int> nums{0,0,0,3,4,5,0,8};
  s.moveZeroes(nums);

  for(auto num : nums) cout << num << endl;

  return 0;
}
