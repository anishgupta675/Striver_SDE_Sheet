#include<bits/stdc++.h>

using namespace std;

class Solution {
    bool check(vector<int> &nums, int element) {
        int count = 0;
        for(int i = 0; i < nums.size(); i++) if(nums[i] == element) count++;
        return (count > nums.size() / 3) ? 1 : 0;
    }
public:
    vector<int> majorityElement(vector<int>& nums) {
        int count1 = 0, count2 = 0, element1 = 0, element2 = 0;
        for(int i = 0; i < nums.size(); i++) {
            if(!count1 && nums[i] != element2) {
                count1 = 1;
                element1 = nums[i];
            } else if(!count2 && nums[i] != element1) {
                count2 = 1;
                element2 = nums[i];
            } else if(nums[i] == element1) count1++;
            else if(nums[i] == element2) count2++;
            else {
                count1--;
                count2--;
            }
        }
        int count = nums.size() / 3;
        vector<int> res;
        if(check(nums, element1)) res.push_back(element1);
        if(check(nums, element2)) res.push_back(element2);
        sort(res.begin(), res.end());
        return res;
    }
};

int main() {}