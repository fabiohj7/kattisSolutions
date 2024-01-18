#include <iostream>
#include <string>
#include <sstream>

using namespace std;

int main() {
  string phrase;
  string comparison = "eh?";
  bool canadian = false;

  getline(cin, phrase);

  istringstream iss(phrase);

  string flag;
  while(iss >> flag) {
    continue;
  }

  if (flag == comparison) {
    canadian = true;
  }

  if (canadian) {
    cout << "Canadian!" << endl;
  } else {
    cout << "Imposter!" << endl;
  }

  return 0;
}
