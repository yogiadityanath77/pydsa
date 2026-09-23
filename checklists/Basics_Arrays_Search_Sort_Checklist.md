# Python Basics / Arrays / Searching / Sorting — DSA Checklist

**Current level:** Patterns in progress  
**Progress:** Python basics and array fundamentals are well covered. Binary search
and its variants are strong. Basic sorts done. **Sliding window is now done on
arrays** (6 of 8 Level 4 window items, in `02_arrays/sliding_window.py`). The
remaining gaps are **prefix sum, Kadane, matrices, modified binary search, and
merge/quick sort**.  
**Last updated:** 2026-09-23

Companion files: `Linked_List_Python_Checklist.md`, `Strings_Python_Checklist.md`  
Level 4 practice file: `02_arrays/arrays_level4.py` (stubs + tests); sliding window solutions in `02_arrays/sliding_window.py`

---

## 🟢 Level 0 — Python Basics: Lists

- [x] Create, index, and mutate a list
- [x] Negative indexing
- [x] `append()` / `pop()` / `pop(index)`
- [x] Iterate with a `for` loop
- [x] `len()`, manual sum, manual max/min
- [x] Count occurrences of a value
- [x] Reverse a list manually (two-pointer swap)
- [x] Copy a list (`.copy()`) and understand reference vs copy
- [x] Compute an average
- [x] Build a list of unique values preserving order
- [ ] List comprehensions (`[x*2 for x in nums if x > 0]`)
- [ ] Slicing (`nums[1:4]`, `nums[::-1]`, `nums[::2]`)
- [ ] `enumerate()` — index + value in one loop
- [ ] `zip()` — walk two lists together
- [ ] `sorted()` with `key=` and `lambda`
- [ ] Nested / 2D lists (`grid[i][j]`)

## 🟢 Level 0 — Python Basics: Tuples & Sets

- [x] Tuple indexing, negative indexing, iteration
- [x] `.count()` and `.index()` on a tuple
- [x] Tuple unpacking (`a, b, c = t`)
- [x] Immutability — convert to list, mutate, convert back
- [x] Swap first and last elements of a tuple
- [x] Sum a tuple manually
- [x] Set `add()` / `discard()`
- [x] Membership testing (`x in s`) — O(1) average
- [x] Deduplicate a list with `set()`
- [x] Manual set intersection
- [x] Detect duplicates using a set
- [ ] Set union / difference / symmetric difference
- [ ] When to reach for a set vs a dict vs a list

## 🟢 Level 0 — Python Basics: Dicts

- [x] `get()` / `[]` set / `pop()`
- [x] `.keys()`, `.values()`, `.items()`
- [x] Iterate key–value pairs
- [x] Build a frequency map from a list
- [x] Build a frequency map from a string's characters
- [x] `dict.get(key, 0) + 1` idiom
- [x] Find the key with the maximum value
- [x] Merge two dicts, summing shared keys
- [x] Invert a dict (swap keys and values)
- [x] First repeating element via dict
- [ ] `collections.Counter`
- [ ] `collections.defaultdict`
- [ ] Dict comprehensions

---

## 🟢 Level 1 — Arrays: Fundamentals

- [x] Traverse and print
- [x] Sum of all elements
- [x] Largest element
- [x] Smallest element
- [x] Min and max in a single pass
- [x] Count even and odd numbers
- [x] Second largest element (single pass, no sorting)
- [x] Check whether an array is sorted
- [x] Reverse an array (two-pointer, in place)
- [x] Reverse an array into a new array
- [x] Left rotate by 1 position
- [ ] Left rotate by **k** positions (reversal algorithm)
- [ ] Right rotate by k positions
- [ ] Remove a given element in place, return new length
- [ ] Find the leaders in an array (element greater than all to its right)

## 🟡 Level 2 — Arrays: Two-Pointer Patterns

- [x] Reverse in place
- [x] Palindrome check
- [x] Move zeroes to the end (write-pointer)
- [x] Remove duplicates from a **sorted** array
- [x] Pair sum on a sorted array (two pointers)
- [x] Merge two sorted arrays
- [ ] Sort an array of 0s, 1s, 2s (Dutch National Flag)
- [ ] Three-sum (sort + two pointers)
- [ ] Container with most water
- [ ] Union of two sorted arrays
- [ ] Intersection of two sorted arrays
- [ ] Trapping rain water (hard, later)

## 🟡 Level 3 — Arrays: Hashing Patterns

- [x] Frequency count with a dict
- [x] First repeating element (dict, two-pass)
- [x] First repeating element (set, single pass)
- [x] First non-repeating element
- [x] Pair sum / Two Sum on an unsorted array (complement lookup)
- [x] Count distinct elements
- [x] Majority element via frequency map
- [ ] Majority element via **Boyer–Moore voting** (O(1) space)
- [ ] Missing number (sum formula and XOR)
- [ ] Single number — every other element appears twice (XOR)
- [ ] Longest consecutive sequence
- [ ] Subarray with a given sum (hashmap of prefix sums)
- [ ] Group anagrams

## 🟡 Level 4 — Arrays: Patterns (in progress)

Practice file: `02_arrays/arrays_level4.py`. Every item below has a stub and tests there,
in the same order. Sliding window solutions live in `02_arrays/sliding_window.py`.
`[~]` = written but not yet correct — see 🐞 Fixes to revisit. **E / M** = Easy / Medium.

### Sliding window — fixed size
- [x] Max sum of k consecutive elements (E) — `max_sum_arrays` in `sliding_window.py`
- [x] Maximum average subarray I (LC 643 · E) — `max_average`
- [x] Maximum points you can obtain from cards (LC 1423 · M) — `max_score`; window over the part you *don't* take

### Sliding window — variable size
- [x] Smallest subarray with sum ≥ target (LC 209 · M) — `min_subarray_len`
- [x] Longest subarray with sum = k, **positives only** (M) — `longest_subarray_sum_k`
- [x] Max consecutive ones III — flip at most k zeroes (LC 1004 · M) — `longest_ones`
- [ ] Fruit into baskets (LC 904 · M) — at most 2 distinct; redo of `longest_at_most_k_distinct` on arrays
- [ ] Binary subarrays with sum (LC 930 · M) — at-most trick: `atMost(k) - atMost(k-1)`

### Prefix sum
- [ ] Build a prefix-sum array + range sum in O(1) (LC 303 · E)
- [ ] Equilibrium / pivot index (LC 724 · E)
- [ ] Count subarrays with sum k (LC 560 · M) — prefix sum + hashmap of counts
- [ ] Longest subarray with sum = k, **with negatives** (M) — prefix sum + first-seen index
- [ ] Product of array except self (LC 238 · M) — prefix and suffix products

### Kadane's algorithm
- [ ] Maximum subarray sum (LC 53 · M)
- [ ] Maximum subarray sum with indices returned (M)
- [ ] Maximum product subarray (LC 152 · M) — track max **and** min

### Stock / greedy scan
- [ ] Best time to buy and sell stock (LC 121 · E) — one pass, running min
- [ ] Best time to buy and sell stock II (LC 122 · M) — add every rise

### 🧭 Which pattern to use
- **Looking for a minimum** → start the answer at `float('inf')`, then convert it
  back (usually to 0) at the end if nothing was found. Starting at 0 means
  `min()` can never move. For a maximum, start at 0 only when the answer cannot
  be negative — Kadane needs `float('-inf')` or `nums[0]`.
- **Contiguous subarray and all numbers positive** → sliding window (the sum only
  grows as the window grows, so shrinking from the left is safe).
- **Negatives or zeros allowed** → prefix sum + hashmap. A window can't know
  when to shrink.
- **"Count subarrays with exactly k …"** → `atMost(k) - atMost(k-1)`, the same
  trick as `count_exactly_k` in `strings.py`.
- **"Best sum ending here"** → Kadane: restart the running sum when it would
  drag the next element down.
- Longest subarray with sum = k is in the checklist twice on purpose: once with
  positives (window) and once with negatives (prefix sum). Solving both is the
  clearest way to see the difference.

## 🔵 Level 5 — 2D Arrays / Matrices (not started)

- [ ] Traverse a 2D list row-wise and column-wise
- [ ] Row sums and column sums
- [ ] Transpose a matrix
- [ ] Rotate a matrix 90° in place
- [ ] Spiral traversal
- [ ] Search a sorted 2D matrix

---

## 🟢 Searching — Level A: Basics

- [x] Linear search
- [x] Binary search (iterative)
- [ ] Binary search (recursive)
- [x] First occurrence of a target
- [x] Last occurrence of a target
- [x] Lower bound (first index with `arr[i] >= target`)
- [x] Upper bound (last index with `arr[i] <= target`)
- [ ] Count occurrences of a value using first + last occurrence
- [ ] Floor and ceiling of a number in a sorted array
- [ ] Search insert position

## 🟡 Searching — Level B: Modified Binary Search

- [ ] Search in a rotated sorted array
- [ ] Find the minimum in a rotated sorted array
- [ ] Find a peak element
- [ ] Find the single non-duplicate element in a sorted array
- [ ] Search in a sorted 2D matrix

## 🔵 Searching — Level C: Binary Search on the Answer

- [ ] Integer square root
- [ ] First bad version
- [ ] Koko eating bananas / minimum capacity problems
- [ ] Split array into k parts minimising the largest sum

> **Note:** overflow-safe midpoint (`mid = left + (right - left) // 2`) does not
> matter in Python (unbounded ints), but is worth knowing for interviews in
> C++/Java.

---

## 🟢 Sorting — Level A: Basic Sorts

- [x] Bubble sort (with early-exit `swapped` flag)
- [x] Selection sort
- [x] Insertion sort
- [ ] Know the time/space complexity of each by heart
- [ ] Know which of the three are **stable** and why it matters

## 🟡 Sorting — Level B: Divide and Conquer

- [ ] Merge sort (needs the merge-two-sorted-arrays step you already have)
- [ ] Quick sort (Lomuto or Hoare partition)
- [ ] Understand the recursion tree and why both are O(n log n)
- [ ] Quick sort worst case and why pivot choice matters

## 🔵 Sorting — Level C: Specialised

- [ ] Counting sort
- [ ] Cycle sort (the key trick for "missing/duplicate number in 1..n" problems)
- [ ] Python's built-in `.sort()` / `sorted()` with `key=` and `reverse=`
- [ ] Sort a list of tuples/dicts by a chosen field

---

## 🐞 Fixes to revisit

- [ ] `arrays.py` — the file is almost entirely commented out. Consider
      converting it to functions with a `main()`, like `search.py` and
      `sorting.py`

---

## ⭐ Must-Solve Before Moving to Trees / Graphs

- [x] Two Sum (hashing)
- [x] Two Sum II (sorted, two pointers)
- [x] Remove Duplicates from Sorted Array
- [x] Move Zeroes
- [x] Merge Sorted Array
- [x] Majority Element
- [x] Binary Search
- [x] Find First and Last Position in Sorted Array
- [ ] Best Time to Buy and Sell Stock
- [ ] Maximum Subarray (Kadane)
- [ ] Longest Substring Without Repeating Characters (sliding window)
- [ ] Search in Rotated Sorted Array
- [ ] Sort Colors (Dutch National Flag)
- [ ] Missing Number
- [ ] Single Number
- [ ] Merge Sort (implement from scratch)
- [ ] Product of Array Except Self (prefix/suffix)

---

## 🎯 Core Patterns to Master

- [x] Linear scan with an accumulator (sum / max / count)
- [x] Two pointers — opposite ends converging
- [x] Two pointers — slow/fast write pointer (in-place compaction)
- [x] Hash map for counting
- [x] Hash set for membership / complement lookup
- [x] Binary search on a sorted array
- [x] Binary search with an `answer` variable (bounds/occurrence variants)
- [x] Sliding window — fixed size (arrays: `sliding_window.py`; strings: `strings.py`)
- [x] Sliding window — variable size (arrays: `longest_ones`, `longest_subarray_sum_k`; strings: `strings.py`)
- [ ] At-most-k trick for counting exactly k (on arrays)
- [ ] Prefix sum
- [ ] Prefix sum + hashmap (counts / first-seen index / remainders)
- [ ] Kadane / running-best scan
- [ ] Divide and conquer (merge sort, quick sort)
- [ ] Binary search on the answer space
- [ ] Matrix / 2D index manipulation

---

### Current assessment

**What is genuinely solid:** Python basics across lists, tuples, sets and dicts;
array traversal and two-pointer work; hashing patterns; binary search (the
first/last-occurrence and lower/upper-bound variants in `03_searching/search.py`);
and sliding window, both fixed and variable size, on strings *and* now on arrays.

**The real gaps, in priority order:**

1. **Finish sliding window** — only 904 (fruit into baskets) and 930 (binary
   subarrays with sum, the at-most-k trick) are left in Level 4.
2. **Prefix sum** — unlocks subarray-sum problems, and 560 is the one that shows
   why a window stops working once negatives appear.
3. **Kadane's algorithm** — one small problem, appears constantly.
4. **Merge sort** — you already wrote the merge step for two sorted arrays;
   wrapping recursion around it is the natural next step, and it feeds directly
   into Sort List (LeetCode 148) on the linked-list side.
5. **Modified binary search** (rotated array, peak element) — a direct extension
   of what `03_searching/search.py` already does.
6. **2D arrays** — needed before any grid/matrix or graph work.

**Suggested order:**

> 904 + 930 → prefix sum → Kadane → stock (121, 122) → merge sort →
> modified binary search → 2D arrays

The week-by-week version of this is in `Phase2_Roadmap.md`.

**Do not** start trees or graphs until prefix sum and 2D array traversal are
comfortable — trees and graphs assume both.
