#include <string>
#include <vector>
#include <utility>
#include <iostream>

using namespace std;

int solution(int bridge_length, int weight, vector<int> truck_weights) {
    int answer = 0;
    int cur_weight = 0;
    vector<pair<int, int> > bridge_queue;  // pair has <truck_weight, process time>

    do {
        if (bridge_queue.size()) {  // if there are some trucks crossing,
            for (int i=0; i<bridge_queue.size(); i++) {
                bridge_queue[i].second--;  // clocks ticking for the trucks
            }

            if (bridge_queue[0].second == 0) { // if the front truck reaches to the end
              cur_weight -= bridge_queue[0].first;
              bridge_queue.erase(bridge_queue.begin());
            }
        }

        if (truck_weights.size() && // if there are trucks still out there,
        bridge_queue.size()+1 <= bridge_length && // if there is enough space for a new truck,
        cur_weight+truck_weights[0] <= weight) {  // if the bridge can hold a new truck,

            cur_weight += truck_weights[0];
            bridge_queue.push_back(make_pair(truck_weights[0], bridge_length)); // bridge enqueue
            truck_weights.erase(truck_weights.begin()); // truck stack pop
        }
        answer++; // clocks ticking for overall
    } while (bridge_queue.size() || truck_weights.size());

    return answer;
}

int main() {
  vector<int> truck_weights = {7, 4, 5, 6};
  cout << solution(2, 10, truck_weights) << endl;

  return 0;
}
