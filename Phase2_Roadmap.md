# Phase 2 Roadmap — Step by Step

**Goal:** finish Phase 2 of `DSA_Master_Checklist.md` (arrays, strings, sliding
window, binary search, linked list, stack & queue) before starting trees and graphs.  
Do the steps in order. Finish a step before starting the next one.

Tick items here **and** in `DSA_Master_Checklist.md`. Numbers are LeetCode IDs.

---

## 🗺️ The map

| Step | Focus | Items |
|:-:|---|:-:|
| 1 | Open bugs · finish sliding window · prefix sum | 4 bugs + 11 |
| 2 | Kadane & stock · binary search refresh | 10 |
| 3 | Modified binary search · binary search on the answer | 10 |
| 4 | Merge sort & quick sort · linked list part 1 | 12 |
| 5 | Linked list part 2 (incl. LRU cache) | 9 |
| 6 | Two pointers · arrays part 1 | 12 |
| 7 | Arrays & hashing part 2 · Python toolkit | 12 |
| 8 | Strings: easy classics | 10 |
| 9 | Strings: building & parsing · matrix start | 10 |
| 10 | Matrix finish · stack & queue basics | 11 |
| 11 | Stack design problems · monotonic stack | 13 |
| ✅ | Phase 2 checkpoint, then start **trees** | — |

**Don't skip items to move on faster.** Leaving gaps is what happened with prefix
sum, and with linked list cycle-start.

---

## 🔁 Rules for every session

1. **Write the time and space complexity as a comment** on every solution. This
   covers checklist section 1.2 as you go.
2. **One revision problem per session** from the step's "Revision" line, solved
   from memory without opening the old file.
3. **Tick an item only if you solved it without looking at a solution.** If you
   needed help, leave it unticked and redo it in the next step.
4. **Commit at the end of each session.** That keeps a record of what you did when.

---

## Step 1 · Bugs + sliding window + prefix sum

*Why first:* you are warm on sliding window. Finishing these 5 closes a topic
completely, and 930 leads straight into prefix sums.

- [x] Fix `02_arrays/questions.py:169` — merge loop should check `len(arr9)`
- [x] Fix `02_arrays/questions.py:36-38` — move zeroes: start at 0, use `arr2[i]`
- [x] Fix `02_arrays/questions_explained.py:90` — move zeroes: start at 0
- [x] Fix `06_linked_list/DLL.py` — `prepend()` should `return True`
- [x] 209 · Minimum Size Subarray Sum · M
- [x] 1004 · Max Consecutive Ones III · M
- [x] 904 · Fruit Into Baskets · M — `total_fruit`
- [x] 1423 · Maximum Points You Can Obtain from Cards · M
- [x] 930 · Binary Subarrays With Sum · M — `num_subarrays_with_sum` + `at_most`
- [x] Prefix-sum array + O(1) range sum (concept) — `build_prefix`, `range_sum`
- [x] 303 · Range Sum Query – Immutable · E — `NumArray`
- [x] 724 · Find Pivot Index · E — `pivot_index`
- [x] 560 · Subarray Sum Equals K · M — `subarray_sum`
- [x] 525 · Contiguous Array · M — `find_max_length`
- [x] 974 · Subarray Sums Divisible by K · M — `subarrays_div_by_k`

**Revision:** two pointers (this is the old batch 5): move zeroes, remove
duplicates from sorted array, pair sum on a sorted array.  
**Done when:** sliding window shows 12 / 12 in the master checklist.  
**Where you are:** ✅ **Step 1 complete** (2026-09-25). Sliding window is 12 / 12,
all 4 bugs are fixed, and all 6 prefix-sum items are done in
`02_arrays/prefix_sum.py` (notes: `02_arrays/prefix_sum.md`). Next: Step 2,
starting with 53 (Kadane).

---

## Step 2 · Kadane + binary search refresh

*Why now:* binary search is your oldest topic. Refresh it before
building on it in step 3.

- [x] 53 · Maximum Subarray · M (Kadane) — `max_subarray`
- [x] 152 · Maximum Product Subarray · M — `max_product`
- [ ] 121 · Best Time to Buy and Sell Stock · E
- [ ] 122 · Best Time to Buy and Sell Stock II · M
- [ ] Re-solve from memory: 704 Binary Search, 34 First and Last Position
- [ ] Re-solve from memory: lower bound and upper bound
- [ ] Recursive binary search
- [ ] 35 · Search Insert Position · E
- [ ] 69 · Sqrt(x) · E
- [ ] 278 · First Bad Version · E

**Revision:** sliding window. Solve 3 and 424 from memory.  
**Done when:** prefix sum & Kadane shows 10 / 10.  
**Where you are:** prefix sum & Kadane is at 8 / 10. 53 and 152 are done in
`02_arrays/kadane.py`; next are 121 and 122, then the binary search refresh.

---

## Step 3 · Modified binary search

- [ ] 33 · Search in Rotated Sorted Array · M
- [ ] 81 · Search in Rotated Sorted Array II · M
- [ ] 153 · Find Minimum in Rotated Sorted Array · M
- [ ] 162 · Find Peak Element · M
- [ ] 540 · Single Element in a Sorted Array · M
- [ ] Binary search on the answer (concept: monotonic yes/no over a range)
- [ ] 875 · Koko Eating Bananas · M
- [ ] 1011 · Capacity To Ship Packages Within D Days · M
- [ ] 1482 · Minimum Number of Days to Make m Bouquets · M
- [ ] 981 · Time Based Key-Value Store · M

**Revision:** sorting (the old batch 7). Write bubble, selection and insertion
sort from scratch.  
**Done when:** binary search shows 17 / 17.

---

## Step 4 · Merge sort + linked list part 1

*Why together:* merge two sorted lists (21) is the merge step of merge sort, and
step 5's Sort List (148) is merge sort on a linked list.

- [ ] Merge sort (from scratch)
- [ ] Quick sort (Lomuto or Hoare partition)
- [ ] Counting sort
- [ ] Cycle sort idea (values in 1..n → index `v - 1`)
- [ ] Stability + time/space of all five sorts, written as a comment table in `sorting.py`
- [ ] 912 · Sort an Array · M
- [ ] Dummy-node technique
- [ ] 21 · Merge Two Sorted Lists · E
- [ ] 83 · Remove Duplicates from Sorted List · E
- [ ] 206 · Reverse Linked List, **recursively**
- [ ] 160 · Intersection of Two Linked Lists · E
- [ ] 142 · Linked List Cycle II · M

**Revision:** array fundamentals. Second largest, rotate by k, check sorted.  
**Done when:** sorting shows 9 / 9.

---

## Step 5 · Linked list part 2

- [ ] 2 · Add Two Numbers · M
- [ ] 2095 · Delete the Middle Node of a Linked List · M
- [ ] 24 · Swap Nodes in Pairs · M
- [ ] 61 · Rotate List · M
- [ ] 328 · Odd Even Linked List · M
- [ ] 143 · Reorder List · M (middle + reverse + merge)
- [ ] 148 · Sort List · M (merge sort)
- [ ] 138 · Copy List with Random Pointer · M
- [ ] 146 · LRU Cache · M (hashmap + your DLL)

**Revision:** prefix sum. Solve 560 from memory.  
**Done when:** linked list shows 24 / 24.

---

## Step 6 · Two pointers + arrays part 1

- [ ] 977 · Squares of a Sorted Array · E
- [ ] 392 · Is Subsequence · E
- [ ] 844 · Backspace String Compare · E
- [ ] 680 · Valid Palindrome II · E
- [ ] 75 · Sort Colors · M (Dutch national flag)
- [ ] 15 · 3Sum · M
- [ ] 11 · Container With Most Water · M
- [ ] 18 · 4Sum · M
- [ ] 169 · Majority Element again, with Boyer–Moore voting
- [ ] 268 · Missing Number · E
- [ ] 136 · Single Number · E
- [ ] 485 · Max Consecutive Ones · E

**Revision:** linked list. Reverse, middle and remove-nth-from-end from memory.  
**Done when:** two pointers shows 12 / 12.

---

## Step 7 · Arrays & hashing part 2 + Python toolkit

- [ ] 189 · Rotate Array · M
- [ ] 1752 · Check if Array Is Sorted and Rotated · E
- [ ] 49 · Group Anagrams · M
- [ ] 347 · Top K Frequent Elements · M
- [ ] 238 · Product of Array Except Self · M
- [ ] 128 · Longest Consecutive Sequence · M
- [ ] 36 · Valid Sudoku · M
- [ ] 229 · Majority Element II · M
- [ ] 31 · Next Permutation · M
- [ ] Toolkit: slicing, comprehensions, `enumerate` / `zip`
- [ ] Toolkit: `sorted(key=lambda ...)`, `Counter`, `defaultdict`
- [ ] Toolkit: `deque`, 2D list creation, `float('inf')`, `divmod`

**Revision:** modified binary search. Solve 33 and 875 from memory.  
**Done when:** arrays & hashing shows 20 / 20.

---

## Step 8 · Strings: easy classics

- [ ] String methods: `split`, `join`, `strip`, `find`, `startswith`, `replace`
- [ ] 387 · First Unique Character in a String · E
- [ ] 14 · Longest Common Prefix · E
- [ ] 205 · Isomorphic Strings · E
- [ ] 796 · Rotate String · E
- [ ] 383 · Ransom Note · E
- [ ] 389 · Find the Difference · E
- [ ] 28 · Find the Index of the First Occurrence in a String · E
- [ ] 13 · Roman to Integer · E
- [ ] 415 · Add Strings · E

**Revision:** Kadane + stock. Solve 53 and 121 from memory.

---

## Step 9 · Strings: building & parsing + matrix start

- [ ] 151 · Reverse Words in a String · M
- [ ] 5 · Longest Palindromic Substring · M (expand around centre)
- [ ] 647 · Palindromic Substrings · M
- [ ] 443 · String Compression · M
- [ ] 12 · Integer to Roman · M
- [ ] 8 · String to Integer (atoi) · M
- [ ] 43 · Multiply Strings · M
- [ ] Row / column / diagonal traversal of a 2D list
- [ ] 867 · Transpose Matrix · E
- [ ] 118 · Pascal's Triangle · E

**Revision:** linked list. Solve 21 and 143 from memory.  
**Done when:** strings shows 20 / 20.

---

## Step 10 · Matrix finish + stack & queue basics

- [ ] 48 · Rotate Image · M
- [ ] 54 · Spiral Matrix · M
- [ ] 73 · Set Matrix Zeroes · M
- [ ] 74 · Search a 2D Matrix · M
- [ ] 240 · Search a 2D Matrix II · M
- [ ] Stack with a list, queue with `deque` (concept)
- [ ] 20 · Valid Parentheses · E
- [ ] 232 · Implement Queue using Stacks · E
- [ ] 225 · Implement Stack using Queues · E
- [ ] 1047 · Remove All Adjacent Duplicates In String · E
- [ ] 155 · Min Stack · M

**Revision:** two pointers. Solve 15 and 75 from memory.  
**Done when:** matrix shows 8 / 8.

---

## Step 11 · Stack design + monotonic stack

- [ ] 150 · Evaluate Reverse Polish Notation · M
- [ ] 71 · Simplify Path · M
- [ ] 394 · Decode String · M
- [ ] 735 · Asteroid Collision · M
- [ ] 622 · Design Circular Queue · M
- [ ] Monotonic stack (concept: next greater / smaller element)
- [ ] 496 · Next Greater Element I · E
- [ ] 503 · Next Greater Element II · M
- [ ] 739 · Daily Temperatures · M
- [ ] 901 · Online Stock Span · M
- [ ] 853 · Car Fleet · M
- [ ] 402 · Remove K Digits · M
- [ ] 907 · Sum of Subarray Minimums · M

**Revision:** strings. Solve 5 and 443 from memory.  
**Done when:** stack & queue shows 19 / 19.

---

## ✅ Checkpoint · Ready for trees?

Before starting Phase 3, pick **6 Mediums you have never seen**, one each from
arrays, sliding window, binary search, linked list, strings and stack. Give
yourself 30 minutes per problem.

- [ ] Solved at least 5 of the 6 without hints → **start trees** (Phase 3.2),
      with recursion (3.1) alongside
- [ ] Solved fewer than 5 → go back and re-solve the ⭐ must-solve
      lists in the detail checklists, then retry with 6 new problems
