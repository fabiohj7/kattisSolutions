#include <cctype>
#include <iostream>
#include <unordered_map>
#include <vector>
#include <algorithm>

using namespace std;

bool isNumber(const string& word) {
    for (size_t j = 0; j < word.size(); j++) {
        if (isdigit(word[j])) {
            return true;
        }
    }
    return false;
}

int main() {
    int n;
    cin >> n;

    vector<string> lines(n * 2);

    for (int i = 0; i < n * 2; i++) {
        cin >> lines[i];
    }

    unordered_map<string, float> cups;

    for (int i = 0; i < n * 2; i++) {
        if (isNumber(lines[i]) && i % 2 == 0) {
            cups[lines[i + 1]] = stof(lines[i]) / 2;
        } else if (isNumber(lines[i]) && i % 2 == 1) {
            cups[lines[i - 1]] = stof(lines[i]);
        }
    }

    vector<pair<float, string>> sortedVec;

    for (const auto& pair : cups) {
        sortedVec.push_back(make_pair(pair.second, pair.first));
    }

    sort(sortedVec.begin(), sortedVec.end());

    for (vector<pair<float, string>>::iterator it = sortedVec.begin();
         it != sortedVec.end(); ++it) {
        std::cout << it->second << std::endl;
    }

    return 0;
}
