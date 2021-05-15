#include <cstdio>
#include <vector>

class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int nums_size = nums.size();
        int bound = nums_size-1;

        // when # nums is 1
        if(bound == 0 && nums[0] == val) return 0;
        else if(bound == 0 && nums[0] != val) return 1;

        for(int i=0; i<=bound; i++){
            if(nums[i] == val) {
                // decrease the bound until it reaches to the i'th index or
                // there is a position to be replaced
                while(bound >= i && nums[i] == nums[bound--])
                // nothing to do... just decrease the bound
                  ;
                swap(nums[i], nums[bound+1]);
            }
        }

        return bound+1;
    }
};
