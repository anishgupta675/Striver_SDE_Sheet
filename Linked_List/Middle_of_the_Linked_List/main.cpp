#include<bits/stdc++.h>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
    int half_length = INT_MAX;
    ListNode *res = nullptr;
    int getHalf(int full_length) {
        if(full_length % 2) return (full_length + 1) >> 1;
        return full_length >> 1;
    }
    void middleNode(ListNode *head, int full_length) {
        if(!head) {
            half_length = getHalf(full_length);
            return;
        }
        middleNode(head->next, full_length + 1);
        if(full_length == half_length) res = head;
    }
public:
    ListNode* middleNode(ListNode* head) {
        if(!head) return nullptr;
        if(!head->next) return head;
        middleNode(head, 1);
        return (res) ? res : head;
    }
};

int main() {}