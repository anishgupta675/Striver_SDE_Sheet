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
    ListNode *cleanBuild(ListNode *clean, ListNode *build) {
        free(clean);
        return build;
    }
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        if(!head) return nullptr;
        int count = 0;
        ListNode *prev, *curr = head;
        while(curr) {
            curr = curr->next;
            count++;
        }
        if(count < n) return nullptr;
        if(count == n) return cleanBuild(head, head->next);
        count-= n - 1;
        curr = head;
        for(int i = 0; i < count; i++) {
            prev = curr;
            curr = curr->next;
        }
        prev->next = cleanBuild(curr, curr->next);
        return head;
    }
};

int main() {}