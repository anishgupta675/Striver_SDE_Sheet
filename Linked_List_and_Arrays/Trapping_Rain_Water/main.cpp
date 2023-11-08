#include<bits/stdc++.h>

using namespace std;

class Solution {
public:
    int trap(vector<int>& height) {
        int ans = 0;
        vector<int> dp1(height.size()), dp2(height.size());
        dp1[0] = height[0];
        for(int i = 1; i < dp1.size(); i++) dp1[i] = max(dp1[i - 1], height[i]);
        dp2[height.size() - 1] = height[height.size() - 1];
        for(int i = dp2.size() - 2; i >= 0; i--) dp2[i] = max(dp2[i + 1], height[i]);
        for(int i = 0; i < height.size(); i++) ans+= min(dp1[i], dp2[i]) - height[i];
        return ans;
    }
};

int main() {}