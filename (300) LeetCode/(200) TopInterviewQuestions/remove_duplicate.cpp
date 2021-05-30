#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if(nums.size() == 1 || nums.size() == 0) return nums.size();
        int tmp = nums[0];

        for(int i=1; i<nums.size(); i++) {
          if(tmp != nums[i]) {  // if there is a different unique element,
            tmp = nums[i];
          }
          else {  // tmp == nums[i]
            nums.erase(nums.begin()+i); // remove i'th element
            i--;  // recover for the next compare
          }
        }

        return nums.size();
    }
};

int main() {
  Solution s;
  vector<int> nums = {0,0,1,1,1,2,2,3,3,4};
  cout << s.removeDuplicates(nums) << endl;

  return 0;
}
