/*
    LeetCode #206 - Reverse Linked List
    https://leetcode.com/problems/reverse-linked-list/
*/

class LinkedList:    
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        current = head
        next = None
        while current:
            # storing the next pointer in a variable
            next = current.next
            # Reverse Operation
            current.next = prev
            # Move the pointer to next element
            prev = current
            current = next
        return prev
