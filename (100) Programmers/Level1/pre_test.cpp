#include <string>
#include <vector>
#include <utility>
#include <algorithm>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> answers) {
    vector<int> answer;

    vector<int> student1 = {1, 2, 3, 4, 5};
    vector<int> student2 = {2, 1, 2, 3, 2, 4, 2, 5};
    vector<int> student3 = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
    int student1_correct = 0;
    int student2_correct = 0;
    int student3_correct = 0;
    vector<pair<int, int> > correct_num_pair;
    int runner = 1;

    for (int i=0; i<answers.size(); i++){
        if (student1[i%5] == answers[i]) student1_correct++;
    }
    correct_num_pair.push_back(make_pair(1, student1_correct));

    for (int i=0; i<answers.size(); i++){
        if (student2[i%8] == answers[i]) student2_correct++;
    }
    correct_num_pair.push_back(make_pair(2, student2_correct));

    for (int i=0; i<answers.size(); i++){
        if (student3[i%10] == answers[i]) student3_correct++;
    }
    correct_num_pair.push_back(make_pair(3, student3_correct));

    sort(correct_num_pair.begin(), correct_num_pair.end(), [](const auto& x,
                                                              const auto& y){return x.second > y.second;} );

    answer.push_back(correct_num_pair[0].first);
    if (correct_num_pair[1].second == correct_num_pair[0].second) answer.push_back(correct_num_pair[1].first);
    if (correct_num_pair[2].second == correct_num_pair[0].second) answer.push_back(correct_num_pair[2].first);

    return answer;
}
