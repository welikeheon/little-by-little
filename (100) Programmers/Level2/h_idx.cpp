#include <string>
#include <vector>
#include <utility>
#include <algorithm>

using namespace std;

int solution(vector<int> citations) {
    int runner = 0; // idx runner for citations vector

    // order by descending
    sort(citations.begin(), citations.end(), [](const auto& x,
                                                const auto& y){ return x>y ;} );

    // find the idx which is bigger than the citation number
    while(runner < citations.size() && runner < citations[runner]) {
        runner++;
    }

    return runner;
}
