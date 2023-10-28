#include<bits/stdc++.h>

using namespace std;

class Solution {
    vector<vector<int>> res;
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        if(nums.size() < 3) return res;
        unordered_map<int, int> umap;
        for(int i = 0; i < nums.size(); i++) {
            for(int j = i + 1; j < nums.size(); j++) {
                if(umap.find((nums[i] + nums[j]) * -1) != umap.end() && umap[(nums[i] + nums[j]) * -1] > j) {
                    vector<int> data(3);
                    data[0] = nums[i];
                    data[1] = nums[j];
                    data[2] = (nums[i] + nums[j]) * -1;
                    res.push_back(data);
                }
            }
        }
        return res;
    }
};

int main() {}