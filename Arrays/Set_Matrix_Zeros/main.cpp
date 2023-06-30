#include<bits/stdc++.h>

using namespace std;

class Solution {
    void fillRow(vector<vector<int>> &matrix, int row) {
        for(int i = 0; i < matrix[row].size(); i++) {
            if(!matrix[row][i]) continue;
            matrix[row][i] = 0;
        }
    }
    void fillColumn(vector<vector<int>> &matrix, int column) {
        for(int i = 0; i < matrix.size(); i++) {
            if(!matrix[i][column]) continue;
            matrix[i][column] = 0;
        }
    }
public:
    void setZeroes(vector<vector<int>>& matrix) {
        unordered_set<int> row;
        unordered_set<int> column;
        for(int i = 0; i < matrix.size(); i++) {
            for(int j = 0; j < matrix[i].size(); j++) {
                if(!matrix[i][j]) {
                    row.insert(i);
                    column.insert(j);
                }
            }
        }
        for(unordered_set<int>::iterator i = row.begin(); i != row.end(); i++) fillRow(matrix, *i);
        for(unordered_set<int>::iterator i = column.begin(); i != column.end(); i++) fillColumn(matrix, *i);
    }
};

int main() {}