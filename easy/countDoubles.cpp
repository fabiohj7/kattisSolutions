#include <iostream>
using namespace std;

int main()
{
  int n, m;
  cin >> n;
  cin >> m;

  int nums[n];

  for(int i = 0; i < n; i++)
  {
    cin >> nums[i];
  }


}

void heap(int arr[], int n, int m)
{
  for(int i = 0; i < m; i++)
  {
    heap(arr, n, i);
  }
}
