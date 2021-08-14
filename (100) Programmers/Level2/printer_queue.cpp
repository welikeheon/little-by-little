#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int solution(vector<int> priorities, int location) {
    int answer = 0;
    vector<int> priorities_index; // the original location of the queuee
    vector<int> ordered_priorities; // the ordered queue

    for (int i=0; i<priorities.size(); i++) {
        priorities_index.push_back(i);  // match the initial location
    }

    while (priorities.size() >= 1) {  // O(n^2)
        // if the first element of the queue should be located at last,
        if (priorities[0] != *max_element(priorities.begin(), priorities.end())) {
            priorities.push_back(priorities[0]);  // move the element
            priorities.erase(priorities.begin());
            priorities_index.push_back(priorities_index[0]);  // move index too
            priorities_index.erase(priorities_index.begin());
        }
        else {  // if the first element has the highest priority and should be printed,
            ordered_priorities.push_back(priorities_index[0]);  // add to the ordered queue

            // dequeue the first one as no need to consider anymore
            priorities.erase(priorities.begin());
            priorities_index.erase(priorities_index.begin());
        }
    }

    while (ordered_priorities[answer] != location) answer++;

    return answer+1;

}
