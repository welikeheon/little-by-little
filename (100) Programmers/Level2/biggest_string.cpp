#include <string>
#include <algorithm>
#include <vector>
#include <iostream>

using namespace std;

string solution(vector<int> numbers) {
    string answer = "";
    vector<vector<string>> numbers_extend;
    string tmp_str;

    // extend the string and save to the tmp vector with the original one
    // i.e. ["3030", "30"]  ["3133", "313"]
    for (int i=0; i<numbers.size(); i++) {
        tmp_str = to_string(numbers[i]);
        for (int j=0; tmp_str.size() != 4; j++) {
            tmp_str += tmp_str[j];
        }
        vector<string> tmp = {tmp_str, to_string(numbers[i])};
        numbers_extend.push_back(tmp);
    }

    // sort by extended string
    sort(numbers_extend.begin(), numbers_extend.end(),
        [](const vector<string>& v1, const vector<string>& v2) { return v1[0] > v2[0];} );
    
    // make the answer string
    for (int i=0; i<numbers_extend.size(); i++) {
        answer += numbers_extend[i][1];
    }

    // test case 11 (what if the array is full of '0' ?)
    for (int i=0; i<answer.size(); i++) {
        if (answer[i] != '0') break;
        if (i == answer.size()-1) return "0";
    }

    return answer;
}
