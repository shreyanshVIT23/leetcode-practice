# Title: 82. Remove Duplicates from Sorted List II
# URL: https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/
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
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        current = head

        while current:
            while current.next and current.val == current.next.val:
                current = current.next

            if prev.next == current:
                prev = prev.next
            else:
                prev.next = current.next

            current = current.next

        return dummy.next


class TestSolution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        prev = None
        current = head
        while current.next:

            val = current.val
            while current.next and current.next.val == val:
                current = current.next
            if prev:
                prev.next = current.next
            else:
                prev = current.next
            current = current.next

        return head
        # while prev.next:
        #     if prev.val == prev.next.val:
        #         if prev.next.next:
        #             prev.next = prev.next.next
        #         else:
        #             prev.next = None
        #             break
        #     prev = prev.next
        # while prev.next:
        #     val = prev.val
        #     while prev.next and prev.next.val == val:
        #         prev.next = prev.next.next
        #     prev = prev.next

        # return head


sol = Solution()
printLinkedList(sol.deleteDuplicates(arrayToLinkedList([1, 2, 3, 3, 4, 4, 5])))
printLinkedList(sol.deleteDuplicates(arrayToLinkedList([1, 1, 1, 2, 3])))
