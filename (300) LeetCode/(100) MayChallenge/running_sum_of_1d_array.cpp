#include <cstdio>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        for(int i=1; i<nums.size(); i++) {
          nums[i] += nums[i-1];
        }
        return nums;
    }
};

int main()
{
  Solution s;
  vector<int> test = {3,1,2,10,1};

  vector<int> runningSums = s.runningSum(test);
  for(int i=0; i<runningSums.size(); i++) printf("%d ", runningSums[i]);
  printf("\n");

  return 0;
}
