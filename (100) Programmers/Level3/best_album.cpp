#include <string>
#include <vector>
#include <map>
#include <iostream>
#include <algorithm>

using namespace std;

struct info {
    string genre_;
    int plays;
    int idx;
    int sum;
};

vector<int> solution(vector<string> genres, vector<int> plays) {
    vector<int> answer;
    map<string, int> total_plays_map;
    vector<info> info_table;

    // create map
    for (int i=0; i<genres.size(); i++) {
        total_plays_map[genres[i]] += plays[i];
    }

    // create information table
    for (int i=0; i<genres.size(); i++) {
        info e;
        e.genre_ = genres[i];
        e.plays = plays[i];
        e.idx = i;
        e.sum = total_plays_map[genres[i]];
        info_table.push_back(e);
    }

    // sort by genre string
    sort(info_table.begin(), info_table.end(),
        [] (const auto& e1, const auto& e2) { return e1.genre_ > e2.genre_; });

    // sort again by total play sum (to properly sort when the total play sum is equal)
    sort(info_table.begin(), info_table.end(),
        [] (const auto& e1, const auto& e2) { return e1.sum > e2.sum; });

    // sort the each genre by plays
    int from = 0;
    int to = 1;
    for(; to<info_table.size(); to++) {
        if(info_table[from].genre_ == info_table[to].genre_) continue;

        sort(info_table.begin()+from, info_table.begin()+to,
            [] (const auto& e1, const auto& e2) { return e1.plays > e2.plays; });
        from = to;
    }

    // sort the rest of the info_table
    sort(info_table.begin()+from, info_table.begin()+to,
            [] (const auto& e1, const auto& e2) { return e1.plays > e2.plays; });

    // for(int i=0; i<info_table.size(); i++)
    //     cout << info_table[i].genre_ << " " << info_table[i].plays << " " << info_table[i].idx << endl;

    // pick two or one idx by genre
    string current_genre = info_table[0].genre_;
    int count = 0;
    for(int i=0; i<info_table.size(); i++) {
        if (++count <= 2 && current_genre == info_table[i].genre_) {
            answer.push_back(info_table[i].idx);
            continue;
        }

        // already exceed the two indices of the genre
        if (count > 2 && current_genre == info_table[i].genre_) continue;

        // new genre to be pushed
        count = 1;
        current_genre = info_table[i].genre_;
        answer.push_back(info_table[i].idx);

    }

    return answer;
}
