#include <cmath>
#include <iostream>

using namespace std;

int main() {
  string word;

  cin >> word;
  int cc = 0, tc = 0, gc = 0;

  for (int i = 0; i < word.size(); i++) {
    switch (word[i]) {
    case 'C':
      cc++;
      break;
    case 'T':
      tc++;
      break;
    case 'G':
      gc++;
      break;
    default:
      cout << "Not a card" << endl;
    }
  }

  int sum = pow(cc, 2) + pow(tc, 2) + pow(gc, 2);

  if (cc >= 1 && tc >= 1 && gc >= 1) {

    int minValue = cc;

    if (tc < minValue) {
      minValue = tc;
    }

    if (gc < minValue) {
      minValue = gc;
    }
    minValue *= 7;
    sum += minValue;
  }
  cout << sum << endl;
}
