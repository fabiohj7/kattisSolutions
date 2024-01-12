#include <cctype>
#include <iostream>
#include <unordered_map>

using namespace std;

bool isNumber(string word) {
  for (int j = 0; j < word.size(); j++) {
    if (isdigit(word[j])) {
      return true;
    }
  }
  return false;
}

int main() {
  int n;

  unordered_map<string, int> cups;
  cin >> n;
  string lines[n];

  for (int i = 0; i < n * 2; i++) {
    cin >> lines[i];
    if (isNumber(lines[i]) && i % 2 == 0) {
      cups[lines[i + 1]] = stoi(lines[i]);
    } else if (isNumber(lines[i]) && i % 2 == 1) {
      cups[lines[i - 1]] = stoi(lines[i]);
    }
  }
  for (const auto &pair : cups) {
    std::cout << pair.first << ": " << pair.second << std::endl;
  }
}
