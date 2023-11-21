#include <iostream>
using namespace std;

int main()
{
  int a,b,c;

  cin >> a;
  cin >> b;
  cin >> c;

  if(a < b && a < c)
  {
    cout << "Monnei" << endl;
  } else if (b < a && b < c) {
    cout << "Fjee" << endl;
  } else {
    cout << "Dolladollabilljoll" << endl;
  }
}
