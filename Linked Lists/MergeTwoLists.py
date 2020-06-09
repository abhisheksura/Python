/*
    LeetCode #21 - Merge Two Sorted Lists
    https://leetcode.com/problems/merge-two-sorted-lists/
    
    Time Complexity - O(M+N)
    Space Complexity - O(M+N)
*/

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        current = dummy

        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next

            current = current.next

        if l1 is None:
            current.next = l2
        elif l2 is None:
            current.next = l1

        return dummy.next
