#include <cstdio>
#include <vector>

using namespace std;

class Solution {
public:
    void rotate(vector<vector<int> >& matrix) {
      int col_size = matrix.size();
      int row_size = matrix[0].size();

      // no need other base cases as this problem only deals n x n matrix

      // transpose the matrix
      for(int i=0; i<row_size-1; i++) {
        for(int j=i+1; j<col_size; j++) {
          swap(matrix[i][j], matrix[j][i]);
        }
      }

      // flip horizontally
      for(int i=0; i<row_size; i++) {
        for(int j=0; j<col_size/2; j++) {
          swap(matrix[i][j], matrix[i][col_size-1-j]);
        }
      }
    }
};

int main() {
  vector<vector<int> > matrix = {{0,1}};
  Solution s;
  s.rotate(matrix);

  // test
  for(int i=0; i<matrix.size(); i++) {
    for(int j=0; j<matrix[0].size(); j++) {
      printf("%d ", matrix[i][j]);
    }
    printf("\n");
  }

  return 0;
}
