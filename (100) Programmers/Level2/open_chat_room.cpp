#include <string>
#include <vector>
#include <unordered_map>
#include <iostream>
#include <algorithm>

using namespace std;

// create hash map with pair(ID, NAME)
unordered_map<string, string> create_map(const vector<string>& record) {
    unordered_map<string, string> id_name_map;

    for (string line : record) {
        int i;
        if (line[0] == 'E') {
            for (i=6; line[i] != ' '; i++);

            // if the key does not exist,
            if (id_name_map.find(line.substr(6, i-6)) == id_name_map.end())
                id_name_map.insert(make_pair(line.substr(6, i-6), line.substr(i+1, line.size()-i)));
            else    // if the key exist, this is same as changing
                id_name_map[line.substr(6, i-6)] = line.substr(i+1, line.size()-i);
        }
        else if (line[0] == 'C') {  // change name
            for (i=7; line[i] != ' '; i++);
            id_name_map[line.substr(7, i-7)] = line.substr(i+1, line.size()-i);
        }
    }

    return id_name_map;
}

vector<string> solution(vector<string> record) {
    vector<string> answer;
    unordered_map<string, string> id_name_map = create_map(record);

    for (string line : record) {
        int i;
        string tmp;
        if (line[0] == 'E') {
            for (i=6; i < line.size() && line[i] != ' '; i++);
            tmp += id_name_map[line.substr(6, i-6)] + "님이 들어왔습니다.";
            answer.push_back(tmp);
        }

        if (line[0] == 'L') {
            for (i=6; i < line.size() && line[i] != ' '; i++);
            tmp += id_name_map[line.substr(6, i-6)] + "님이 나갔습니다.";
            answer.push_back(tmp);
        }
    }

    return answer;
}
