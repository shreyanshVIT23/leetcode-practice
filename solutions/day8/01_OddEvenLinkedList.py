# Title: 328. Odd Even Linked List
# URL: https://leetcode.com/problems/odd-even-linked-list/description/

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        odd = head
        even = head.next
        even_head = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = even_head
        return head


class Solution1:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        odds = []
        evens = []
        curr = head
        i = 1
        while curr:
            if i % 2 == 1:
                odds.append(curr)
            else:
                evens.append(curr)
            curr = curr.next
            i += 1

        for i in range(len(odds) - 1):
            odds[i].next = odds[i + 1]

        for i in range(len(evens) - 1):
            evens[i].next = evens[i + 1]

        if odds:
            odds[-1].next = evens[0] if evens else None
        if evens:
            evens[-1].next = None

        return odds[0]


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
print(printLinkedList(sol.oddEvenList(arrayToLinkedList([1, 2, 3, 4, 5]))))
print(printLinkedList(sol.oddEvenList(arrayToLinkedList(
    [2, 1, 3, 5, 6, 4, 7]))))  # [2, 3, 6, 1, 5, 4, 7]
