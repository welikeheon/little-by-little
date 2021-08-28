#include <string>
#include <vector>
#include <utility>
#include <iostream>

using namespace std;

int getGCD(int a, int b) {  // GCD given two numbers
    if (a < b) swap(a, b);
    if (b == 0) return a;
    return getGCD(b, a % b);
}

int solution(vector<int> arr) {
    int arr_size = arr.size();
    int answer = arr[0];

    if (arr_size == 1)
        return answer;

    for(int i=1; i<arr_size; i++) {
        answer = (answer * arr[i]) / (getGCD(arr[i], answer));
    }
    return answer;
}
