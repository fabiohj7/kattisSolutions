#include <iostream>

using namespace std;

int main() {
  int k, n;
  int x, sum = 0;

  cin >> k;
  cin >> n;

  for (int i = 0; i < n; i++) {
    cin >> x;
    sum += x;
  }

  k = k * (n + 1);

  int ans = k - sum;

  cout << ans << endl;
}
