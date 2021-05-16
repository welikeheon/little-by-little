#include <cstdio>
#include <vector>

using namespace std;

class Solution {
public:
    // create a powerset
    vector<vector<int> > powerSet(vector<int>& nums) {
        int nums_size = nums.size();
        vector<vector<int> > powerset;
        vector<int> subset;

        for(int i=0; i<pow(2, nums_size); i++) {
            subset.clear();
            for(int j=0; j<nums_size; j++) {
                if(i & (1 << j)) subset.push_back(nums[j]);   // magic!
            }
            powerset.push_back(subset);
        }
        return powerset;
    }

    int subsetXORSum(vector<int>& nums) {
        if(nums.empty()) return 0;  // do nothing with the empty nums vector

        vector<vector<int> > powerset = powerSet(nums);
        vector<int> xor_lst;  // append every result of xor
        int tmp;  // var. for xor result
        int result = 0;

        for(int i=1; i<powerset.size(); i++) {  // discard the empty vector (the first one)
          tmp = 0;
          for(int j=0; j<powerset[i].size(); j++) { // for each subset
            tmp = tmp ^ powerset[i][j];
          }
          xor_lst.push_back(tmp);
        }

        result = 0;
        for(int i=0; i<xor_lst.size(); i++) { // add every xor result
          result += xor_lst[i];
        }
        return result;
    }
};

int main() {
  Solution s;
  vector<int> test;
  test.push_back(1);
  test.push_back(3);
  printf("%d\n", s.subsetXORSum(test));
  return 0;
}
