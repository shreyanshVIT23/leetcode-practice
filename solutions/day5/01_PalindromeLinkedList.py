# Title: 234. Palindrome Linked List
# URL: https://leetcode.com/problems/palindrome-linked-list/

from typing import List, Optional

class ListNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        linked_array = []
        while head:
            linked_array.append(head.val)
            head = head.next
        return linked_array[::-1] == linked_array

def arrayToLinkedList(array: List[int]):
    head = ListNode(array[0])
    current = head
    for i in range(1, len(array)):
        current.next = ListNode(array[i])
        current = current.next
    return head

sol = Solution()
print(sol.isPalindrome(arrayToLinkedList([1, 2, 3, 2, 1]))) # True
