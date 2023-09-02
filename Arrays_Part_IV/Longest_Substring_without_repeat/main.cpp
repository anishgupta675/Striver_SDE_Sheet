#include<bits/stdc++.h>

using namespace std;

class Solution {
    const int NO_OF_CHARS = 256;
public:
    int lengthOfLongestSubstring(string s) {
        int i = 0, res = 0;
        vector<int> last_index(NO_OF_CHARS, -1);
        for(int j = 0; j < s.length(); j++) {
            i = max(i, last_index[s[j]] + 1);
            res = max(res, j - i + 1);
            last_index[s[j]] = j;
        }
        return res;
    }
};

int main() {}