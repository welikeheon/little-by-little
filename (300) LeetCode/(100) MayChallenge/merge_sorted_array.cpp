#include <vector>
#include <cstdio>

using namespace std;

class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
      if (n == 0) return;

      int runner1 = 0;

      while(n != 0 && runner1 < nums1.size()) {
        if(nums1[runner1] >= nums2[0]) {    // found location to inserst,
          nums1.insert(nums1.begin()+runner1, nums2[0]); // insert the nums2 element
          nums2.erase(nums2.begin()); // erase the inserted element
          n--;
          nums1.pop_back(); // pop the last element of nums1 (which is 0)
        }
        runner1++;
      }

      runner1 = runner1 - n;
      while(n > 0) {    // if nums2 still has something
        nums1.insert(nums1.begin()+runner1, nums2[0]);
        nums2.erase(nums2.begin());
        n--;
        nums1.pop_back();
        runner1++;
      }
    }
};

int main() {
  Solution s;
  vector<int> t1 = {4, 0,0,0,0,0};
  vector<int> t2 = {1,2,3,5,6};
  s.merge(t1, 1, t2, 5);
  for(int i=0; i<6; i++) {
    printf("%d ", t1[i]);
  }
  printf("\n");
  return 0;
}
