#include <iostream>

using namespace std;

int main() {
  int n;

  cin >> n;
  string words[n];

  for (int i = 0; i < n; i++) {
    cin >> words[i];
  }

  bool ascending = false;
  bool descending = false;

  for (int i = 0; i < n - 1; i++) {
    if (words[i] < words[i + 1]) {
      ascending = true;
    } else if (words[i] > words[i + 1]) {
      descending = true;
    } else if (words[i] == words[i + 1]) {
      continue;
    } else {
      // Handle the case when words[i] is equal to words[i + 1]
      cout << "NEITHER" << endl;
      return 0;
    }
  }

  if (ascending && !descending) {
    cout << "INCREASING" << endl;
  } else if (descending && !ascending) {
    cout << "DECREASING" << endl;
  } else {
    // Handle the case when the sequence is neither strictly ascending nor
    // strictly descending
    cout << "NEITHER" << endl;
  }

  return 0;
}
