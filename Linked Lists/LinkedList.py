class LinkedList:
    # LeetCode #206 - Reverse Linked List
    # https://leetcode.com/problems/reverse-linked-list/
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

    # LeetCode #876 - Middle of the Linked List
    # https://leetcode.com/problems/middle-of-the-linked-list/
    # TC - O(N) No of nodes
    def middleNode(self, head: ListNode) -> ListNode:
        if head is None:
            return None

        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
