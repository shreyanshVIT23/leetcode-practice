# Title: 21. Merge Two Sorted Lists
# URL: https://leetcode.com/problems/merge-two-sorted-lists/


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_head = None

        if list1 is None:
            return list2

        if list2 is None:
            return list1

        if list1.val < list2.val:
            new_head = list1
            list1 = list1.next
        else:
            new_head = list2
            list2 = list2.next

        curr = new_head

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        if list1:
            curr.next = list1
        else:
            curr.next = list2

        return new_head
