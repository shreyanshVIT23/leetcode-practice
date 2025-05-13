# Title: 2807. Insert Greatest Common Divisor in Linked List
# URL: https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/description/

import math
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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
    print(result)


class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not (head or head.next):
            return head

        first = head
        second = head.next

        while second:
            newNode = ListNode(math.gcd(first.val, second.val), second)
            first.next = newNode
            first = second
            second = second.next

        return head

sol = Solution()
printLinkedList(sol.insertGreatestCommonDivisors(arrayToLinkedList([18,6,9,3,12])))