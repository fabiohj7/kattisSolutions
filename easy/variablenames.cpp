#include <iostream>
#include <vector>
using namespace std;

int main() {
  int n;
  cin >> n;

  vector<int> nums;

  for (int i = 0; i < n; i++) {
    int c;
    cin >> c;

    int x = 1;
    int b = 0;
    while (1) {
      bool found = false;
      b = x * c;
      for (int j = 0; j < nums.size(); j++) {
        if (b == nums[j]) {
          found = true;
          break;
        } else {
          found = false;
        }
      }
      if (found == false) {
        nums.push_back(b);
        cout << b << endl;
        break;
      } else {
        x++;
      }
    }
  }
}
