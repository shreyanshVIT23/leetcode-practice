# 🧠 LeetCode Problem Solutions

This repository contains Python solutions to two classic problems from [LeetCode](https://leetcode.com/):

1. **234. Palindrome Linked List**
2. **367. Valid Perfect Square**

Each solution includes a clear explanation and implementation logic.

---

## 📘 Problem 1: [234. Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)

### ✅ Objective

Determine whether a singly linked list is a **palindrome** (reads the same forward and backward).

### 💡 Approach

* Traverse the entire linked list and store each node’s value in a list.
* Compare that list to its reversed version using slicing (`[::-1]`).
* If they are equal, the linked list is a palindrome.

### 🧾 Code

```python
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
```

### 🔧 Helper

```python
def arrayToLinkedList(array: List[int]):
    head = ListNode(array[0])
    current = head
    for i in range(1, len(array)):
        current.next = ListNode(array[i])
        current = current.next
    return head
```

### 🧪 Example

```python
sol = Solution()
print(sol.isPalindrome(arrayToLinkedList([1, 2, 3, 2, 1])))  # Output: True
```

---

## 📘 Problem 2: [367. Valid Perfect Square](https://leetcode.com/problems/valid-perfect-square/)

### ✅ Objective

Determine whether a given positive integer is a **perfect square** (i.e., the square of an integer).

---

### 🧪 Version 1: Linear Search

```python
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 1
        while i**2 <= num:
            if i**2 == num:
                return True
            i += 1
        return False
```

* ✅ Simple and intuitive.
* ❌ Slower for large numbers (Time: O(√n))

---

### 🧪 Version 2: Floating Point Check (Clever but Risky)

```python
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return num**0.5 == (num**0.5) // 1
```

* ✅ Short and works well for small/medium inputs.


## 🧠 Concepts Used

* Linked List Traversal
* List Comparison
* Loop-based Square Checking
* Integer Square Root vs Floating Point Pitfalls

---

