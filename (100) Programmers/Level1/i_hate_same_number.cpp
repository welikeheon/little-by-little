#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> arr)
{
    vector<int> answer;

    for(int i=0; i<arr.size(); i++) {
        // keep looking for no overlap point
        if(i+1 < arr.size() && arr[i] == arr[i+1]) continue;
        else answer.push_back(arr[i]);
    }

    return answer;
}
