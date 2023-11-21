#include <iostream>

using namespace std;

int main()
{

  int n;
  cin >> n;
  string words[n];

  for(int i = 0; i < n; i++)
  {
    cin >> words[i];

    if((i + 1) % 2 == 1)
    {
      cout << words[i] << endl;
    }
  }
}
