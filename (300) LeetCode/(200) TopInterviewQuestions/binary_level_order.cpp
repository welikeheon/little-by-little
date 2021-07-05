#include <cstdio>
#include <vector>
#include <stdlib.h>
#include <math.h>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    vector<vector<int> > levelOrder(TreeNode* root) {
      vector<vector<int> > result;
      vector<TreeNode*> q;
      vector<int> *nodes_in_level;
      TreeNode* p_node;
      int cur_level = 0;
      int cnt = 1;

      if (!root) return result;

      // push the root first
      q.push_back(root);
      nodes_in_level = new vector<int>{root->val};
      result.push_back(*nodes_in_level);
      cur_level++;
      cnt++;

      while(!q.empty()) {
        // todo1
        if(cnt == pow(2, cur_level)) {
          nodes_in_level = new vector<int>;
          cur_level++;
          cnt = 0;
        }
        p_node = q.front();

        if(p_node->left) {
          nodes_in_level->push_back(p_node->left->val);
          q.push_back(p_node->left);  // enqueue
        }

        if(p_node->right){
          nodes_in_level->push_back(p_node->right->val);
          q.push_back(p_node->right); // enqueue
        }
        cnt += 2;

        if(!nodes_in_level->empty()) result.push_back(*nodes_in_level);
        q.erase(q.begin()); // dequeue
      }
      return result;
    }
};

int main() {
  Solution s;

  TreeNode *n1 = (TreeNode*)malloc(sizeof(TreeNode));
  n1 -> val = 1;
  TreeNode *n2 = (TreeNode*)malloc(sizeof(TreeNode));
  n2 -> val = 2;
  TreeNode *n3 = (TreeNode*)malloc(sizeof(TreeNode));
  n3 -> val = 3;
  TreeNode *n4 = (TreeNode*)malloc(sizeof(TreeNode));
  n4 -> val = 4;
  TreeNode *n5 = (TreeNode*)malloc(sizeof(TreeNode));
  n5 -> val = 5;

  n1 -> left = n2;
  n1 -> right = n3;

  n2 -> left = n4;
  n2 -> right = NULL;

  n3 -> left = NULL;
  n3 -> right = n5;

  n4 -> left = NULL;
  n4 -> right = NULL;

  n5 -> left = NULL;
  n5 -> right = NULL;

  vector<vector<int> > arr_level_order = s.levelOrder(n1);
  for(int i=0; i<arr_level_order.size(); i++) {
    for(int j=0; j<arr_level_order[i].size(); j++) {
      printf("%d ", arr_level_order[i][j]);
    }
    printf("\n");
  }


  return 0;
}
