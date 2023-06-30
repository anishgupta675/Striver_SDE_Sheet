#include<bits/stdc++.h>

using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int max_val = 0, min_val = prices[0];
        for(int i = 0; i < prices.size(); i++) {
            min_val = min(min_val, prices[i]);
            max_val = max(max_val, prices[i] - min_val);
        }
        return max_val;
    }
};

int main() {}