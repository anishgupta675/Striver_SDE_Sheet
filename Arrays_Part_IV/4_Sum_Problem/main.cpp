#include<bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        vector<vector<int>> ans;
        sort(nums.begin(), nums.end());
        for(int i = 0; i < nums.size(); i++) {
            for(int j = i + 1; j < nums.size(); j++) {
                int target2 = target - nums[i] - nums[j], low = j + 1, high = nums.size() - 1;
                while(low < high) {
                    int two_sum = nums[low] + nums[high];
                    if(two_sum < target2) low++;
                    else if(two_sum > target2) high--;
                    else {
                        vector<int> quad;
                        quad.push_back(nums[i]);
                        quad.push_back(nums[j]);
                        quad.push_back(nums[low]);
                        quad.push_back(nums[high]);
                        ans.push_back(quad);
                        while(low < high && nums[low] == quad[2]) low++;
                        while(low < high && nums[high] == quad[3]) high++;
                    }
                }
                while(j + 1 < nums.size() && nums[j] == nums[j + 1]) j++;
            }
            while(i + 1 < nums.size() && nums[i] == nums[i + 1]) i++;
        }
        return ans;
    }
};

int main() {}