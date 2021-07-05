#include <string>
#include <iostream>

using namespace std;

void reverseStr(string& str) {
  int right = str.size() - 1;
  int left = 0;
  while(left < right) {
    swap(str[left++], str[right--]);
  }

}

int main() {
  string str;
  cin >> str;

  reverseStr(str);
  cout << str << endl;

  return 0;
}
