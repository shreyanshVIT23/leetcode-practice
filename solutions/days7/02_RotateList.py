# Title: 61. Rotate List
# URL: https://leetcode.com/problems/rotate-list/description/

# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        if head.next is None:
            return head

        if head.next.next is None:
            if k % 2 == 0:
                return head
            else:
                head.next.next = head
                curr = head.next
                head.next = None
                return curr

        length = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1

        k = k % length

        for i in range(k):
            curr = head
            while curr.next.next:
                curr = curr.next
            curr.next.next = head
            head = curr.next
            curr.next = None
        return head


class Solution2:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        tail.next = head

        k %= length

        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None

        return new_head


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
print(printLinkedList(sol.rotateRight(
    arrayToLinkedList([1, 2, 3, 4, 5]), 2)))  # [4,5,1,2,3]
print(printLinkedList(sol.rotateRight(
    arrayToLinkedList([0, 1, 2]), 4)))  # [2,0,1]
print(printLinkedList(sol.rotateRight(arrayToLinkedList([1]), 10)))  # [1]
print(printLinkedList(sol.rotateRight(arrayToLinkedList([1, 2]), 1)))  # [2,1]
