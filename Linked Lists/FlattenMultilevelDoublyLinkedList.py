/*
    LeetCode #430 - Flatten a Multilevel Doubly Linked List
    https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/
    
    Time Complexity - O(N) - No of nodes
    Space Complexity - O(N) - WorstCase as we are using stack to store the data
*/
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        dummy = Node(0)
        dummy.next = head
        
        stack = []
        while head is not None:
            if head.child:
                if head.next:
                    stack.append(head.next)
                head.next = head.child
                head.next.prev = head
                head.child = None
            elif head.next is None and stack:
                # if the list has reached the end & stack is not empty, pop the stack & continue the operation
                head.next = stack.pop()
                head.next.prev = head

            head = head.next

        return dummy.next
