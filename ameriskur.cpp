#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
  int n;

  cin >> n;

  double ans = n * 0.09144;

  cout << fixed << setprecision(5) << ans;
}
