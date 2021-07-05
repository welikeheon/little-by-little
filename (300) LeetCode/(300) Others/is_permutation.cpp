#include <iostream>

using namespace std;

bool isPermutation(string s1, string s2) {
  if(s1.size() != s2.size()) return false;

  char s1_arr_cnt[27];
  for(int i=0; i<s1.size(); i++) {  // str to arr
    s1_arr_cnt[ s1[i]-'a' ]++;
  }

  for(int i=0; i<s2.size(); i++) {
    if(--s1_arr_cnt[ s2[i]-'a' ] < 0) return false;
  }

  return true;
}

int main() {
  string s1, s2;

  cin >> s1;
  cin >> s2;

  cout << isPermutation(s1, s2) << endl;

  return 0;
}
