#include <iostream>
using namespace std;

int main()
{
  int n = 0;
  cin >> n;

  int arr[n];

  for(int i = 0; i < n; i++)
  {
    cin >> arr[i];
    if(arr[i] % 2 == 0)
    {
      cout << arr[i] << " is even" << endl;
    } else {
      cout << arr[i] << " is odd" << endl;
    }
  }
}
