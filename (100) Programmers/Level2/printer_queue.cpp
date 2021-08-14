#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <utility>

using namespace std;

int solution(vector<int> priorities, int location) {
    int answer = 0;
    int target = 0;
    vector<pair<int, int> > priorities_pair;    // pair with (priority, index)

    // make the new priorities vector with pair
    for (int i=0; i<priorities.size(); i++) {
        priorities_pair.push_back(make_pair(priorities[i], i));
    }

    // sort the priorities (descending order)
    sort(priorities.begin(), priorities.end(), [](const auto& x, const auto& y) {return x > y;} );

    while (priorities.size()) {
        if (priorities_pair[target].first == priorities[0]) {   // if the target has the biggest priority
            priorities.erase(priorities.begin());
            target++;   // aim for the next target (this leads resizing the queue)
        }
        else {    // if not,
            // copy the target and paste it to the end
            priorities_pair.push_back(make_pair(priorities_pair[target].first,
                                                priorities_pair[target].second));
            // dequeue the target
            priorities_pair.erase(priorities_pair.begin()+target);
        }
    }

    // find the answer with the location
    while (priorities_pair[answer].second != location) answer++;

    return answer+1;

}
