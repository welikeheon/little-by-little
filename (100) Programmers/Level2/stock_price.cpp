#include <string>
#include <vector>
#include <stack>
#include <utility>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> prices) {  // consider the prices vector as a queue
    vector<int> answer(prices.size());
    stack<pair<int, int> > stk; // stack with <time, price>

    // using stack -- O(n)
    for (int i=0; i<prices.size()-1; i++) {
        if (stk.empty()) {  // push first on empty stack
            stk.push(make_pair(i+1, prices[i]));
        }
        else {
            if (stk.top().second > prices[i]) { // price dropped,
                while(!stk.empty() && stk.top().second > prices[i]) {
                    // does not have to go through every index!! ( as it takes O(n^2) )
                    // just pop and calculate the time until the top of stack price is bigger
                    // when the top of stack price is bigger than the prices[i], i := i+1
                    answer[stk.top().first - 1] = (i+1) - stk.top().first;
                    stk.pop();
                }
            }
            stk.push(make_pair(i+1, prices[i]));
        }
    }

    // now, the rest
    while (!stk.empty()) {
        answer[stk.top().first - 1] = prices.size() - stk.top().first;
        stk.pop();
    }
    answer[answer.size()-1] = 0;

    return answer;
}
