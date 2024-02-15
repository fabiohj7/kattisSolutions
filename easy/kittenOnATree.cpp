#include <iostream>
#include <sstream>

using namespace std;

int main() {
  int cat;
  cin >> cat;
  int arr[100] = {0};
  string line;
  bool found = false;

  while (getline(cin, line)) {
    int index;
    int number;
    istringstream iss(line);

    iss >> number;
    while (iss >> index) {
      arr[index] = number;
    }
  }

  cout << cat << " ";
  while (!found) {
    cout << arr[cat] << " ";
    cat = arr[cat];
    if (arr[cat] == 0) {
      found = true;
    }
  }
}
