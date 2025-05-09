# Title: 2095. Delete Middle Node in a Linked List
# URL: https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/description/


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
    return result


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None

        length = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1

        middlePos = length//2

        prev = None
        curr = head
        n = 0
        while curr:
            if n == middlePos:
                prev.next = curr.next
                return head
            prev = curr
            curr = curr.next
            n += 1


class Solution1:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None

        prev = None
        slow = fast = head

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # Now slow points to the middle node to be deleted
        if prev:
            prev.next = slow.next
        else:
            head = head.next  # Update head if the first node is deleted

        return head


sol = Solution()
head = arrayToLinkedList([1, 3, 4, 7, 1, 2, 6])
head2 = arrayToLinkedList([1, 2, 3, 4])
head3 = arrayToLinkedList([2, 1])
print(printLinkedList(sol.deleteMiddle(head)))  # [1, 3, 4, 1, 2, 6]
print(printLinkedList(sol.deleteMiddle(head2)))  # [1, 2, 4]
print(printLinkedList(sol.deleteMiddle(head3)))  # [1]
