class Solution {
public:
    string mostCommonWord(string paragraph, vector<string>& banned) {
        // reminder! the size of the vector is lower than or equal to 1000

        // to return
        string to_return;

        // hash_map for the paragraph
        unordered_map<string, int> paragraph_hash;

        // tmp. string for the alphabet, this contains only a word with [a-z]
        string tmp;

        // complete and input the hash_map
        for (auto& smt : paragraph) {    // smt stands for something
            if ((smt >= 65 && smt <= 90) ||
                (smt >= 97 && smt <= 122)){    // if something is a alphabet,
                tmp.push_back(tolower(smt));
                continue;       // block from here
            }

            if(tmp.size() > 0) {        // if something is not a alphabet,
                paragraph_hash[tmp]++;
                tmp = "";
            }
        }

        if (tmp.size() > 0) {  // in case we only have one word in paragraph
            paragraph_hash[tmp]++;
            tmp = "";
        }

        // test
        // for (auto p : paragraph_hash) {
        //     cout << p.first << " " << p.second << endl;
        // }
        // cout << endl;

        // create the banned hash map
        unordered_map<string, int> banned_map;
        for (string& s : banned) banned_map[s]++;

        // for (auto p : banned_map) {
        //     cout << p.first << " " << p.second << endl;
        // }

        // // find out what to return except the banned string
        for (const auto& p : paragraph_hash) {
            if ((to_return.size() == 0 || p.second > paragraph_hash[to_return])
                && banned_map.find(p.first) == banned_map.end()) {
                to_return = p.first;
            }

        }
        return to_return;
    }
};
