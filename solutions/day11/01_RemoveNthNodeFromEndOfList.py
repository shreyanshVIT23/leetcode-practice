# Title: 19. Remove Nth Node From End of List
# URL: https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy

        for _ in range(n + 1):
            fast = fast.next
        
        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy.next

sol = Solution()
printLinkedList(sol.removeNthFromEnd(arrayToLinkedList([1,2,3,4,5]), 2))
printLinkedList(sol.removeNthFromEnd(arrayToLinkedList([1]), 1))
printLinkedList(sol.removeNthFromEnd(arrayToLinkedList([1,2]), 1))