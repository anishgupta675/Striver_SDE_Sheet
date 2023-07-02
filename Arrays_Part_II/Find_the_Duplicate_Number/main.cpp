#include<bits/stdc++.h>

using namespace std;

class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int cur = 0, cur2 = 0, fast = 0;
        while(1) {
            cur = nums[cur];
            fast = nums[nums[fast]];
            if(cur == fast) break;
        }
        while(1) {
            cur = nums[cur];
            cur2 = nums[cur2];
            if(cur == cur2) return cur;
        }
        return 0;
    }
};

int main() {}