#include<bits/stdc++.h>

using namespace std;

class Solution {
public:
    int checkRow(vector<int> &row, int target) {
        if(row[0] <= target && row[row.size() - 1] >= target) return 0;
        if(row[0] > target) return 1;
        return -1;
    }
    bool searchColumn(vector<int> &row, int low, int high, int target) {
        if(low > high) return false;
        int mid = (low + high) >> 1;
        if(row[mid] == target) return true;
        if(row[mid] > target) return searchColumn(row, low, mid - 1, target);
        return searchColumn(row, mid + 1, high, target);
    }
    bool searchRow(vector<vector<int>> &matrix, int low, int high, int target) {
        if(low > high) return false;
        int mid = (low + high) >> 1;
        if(!checkRow(matrix[mid], target)) return searchColumn(matrix[mid], 0, matrix[mid].size() - 1, target);
        if(checkRow(matrix[mid], target) == 1) return searchRow(matrix, low, mid - 1, target);
        return searchRow(matrix, mid + 1, high, target);
    }
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        return searchRow(matrix, 0, matrix.size() - 1, target);
    }
};

int main() {}