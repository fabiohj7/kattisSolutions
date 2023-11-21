#include <iostream>
using namespace std;

int main()
{
  char name[40];

  cin.getline(name, 40);

  int a, b, c;
  cin >> a;
  cin >> b;
  cin >> c;

  if(a > b)
  {
    cout << "VEIT EKKI" << endl;
  } else if(c == abs(a - b)) {
    cout << "SITH";
  } else {
    cout << "JEDI";
  }


}
