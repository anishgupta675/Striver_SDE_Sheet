#include<bits/stdc++.h>

using namespace std;

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int prev = -1, count = 0, longest = 0;
        unordered_set<int> uset;
        for(int i = 0; i < nums.size(); i++) uset.insert(nums[i]);
        for(int i = 0; i < nums.size(); i++) {
            count = 0;
            if(uset.find(nums[i] - 1) == uset.end()) {
                prev = nums[i];
                count = 1;
                while(uset.find(prev + 1) != uset.end()) {
                    prev++;
                    count++;
                }
            }
            longest = max(count, longest);
        }
        return longest;
    }
};

int main() {}