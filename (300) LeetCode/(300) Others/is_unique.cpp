#include <iostream>
#include <string>

using namespace std;

bool isUniqueChars(string str) {
  int checker = 0;
  int char_ascii;

  for(int i=0; i<str.size(); i++) {
    char_ascii = str[i] - 'a';
    if(checker & (1 << char_ascii)) return false;
    checker |= 1 << char_ascii;
  }
  return true;
}

int main() {
  string inpt;
  cin >> inpt;
  cout << isUniqueChars(inpt) << endl;


  return 0;
}
