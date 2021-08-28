#include <string>
#include <vector>
#include <cctype>

using namespace std;

int solution(int cacheSize, vector<string> cities) {
    int answer = 0;
    int cities_size = cities.size();
    bool cache_hit;
    vector<string> cache;

    if (cacheSize == 0) return cities_size * 5; // when we don't have a cache

    // to uppercase
    for (int i=0; i<cities_size; i++) {
        for (int j=0; j<cities[i].size(); j++) {
            cities[i][j] = toupper(cities[i][j]);
        }
    }

    for (int runner=0; runner<cities_size; runner++) {
        cache_hit = false;  // we assume there is a cache miss

        for (int i=0; i<cache.size(); i++) {
            if (cache[i].compare(cities[runner]) == 0) {   // cache hit
                cache.erase(cache.begin()+i); // remove it and push back to end
                answer++;
                cache_hit = true;
                break;
            }
        }

        cache.push_back(cities[runner]);  // push back wether it is hit or miss

        if (!cache_hit) { // cache miss
            if (cache.size() > cacheSize) // needs to pop the LRU
                cache.erase(cache.begin());
            answer += 5;
        }
    }

    return answer;
}
