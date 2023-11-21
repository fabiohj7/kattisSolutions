#include <iostream>

using namespace std;

int main()
{
  int scores[5][4];
  int sum[5] = {0};
  int flag = 0;
  int index = 0;
  
  for(int i = 0; i < 5; i++)
  {
    for(int j = 0; j < 4; j++)
    {
      cin >> scores[i][j];
      sum[i] += scores[i][j];
    }
  }

  for(int i = 0; i < 5; i++)
  {
    if(flag < sum[i])
    {
      flag = sum[i];
      index = i;
    }
  }

  cout << index + 1 << " " << flag << endl;

}
