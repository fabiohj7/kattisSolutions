#include <algorithm>
#include <iostream>
#include <unordered_map>

using namespace std;

int max(int arr[3]) {
  int flag;
  for (int i = 0; i < 3; i++) {
    flag = max(flag, arr[i]);
  }
  return flag;
}

int min(int arr[3]) {
  int flag = arr[0];
  for (int i = 1; i < 3; i++) {
    flag = min(flag, arr[i]);
  }
  return flag;
}

int lastNum(int arr[3]) {
  int flag;
  for (int i = 0; i < 3; i++) {
    if (arr[i] != min(arr) && arr[i] != max(arr)) {
      flag = arr[i];
    }
  }
  return flag;
}

int main() {
  string letters;
  int arr[3];
  for (int i = 0; i < 3; i++) {
    cin >> arr[i];
  }

  cin >> letters;
  unordered_map<char, int> map;

  int correct[3];
  for (int i = 0; i < 3; i++) {
    if (letters[i] == 'A') {
      correct[i] = min(arr);
    } else if (letters[i] == 'C') {
      correct[i] = max(arr);
    } else if (letters[i] == 'B') {
      correct[i] = lastNum(arr);
    }
  }
  for (int i = 0; i < 3; i++) {
    cout << correct[i] << " ";
  }
}
