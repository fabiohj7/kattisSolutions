#include <iostream>
#include <bits/stdc++.h>
using namespace std;


int main()
{
  char s[100];

  int counter =0;
  cin.getline(s, 100);

  char *p = strtok(s, "-");

  while(p != NULL)
  {
    cout << p[0];
    p = strtok(NULL, "-");
  }
}
