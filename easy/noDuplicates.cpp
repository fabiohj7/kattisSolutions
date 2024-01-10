#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

int main() {

  vector<string> sentence;
  string temp;

  getline(cin, temp);

  istringstream iss(temp);

  string words;
  while (iss >> words) {
    sentence.push_back(words);
  }

  bool duplicate = false;

  for (int i = 0; i < sentence.size(); i++) {
    for (int j = 0; j < sentence.size(); j++) {
      if (i != j && sentence[i] == sentence[j]) {
        duplicate = true;
      }
    }
  }
  if (duplicate) {
    cout << "no" << endl;
  } else {
    cout << "yes" << endl;
  }
}
