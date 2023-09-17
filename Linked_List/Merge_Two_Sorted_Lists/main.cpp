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
    int getMax(ListNode *list1, ListNode *list2) {
        if(list1->val < list2->val) return getMax(list2, list1);
        int temp = list1->val;
        list1 = list1->next;
        return temp;
    }
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode *head = new ListNode(getMax(list1, list2)), *curr = head;
        while(list1 && list2) {
            curr->next = new ListNode(getMax(list1, list2));
            curr = curr->next;
        }
        while(list1) {
            curr->next = new ListNode(list1->val);
            list1 = list1->next;
            curr = curr->next;
        }
        while(list2) {
            curr->next = new ListNode(list2->val);
            list2 = list2->next;
            curr = curr->next;
        }
        return head;
    }
};

int main() {}