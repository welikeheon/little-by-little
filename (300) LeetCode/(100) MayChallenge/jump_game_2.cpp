#include <cstdio>
#include <vector>

using namespace std;

class Solution {
public:
    int jump(vector<int>& nums) {
        int max_jump_loc = 0;
        int current = 0;
        int count = 0;

        for(int i=0; i<nums.size()-1; i++) {

          // who is going to jump more?
          max_jump_loc = max(max_jump_loc, nums[i]+i);

          if(i == current) {
            current = max_jump_loc; // current(target) is maximum jumpable location
            count++;  // count up when i reaches to the target
          }
        }
        return count;
    }
};

int main()
{
  Solution s;
  vector<int> test = {2,3,1,1,4};

  printf("%d\n", s.jump(test));

  return 0;
}
