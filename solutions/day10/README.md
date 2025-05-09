

# 💡 Bulb Switcher Problem

## Problem Summary

You're given `n` light bulbs, initially all **OFF**. You make `n` passes over the bulbs:

* On the first pass, you toggle every bulb.
* On the second pass, you toggle every 2nd bulb.
* On the third pass, every 3rd bulb.
* ...
* On the `i`-th pass, you toggle every `i`-th bulb.
* You repeat this for `n` passes.

**Goal:** After `n` passes, how many bulbs are ON?

---

## Core Intuition

Each bulb ends up being **toggled once for every divisor** it has.

* For example, bulb `6` is toggled in rounds `1, 2, 3, 6` (because those numbers divide 6).
* Normally, divisors come in pairs: e.g., `2 x 3 = 6`, so toggles happen an even number of times.
* **Perfect squares** are special: e.g., `36` has a divisor pair `(6, 6)`. Since `6` is repeated only once, `36` has an **odd** number of divisors.
* **Only bulbs at positions that are perfect squares** will be toggled an **odd number of times** and hence remain **ON**.

---

## Mathematical Insight

We only need to count how many perfect squares ≤ `n`.

* Perfect squares ≤ `n` are: `1^2`, `2^2`, ..., `k^2` where `k^2 ≤ n`
* So the number of such bulbs is `⌊√n⌋`

---

## Python Code

```python
import math

class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(math.sqrt(n))
```

---

## Time & Space Complexity

* **Time:** O(1)
* **Space:** O(1)

This is a mathematically optimal solution—no need to simulate the process.

---

## Example

```python
sol = Solution()
print(sol.bulbSwitch(25))  # Output: 5 (Perfect squares: 1, 4, 9, 16, 25)
```



# 🧹 Delete the Middle Node of a Linked List

**LeetCode Problem:** [2095](https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/)

## ❓ Problem Statement

Given the `head` of a **singly linked list**, delete the **middle node**, and return the head of the modified list.

* If there are `n` nodes, the middle node is at index `n // 2` (0-indexed).
* If the list has only one node, return `None`.

---

## 🧠 Intuition

There are two common approaches to identify and delete the middle node:

### ✅ Method 1: Two-Pass (Counting)

1. First traverse the list to count its total length.
2. Compute the index of the middle node: `middle = length // 2`.
3. Traverse again until just before the middle node and bypass it using `prev.next = curr.next`.

### ✅ Method 2: Fast & Slow Pointer (One-Pass)

1. Use two pointers: `slow` moves 1 step, `fast` moves 2 steps.
2. When `fast` reaches the end, `slow` will be at the middle node.
3. Use a `prev` pointer to keep track of the node just before `slow` and update `prev.next = slow.next`.

---

## ✅ Python Implementations

### 🔁 Method 1: Count Length First

```python
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None

        length = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1

        middlePos = length // 2

        prev = None
        curr = head
        for _ in range(middlePos):
            prev = curr
            curr = curr.next

        prev.next = curr.next
        return head
```

### 🏃‍♂️🏃‍♂️ Method 2: Fast and Slow Pointer

```python
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

        prev.next = slow.next
        return head
```

---

## 🧪 Example Usage

```python
sol = Solution()
head = arrayToLinkedList([1, 3, 4, 7, 1, 2, 6])
print(printLinkedList(sol.deleteMiddle(head)))  # Output: [1, 3, 4, 1, 2, 6]

head2 = arrayToLinkedList([1, 2, 3, 4])
print(printLinkedList(sol.deleteMiddle(head2)))  # Output: [1, 2, 4]

head3 = arrayToLinkedList([2, 1])
print(printLinkedList(sol.deleteMiddle(head3)))  # Output: [2]
```

---

## ⏱ Time & Space Complexity

| Approach    | Time Complexity | Space Complexity |
| ----------- | --------------- | ---------------- |
| Counting    | O(n)            | O(1)             |
| Fast & Slow | O(n)            | O(1)             |

Both approaches are efficient and run in linear time with constant extra space.


