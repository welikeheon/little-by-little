#include <cstdio>

class Solution {
public:
    ListNode* mergeInBetween(ListNode* list1, int a, int b, ListNode* list2) {
        if (list1 == NULL) return list2;
        if (list2 == NULL) return list1;

        ListNode* connect_from = list1;   // starts from the head of list1
        for (int i=0; i<a-1; i++) {  // connect_from should be the node right before the a's position
            connect_from = connect_from -> next;
        }

        ListNode* connect_end = connect_from;   // finding the end point
        for (int i=a-1; i<b+1; i++) {    // the journey's end... (found target for list2's end)
            connect_end = connect_end -> next;
        }

        // find the end point of list2
        ListNode* list2_end = list2;
        while (list2_end->next) {
            list2_end = list2_end -> next;
        }

        // connection
        connect_from -> next = list2;
        list2_end = connect_end;

        return list1;
    }
};
