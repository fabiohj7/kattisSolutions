#include <iostream>
using namespace std;

int main()
{
  int k, n = 0;
  int counter = 1;

  bool rep = false;
  cin >> k;

  for(int x = 0; x < k; x++)
  {
    cin >> n;
    string countries[n];
    cin >> countries[0];
    counter = 1;
    for(int i = 1; i < n; i++)
    {
      rep = false;
      cin >> countries[i];
      for(int j = 0; j < i; j++)
      {
        if(countries[i] == countries[j])
        {
          rep = false;
          break;
        } else {
          rep = true;
        }
      }
      if(rep == true)
      {
        counter++;
      }
    }
    cout << counter << endl;
  }
}
