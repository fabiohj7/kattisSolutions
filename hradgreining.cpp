#include <iostream>
#include <string.h>
#include <algorithm>

using namespace std;

int main()
{
  string s;

  cin >> s;

  string s2 = "COV";

  transform(s.begin(), s.end(), s.begin(), ::toupper);

  if(s.find(s2) != string::npos)
  {
    cout << "Veikur!" << endl;
  } else {
    cout << "Ekki veikur!" << endl;
  }


}
