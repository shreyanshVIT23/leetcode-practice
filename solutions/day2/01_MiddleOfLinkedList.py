# Title: 876. Middle of the Linked List
# URL: https://leetcode.com/problems/middle-of-the-linked-list/
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Calculate Length
        length = 0
        curr = head
        while curr:
            curr = curr.next
            length+=1
        length = (length)//2 if length%2 != 0 else (length+1)//2
        while length > 0:
            head = head.next
            length -= 1
        return head
        