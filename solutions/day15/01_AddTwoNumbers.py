# Title: 2. Add Two Numbers
# URL: https://leetcode.com/problems/add-two-numbers/description/

from typing import List, Optional
from atexit import register
from subprocess import run


def f():
    run(["cat", "display_runtime.txt"])
    with open("display_runtime.txt", "w") as file:
        print('0', file=file)
    run("ls")


# register(f)


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
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        head = dummy
        carry = 0
        while l1 and l2:
            total = l1.val + l2.val + carry
            if total <= 9:
                dummy.next = ListNode(total)
                carry = 0
                dummy = dummy.next
            else:
                dummy.next = ListNode(total - 10)
                carry = 1
                dummy = dummy.next
            l1 = l1.next
            l2 = l2.next
        
        while l1 and carry:
            l1.val += carry
            if l1.val <= 9:
                dummy.next = l1
                carry = 0
                dummy = dummy.next
            else:
                dummy.next = ListNode(l1.val - 10)
                carry = 1
                dummy = dummy.next
            l1 = l1.next
        
        if l1:
            dummy.next = l1
            
        if carry and not l1 and not l2:
            dummy.next = ListNode(1)
            carry = 0
            dummy = dummy.next
            
        while l2 and carry:
            l2.val += carry
            if l2.val <= 9:
                dummy.next = l2
                carry = 0
                dummy = dummy.next
            else:
                dummy.next = ListNode(l2.val - 10)
                carry = 1
                dummy = dummy.next
            l2 = l2.next

        if l2:
            dummy.next = l2

        if carry and not l2 and not l1:
            dummy.next = ListNode(1)
            carry = 0
            dummy = dummy.next
        
        return head.next
                
sol = Solution()
l1 = arrayToLinkedList([2,4,9])
l2 = arrayToLinkedList([5,6,4,9])
printLinkedList(sol.addTwoNumbers(l1, l2))  # Output: [7, 0, 8]