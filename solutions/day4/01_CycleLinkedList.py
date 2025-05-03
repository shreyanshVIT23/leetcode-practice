# Title: 141. Linked List Cycle
# URL: https://leetcode.com/problems/linked-list-cycle/



from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        array = []
        while head:
            array.append(head)
            head = head.next
            if head in array:
                return True
        return False
