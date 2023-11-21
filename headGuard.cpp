#include <iostream>
#include <cstring>
using namespace std;

int main()
{
  char letters[15][500];
  char temp = '\0';
  int counter = 1;
  int sentCount = 0;

  for(int i = 0; i < 15; i++)
  {
    cin.getline(letters[i], 500);
    if(strlen(letters[i]) == 0)
    {
      break;
    }
    ++sentCount;
  }

  for(int i = 0; i < sentCount; i++)
  {
    temp = letters[i][0];
    for(int j = 1; j < strlen(letters[i]) + 1; j++)
    {
      if(letters[i][j] == temp)
      {
        counter++;
        temp = letters[i][j];
      } else {
        cout << counter << temp;
        counter = 1;
        temp = letters[i][j];
      }
    } 
    cout << endl;
  }
}
