# Linked List DSA Checklist — Python

**Current level:** Intermediate  
**Progress:** Singly LL fundamentals + palindrome + remove-nth-from-end done. DLL basics done (backward traverse / DLL reverse descoped for now).  
**Last updated:** 2026-09-09

## 🟢 Level 0 — Linked List Basics

- [x] Create a `Node`
- [x] Create a `LinkedList`
- [x] Store `head`, `tail`, and `length`
- [x] Traverse / print the linked list
- [x] Find the length of a linked list
- [x] Search for a value
- [x] Find the maximum element
- [x] Find the minimum element
- [x] Count occurrences of a value

## 🟢 Level 1 — Basic Operations

### Insertion
- [x] Append / insert at the end
- [x] Prepend / insert at the beginning
- [x] Insert at a given index
- [x] Insert after a given value

### Deletion
- [x] Pop / delete the last node
- [x] Pop first / delete the first node
- [x] Delete at a given index
- [x] Delete by value — first occurrence
- [x] Delete all occurrences of a value

### Implementation fixes to revisit
- [x] Fix `pop()`: `self.head == None` should assign `None`
- [x] Fix `pop_first()`: decrement `self.length`
- [x] Fix `pop_first()`: check `self.length == 0` after decrement
- [x] Fix `remove()`: invalid index should be `index < 0 or index >= self.length`
- [x] Make `append()` return `True` if `insert()` is expected to return a success flag
- [ ] Make `reverse()` handle an empty list safely (still crashes on `temp.next` when `head` is `None`)
- [ ] Fix `insert_after()`: assign fixed, but guard `if temp.next == self.tail` is never true — should be `if new_node.next is None:`
- [ ] Fix `find_kth_from_beginning()`: bounds should be `k < 1 or k > self.length` (still `k < 0`; k=0 returns head)
- [ ] Fix `remove_nth_from_end()`: guard should be `n < 1` not `n < 0` (n=0 currently deletes the last node)

## 🟢 Level 2 — Core Interview Questions

- [x] Reverse a linked list
- [x] Find the middle node
- [x] Find the kth node from the end
- [ ] Reverse a linked list recursively
- [x] Check if a linked list is a palindrome
- [x] Find the kth node from the beginning

## 🟡 Level 3 — Two-Pointer / Cycle Problems

- [x] Detect whether a linked list has a cycle
- [ ] Find the starting node of a cycle
- [ ] Find the length of a cycle
- [ ] Remove a cycle
- [ ] Find the intersection of two linked lists

## 🟡 Level 4 — Medium-Level Manipulation

- [ ] Remove duplicates from a sorted linked list
- [ ] Remove duplicates from an unsorted linked list
- [x] Remove the nth node from the end
- [ ] Delete the middle node
- [ ] Swap nodes in pairs
- [ ] Rotate a linked list
- [ ] Merge two sorted linked lists
- [ ] Add two numbers represented by linked lists
- [ ] Partition a linked list
- [ ] Reverse nodes in groups of K
- [ ] Sort a linked list using merge sort

## 🔵 Level 5 — Doubly Linked List

- [x] Implement a doubly linked-list `Node`
- [x] Create a doubly linked list
- [x] Traverse forward
- [ ] Traverse backward (descoped — revisit if needed)
- [x] Insert at beginning
- [x] Insert at end
- [x] Insert at a given index
- [x] Delete from beginning
- [x] Delete from end
- [x] Delete a given node
- [ ] Reverse a doubly linked list (descoped — revisit if needed)

### DLL fixes to revisit
- [ ] `prepend()` should `return True` (so `insert()` at index 0 returns a flag, not `None`)

## 🔵 Level 6 — Advanced Interview Problems

- [ ] Clone a linked list with random pointer
- [ ] Merge K sorted linked lists
- [ ] Flatten a multilevel doubly linked list
- [ ] LRU Cache using HashMap + Doubly Linked List

## ⭐ Must-Solve Before Moving to Trees

- [x] Reverse Linked List
- [x] Find Middle Node
- [x] Kth Node from End
- [x] Remove Nth Node from End
- [x] Detect Cycle
- [ ] Find Cycle Start
- [x] Palindrome Linked List
- [ ] Intersection of Two Linked Lists
- [ ] Merge Two Sorted Lists
- [ ] Reverse Nodes in K-Group

## 🎯 Core Patterns to Master

- [x] Basic pointer manipulation
- [x] Slow + fast pointers
- [x] Two pointers with a gap
- [ ] Dummy node technique
- [x] In-place reversal
- [ ] Multiple-pointer manipulation

---

### Current assessment

Singly LL fundamentals + palindrome + remove-nth-from-end are done. DLL basics
(build, forward traverse, all insert/delete, bidirectional `get`) are done;
backward traverse and DLL reverse are descoped for now.

**Remaining before strings:**

1. **Reverse recursively** (quick, cements the pattern)
2. **Merge two sorted lists** (dummy node technique) — still need this pattern
3. Cycle start (142) → Intersection (160) → Reverse K-group (25)

**Outstanding one-line bug fixes** (see "fixes to revisit" above):
- `reverse()` — empty-list guard
- `insert_after()` — tail-update guard should be `if new_node.next is None:`
- `find_kth_from_beginning()` — `k < 1` not `k < 0`
- `remove_nth_from_end()` — `n < 1` not `n < 0`

After the merge-sorted + cycle/intersection trio, move to **strings** (easy set,
then sliding window).
