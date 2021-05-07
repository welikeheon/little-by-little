#include <cstdio>
#include <math.h>
#include <vector>

using namespace std;

class ListNode {
public:
  int val;
  ListNode *next;
  ListNode(int x) {
    val = x;
    next = NULL;
  }
};

class TreeNode {
public:
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode(int x) {
    val = x;
    left = NULL;
    right = NULL;
  }
};

class Solution {
public:

  // inorder traverse
  void treeTraverse(TreeNode* root) {
      if(root == NULL) return;
      treeTraverse(root->left);
      printf("%d ", root->val);
      treeTraverse(root->right);
  }

  TreeNode* makeChild(TreeNode* parent, vector<int> node_vector, int l, int r) {
    parent -> left = NULL;
    parent -> right = NULL;

    // base case (# vectors is 1)
    if(l >= r) {
      parent -> val = node_vector[r];
      return parent;
    }

    // finding the middle point
    int mid = (r+l)/2;
    int size = r-l+1;
    if(size % 2 == 0) mid++;  // when # vectors is even

    // divide and conquer
    parent -> left = makeChild(new TreeNode(NULL), node_vector, l, mid-1);
    if(mid+1 < r+1) // only do this if the parent has right childs (parent always has left child)
      parent -> right = makeChild(new TreeNode(NULL), node_vector, mid+1, r);
    parent -> val = node_vector[mid];

    return parent;
  }

  TreeNode* sortedListToBST(ListNode* head) {
    if(head == NULL) return NULL; // with empty linked list

    ListNode* runner = head;
    vector<int> node_vector;
    TreeNode* to_return;

    // convert linked list to a vector
    while(runner) {
      node_vector.push_back(runner->val);
      runner = runner -> next;
    }

    // make childs recursively
    to_return = makeChild(new TreeNode(NULL), node_vector, 0, node_vector.size()-1);
    treeTraverse(to_return);
    printf("\n");

    return to_return;

  }
};

int main() {
  Solution s;
  ListNode n1(-10);
  ListNode n2(-3);
  ListNode n3(0);
  ListNode n4(5);
  ListNode n5(9);

  n1.next = &n2;
  n2.next = &n3;
  n3.next = &n4;
  n4.next = &n5;
  n5.next = NULL;

  TreeNode* t = s.sortedListToBST(&n1);

  return 0;
}
