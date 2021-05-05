#include <cstdio>
#include <vector>

using namespace std;

class Solution {
public:
    bool checkPossibility(vector<int>& nums) {
      int cnt = 0;  // # decreasing point

      for(int i=0; i<nums.size()-1; i++) {
        if(nums[i] > nums[i+1]) {
          if(++cnt > 1) return false; // when modify happens more than once

          // to determine which element should be changed
          if(i+2 < nums.size() && nums[i] > nums[i+2]) nums[i] = nums[i+1];
          else nums[i+1] = nums[i];

          i = -1;    // start over again to look up more decreasing point
        }
      }
      return true;
    }
};

int main()
{
  Solution s;
  vector<int> test = {3,4,2,3};

  printf("%s\n", s.checkPossibility(test) ? "True" : "False");

  return 0;
}
