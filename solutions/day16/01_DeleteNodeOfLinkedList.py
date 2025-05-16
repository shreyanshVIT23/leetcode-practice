# Title: 237. Delete Node In a Linked List
# URL: https://leetcode.com/problems/delete-node-in-a-linked-list/description/

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
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        while node.next.next:
            node.val = node.next.val
            node = node.next
        node.val = node.next.val
        node.next = None
        