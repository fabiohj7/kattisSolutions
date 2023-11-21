#include <iostream>
using namespace std;

int main()
{
  char phone[7];

  cin.getline(phone, 7);

  for(int i = 0; i < 3; i++)
  {
    if(phone[i] == '5')
    {
      continue;
    } else {
      cout << 0 << endl;
      return 0;
    }
  }
  cout << 1 << endl;


}
