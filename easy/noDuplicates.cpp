#include <iostream>
#include <string>
using namespace std;

int main()
{

  char* words[80][80];
  char s[80];
  int i = 0;
  
  while(words[i] != NULL)
  {
    words[i][i] = strtok(s, 80);
  }
}
