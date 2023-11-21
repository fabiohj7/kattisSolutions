#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

int main()
{

  long n1, n2; 
  //The while loop basically waits for a EOF
  while(cin >> n1 >> n2)
  {
    long ans = n1 - n2;
    cout << abs(ans) << endl;
  }
  return 0;
}
