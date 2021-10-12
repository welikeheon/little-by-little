#include <string>
#include <vector>

using namespace std;

string solution(string numbers, int k) {
    string answer = "";
    vector<char> stk;
    for (auto number : numbers) {
        while (stk.size() && k > 0 && stk[stk.size()-1] < number) {
            k--;
            stk.pop_back();
        }
        stk.push_back(number);
    }

    for (int i=0; i<stk.size()-k; i++)
        answer += stk[i];

    return answer;
}
