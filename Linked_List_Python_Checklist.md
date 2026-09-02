# Linked List DSA Checklist — Python

**Current level:** Intermediate  
**Progress:** All Level 0 helpers done. Level 1 insertion/deletion complete. Level 2 done except recursive reverse. Palindrome (O(1) space) done. Cycle detection done.  
**Last updated:** 2026-09-01

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
- [ ] Fix `insert_after()`: `self.tail == new_node` is a comparison, should assign; tail-update condition is also wrong
- [ ] Fix `find_kth_from_beginning()`: bounds should be `k < 1 or k > self.length` (k=0 currently under-walks)

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
- [ ] Remove the nth node from the end
- [ ] Delete the middle node
- [ ] Swap nodes in pairs
- [ ] Rotate a linked list
- [ ] Merge two sorted linked lists
- [ ] Add two numbers represented by linked lists
- [ ] Partition a linked list
- [ ] Reverse nodes in groups of K
- [ ] Sort a linked list using merge sort

## 🔵 Level 5 — Doubly Linked List

- [ ] Implement a doubly linked-list `Node`
- [ ] Create a doubly linked list
- [ ] Traverse forward
- [ ] Traverse backward
- [ ] Insert at beginning
- [ ] Insert at end
- [ ] Insert at a given index
- [ ] Delete from beginning
- [ ] Delete from end
- [ ] Delete a given node
- [ ] Reverse a doubly linked list

## 🔵 Level 6 — Advanced Interview Problems

- [ ] Clone a linked list with random pointer
- [ ] Merge K sorted linked lists
- [ ] Flatten a multilevel doubly linked list
- [ ] LRU Cache using HashMap + Doubly Linked List

## ⭐ Must-Solve Before Moving to Trees

- [x] Reverse Linked List
- [x] Find Middle Node
- [x] Kth Node from End
- [ ] Remove Nth Node from End
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

Singly linked-list fundamentals are **done**, and palindrome (O(1) space) is now implemented and verified — it correctly restores the list after comparing.

**Is the checklist too much?** No — it is a full roadmap, not a daily to-do. Levels 4–6 are "later"; you are not behind.

**Should you start DLL now, then do the hard questions?** Not yet. DLL (Level 5) is mostly mechanical prev/next bookkeeping and teaches little you don't already know. Remaining order:

1. **Reverse recursively** (quick, cements the pattern)
2. **Remove nth node from end** (two pointers with a gap)
3. **Merge two sorted lists** (dummy node technique)
4. **Then DLL** as a lighter change of pace
5. Cycle start → Intersection → Reverse K-group

Also clear the outstanding bug fixes (`reverse` empty list, `insert_after` tail update, `find_kth_from_beginning` bounds) before the DLL detour.
