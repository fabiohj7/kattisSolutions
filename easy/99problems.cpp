#include <iostream>
#include <cmath>

using namespace std;

int main()
{
  int n;
  cin >> n;
  
  if(n < 100) {
    n = 99;
    cout << n;
  }
  else if(n % 100 >= 50 || ((n + 1) * 2) % 100 == 0)
  {
    float nf = static_cast<float>(n);
    nf = (ceil(nf / 100) * 100) - 1;
    cout << nf;
  } else {
    n = (floor(n / 100) * 100) - 1;
    cout << n;
  }
}
