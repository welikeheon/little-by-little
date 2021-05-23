#include <cstdio>

using namespace std;

class ListNode {
public:
  int val;
  ListNode* next;
  ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* prev = NULL;
        ListNode* runner = NULL;
        ListNode* to_go = NULL;
        if(head) prev = head; else return NULL;
        if(head->next) runner = head->next; else return prev;

        prev -> next = NULL;  // first prev should point nothing
        while((to_go = runner -> next)) {
            runner -> next = prev;
            prev = runner;
            runner = to_go;
        }
        runner -> next = prev;
        return runner;
    }
};

int main() {
  ListNode n5(5, NULL);
  ListNode n4(4, &n5);
  ListNode n3(3, &n4);
  ListNode n2(2, &n3);
  ListNode n1(1, &n2);

  Solution s;
  ListNode* result = s.reverseList(&n1);
  while(result) {
    printf("%d ", result->val);
    result = result -> next;
  }

  return 0;
}
