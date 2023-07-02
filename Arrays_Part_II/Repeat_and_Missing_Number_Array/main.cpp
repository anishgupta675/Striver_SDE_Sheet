#include<bits/stdc++.h>

using namespace std;

vector<int> repeatedNumber(const vector<int> &A) {
    int S = 0, S2 = 0;
    for(int i : A) {
        S+= i;
        S2+= i * i;
    }
    return {(int)(((S - ((A.size() * (A.size() + 1)) / 2)) + (S2 - ((A.size() * (A.size() + 1) * (2 * A.size() + 1)) / 6))) / 2), (int)((((S - ((A.size() * (A.size() + 1)) / 2)) + (S2 - ((A.size() * (A.size() + 1) * (2 * A.size() + 1)) / 6))) / 2) - (S - ((A.size() * (A.size() + 1)) / 2)))};
}

int main() {}