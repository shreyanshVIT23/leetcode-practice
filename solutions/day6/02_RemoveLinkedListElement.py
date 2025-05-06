# Title: 203. Remove Linked List Elements
# URL: https://leetcode.com/problems/remove-linked-list-elements/

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val == val:
            head = head.next

        current = head
        prev = None

        while current:
            if current.val == val:
                prev.next = current.next
            else:
                prev = current
            current = current.next

        return head


def arrayToLinkedList(array: List[int]):
    head = ListNode(array[0])
    current = head
    for i in range(1, len(array)):
        current.next = ListNode(array[i])
        current = current.next
    return head

def printLinkedList(head: Optional[ListNode]):
    current = head
    result = []
    while current:
        result.append(current.val)
        current = current.next
    return result

sol = Solution()
print(printLinkedList(sol.removeElements(arrayToLinkedList([1, 2, 6, 3, 4, 5, 6]), 6))) # [1,2,3,4,5]