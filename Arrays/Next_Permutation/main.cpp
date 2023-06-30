#include<bits/stdc++.h>

using namespace std;

class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int i, index1, index2;
        for(i = nums.size() - 2; i >= 0; i--) {
            if(nums[i] < nums[i + 1]) {
                index1 = i;
                break;
            }
        }
        if(i < 0) {
            reverse(nums.begin(), nums.end());
            return;
        }
        for(i = nums.size() - 1; i >= 0; i--) {
            if(nums[i] > nums[index1]) {
                index2 = i;
                break;
            }
        }
        swap(nums[index1], nums[index2]);
        reverse(nums.begin() + index1 + 1, nums.end());
    }
};

int main() {}