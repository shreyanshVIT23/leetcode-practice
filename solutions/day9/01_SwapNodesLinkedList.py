# Title: 1721. Swapping Nodes in a Linked List
# URL: https://leetcode.com/problems/swapping-nodes-in-a-linked-list/description/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        length = 1
        curr = head
        while curr.next:
            curr = curr.next
            length += 1

        posX = k
        posY = length - k + 1

        if k == posY:
            return head

        prevX = prevY = None
        currX = currY = head

        if posX > posY:
            posX, posY = posY, posX

        i = 1
        prev = None
        curr = head
        while curr:
            if i == posX:
                prevX, currX = prev, curr
            if i == posY:
                prevY, currY = prev, curr
            prev = curr
            curr = curr.next
            i += 1

        if prevX:
            prevX.next = currY
        else:
            head = currY

        if prevY:
            prevY.next = currX
        else:
            head = currX

        if currX.next == currY:
            currX.next = currY.next
            currY.next = currX
        else:
            temp = currX.next
            currX.next = currY.next
            currY.next = temp

        return head

