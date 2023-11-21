#include <iomanip>
#include <iostream>
#include <cmath>

using namespace std;

int main()
{
  double a, b, c, d;

  cin >> a >> b >> c >> d;

  double sum = (a + b + c + d) / 2;

  double total = sqrt((sum - a) * (sum - b) * (sum - c) * (sum - d));

  cout << fixed << setprecision(6) << total;
}
