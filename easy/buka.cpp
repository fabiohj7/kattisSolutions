#include <iostream>

using namespace std;

int main()
{
  long long a, b;
  char op;

  cin >> a;
  cin >> op;
  cin >> b;

  if(op == '*')
  {
    cout << a * b << endl;
  } else if (op == '+') {
    cout << a + b << endl;
  }
}
