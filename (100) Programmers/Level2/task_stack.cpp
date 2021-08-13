#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    // progresses -- the tasks stk.
    // speeds -- the adder stk.

    vector<int> answer;     // asnwer stk.
    int push_numb = 0;      // the number of tasks which is needed to push to the answer

    while(progresses.size() > 0) {  // while there is smt. in the progress stk.
        for(int i=0; i<progresses.size(); i++) {
            if (progresses[i] < 100) progresses[i] += speeds[i];
        }

        // pop the every completed task while the top is >= 100
        while(progresses.size() > 0 && progresses[0] >= 100) {
            progresses.erase(progresses.begin());   // pop the top of progresses stk.
            speeds.erase(speeds.begin());           // pop the speeds stk. as well
            push_numb++;
        }

        // push to the answer stk with the push_numb
        if(push_numb > 0) {
            answer.push_back(push_numb);
            push_numb = 0;
        }
    }

    return answer;
}
