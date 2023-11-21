#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int main()
{
  string n;

  cin >> n;

  reverse(n.begin(), n.end());

  cout << n << endl;
  
}
