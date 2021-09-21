#include <string>
#include <vector>

using namespace std;

int checkDynamic(vector<int> numbers, int target, int memo, int running_idx) {
    // base case
    // check with memorized number and the last element calculation
    if (running_idx == numbers.size()-1) {
        if (memo + numbers[running_idx] == target ||
            memo - numbers[running_idx] == target)
            return 1;
        return 0;
    }

    // check two cases:
    // add the running_idx number to memo,
    // sub the running_idx number from memo
    return checkDynamic(numbers, target, memo+numbers[running_idx], running_idx+1) +
           checkDynamic(numbers, target, memo-numbers[running_idx], running_idx+1);

}

int solution(vector<int> numbers, int target) {
    int answer = 0;

    answer = checkDynamic(numbers, target, 0, 0);

    return answer;
}
