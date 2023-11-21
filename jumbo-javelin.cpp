#include <iostream>

using namespace std;

int main()
{
  int n;
  int a = 0;
  int sum = 0;
  
  cin >> n;

  for(int i = 0; i < n; i++)
  {
    cin >> a;
    sum += a;
    
  }

  cout << sum - (n - 1) << endl;
}
