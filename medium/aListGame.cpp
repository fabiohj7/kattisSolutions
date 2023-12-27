#include <iostream>

using namespace std;

int getDivision(int num) {
  int remainder = 0;
  int counter = 0;
  int arr[] = {2, 3, 5};

  for (int n : arr) {
    while (remainder == 0) {
      remainder = num % n;
      counter++;
    }
  }
  // if (counter == 1) {
  //   counter = 3;
  // }
  return counter;
}

int main() {
  int num;
  int result = 0;
  cout << "Enter your number:" << endl;
  cin >> num;

  bool max = false;

  result = getDivision(num);

  cout << result << endl;
}
