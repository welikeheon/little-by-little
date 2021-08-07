#include <string>
#include <vector>
#include <unordered_map>
#include <iostream>
using namespace std;

int solution(vector<vector<string>> clothes) {
    int answer = 1;
    unordered_map<string, int> clothes_map;

    // create unsorted map to find out the combination numbers
    for (auto str : clothes) {
        if (clothes_map.find(str[1]) == clothes_map.end()) {
            clothes_map[str[1]] = 1;
        }
        else clothes_map[str[1]]++;
    }

    // use the combination method
    unordered_map<string, int>:: iterator it;
    for(it = clothes_map.begin(); it != clothes_map.end(); it++) {
        answer *= it->second + 1;
    }

    return answer - 1;  // wear at least one cloth
}
