#include <string>
#include <vector>
#include <algorithm>
#include <unordered_map>

using namespace std;

bool solution(vector<string> phone_book) {
    bool answer = true;
    int prefix_size;
    string to_cmp;

    sort(phone_book.begin(), phone_book.end());  // sort by the prefix char of the strings
    for (int i=0; i<phone_book.size()-1; i++) {
        prefix_size = phone_book[i].size();
        to_cmp = phone_book[i+1].substr(0, prefix_size);  // cmp with str right next to it
        if (to_cmp.compare(phone_book[i]) == 0) {         // whether phone_book[i] is a key of to_cmp or not
            return false;
        }
    }

    return answer;
}
