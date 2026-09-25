# Python Basics / Arrays / Searching / Sorting — DSA Checklist

**Current level:** Patterns in progress  
**Progress:** Python basics and array fundamentals are well covered. Binary search
and its variants are strong. Basic sorts done. **Sliding window is done on
arrays** — all 8 Level 4 window items solved, in `02_arrays/sliding_window.py`.
**Prefix sum is mostly done** — 303, 724, 560, 525 and 974 in
`02_arrays/prefix_sum.py` (notes in `02_arrays/prefix_sum.md`). **Kadane is
done** in `02_arrays/kadane.py` — 53, the with-indices version, and 152. The
remaining gaps are **stock, product-except-self, longest sum = k with negatives, matrices, modified binary search, and merge/quick
sort**.  
**Last updated:** 2026-09-26

Companion files: `Linked_List_Python_Checklist.md`, `Strings_Python_Checklist.md`  
Level 4 practice file: `02_arrays/arrays_level4.py` (stubs + tests); sliding window solutions in `02_arrays/sliding_window.py`; prefix sum solutions in `02_arrays/prefix_sum.py`; Kadane in `02_arrays/kadane.py`

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
- [x] Subarray with a given sum (hashmap of prefix sums) — LC 560, `subarray_sum` in `prefix_sum.py`
- [ ] Group anagrams

## 🟡 Level 4 — Arrays: Patterns (in progress)

Practice file: `02_arrays/arrays_level4.py`. Every item below has a stub and tests there,
in the same order. Sliding window solutions live in `02_arrays/sliding_window.py`;
prefix sum solutions live in `02_arrays/prefix_sum.py`.
`[~]` = written but not yet correct — see 🐞 Fixes to revisit. **E / M** = Easy / Medium.

### Sliding window — fixed size
- [x] Max sum of k consecutive elements (E) — `max_sum_arrays` in `sliding_window.py`
- [x] Maximum average subarray I (LC 643 · E) — `max_average`
- [x] Maximum points you can obtain from cards (LC 1423 · M) — `max_score`; window over the part you *don't* take

### Sliding window — variable size
- [x] Smallest subarray with sum ≥ target (LC 209 · M) — `min_subarray_len`
- [x] Longest subarray with sum = k, **positives only** (M) — `longest_subarray_sum_k`
- [x] Max consecutive ones III — flip at most k zeroes (LC 1004 · M) — `longest_ones`
- [x] Fruit into baskets (LC 904 · M) — at most 2 distinct; redo of `longest_at_most_k_distinct` on arrays — `total_fruit`
- [x] Binary subarrays with sum (LC 930 · M) — at-most trick: `atMost(k) - atMost(k-1)` — `num_subarrays_with_sum` + `at_most`

### Prefix sum
- [x] Build a prefix-sum array + range sum in O(1) (LC 303 · E) — `build_prefix`, `range_sum`, `NumArray`
- [x] Equilibrium / pivot index (LC 724 · E) — `pivot_index`
- [x] Count subarrays with sum k (LC 560 · M) — prefix sum + hashmap of counts — `subarray_sum` (+ `subarray_sum_brute`)
- [x] Contiguous array (LC 525 · M) — 0 → −1, prefix sum + first-seen index — `find_max_length`
- [x] Subarray sums divisible by k (LC 974 · M) — remainder as the key — `subarrays_div_by_k`
- [ ] Longest subarray with sum = k, **with negatives** (M) — prefix sum + first-seen index
      (same template as 525 — should be quick now)
- [ ] Product of array except self (LC 238 · M) — prefix and suffix products

### Kadane's algorithm
- [x] Maximum subarray sum (LC 53 · M) — `max_subarray` in `kadane.py` (+ `max_subarray_brute`)
- [x] Maximum subarray sum with indices returned (M) — `max_subarray_with_indices`
- [x] Maximum product subarray (LC 152 · M) — track max **and** min — `max_product`

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

- [x] `02_arrays/sliding_window.py` — `at_most()` counted `right + left + 1`
      instead of `right - left + 1`. Fixed 2026-09-24; LC 930 now matches brute
      force on every binary array up to length 9.
- [x] `02_arrays/kadane.py` — `max_subarray()` had no `return best`. Fixed
      2026-09-26; matches brute force on 5,000 random arrays
- [x] `02_arrays/kadane.py` — `max_product()` used `max` for `cur_min`. Fixed
      2026-09-26; `[-2, 3, -4]` now gives 24 and it matches brute force on 5,000
      random arrays
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
- [x] Longest Substring Without Repeating Characters (sliding window) — `05_strings/strings.py`
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
- [x] At-most-k trick for counting exactly k (on arrays) — `at_most` + `num_subarrays_with_sum`
- [x] Prefix sum — `build_prefix`, `NumArray`, `pivot_index`
- [x] Prefix sum + hashmap (counts / first-seen index / remainders) — 560, 525, 974
- [x] Kadane / running-best scan — `max_subarray`, `max_subarray_with_indices`, `max_product`
- [ ] Divide and conquer (merge sort, quick sort)
- [ ] Binary search on the answer space
- [ ] Matrix / 2D index manipulation

---

### Current assessment

**What is genuinely solid:** Python basics across lists, tuples, sets and dicts;
array traversal and two-pointer work; hashing patterns; binary search (the
first/last-occurrence and lower/upper-bound variants in `03_searching/search.py`);
sliding window — **complete**, fixed and variable size, on strings *and*
arrays, including the at-most-k counting trick; and **prefix sum** — all three
hashmap variants (counts for 560, first-seen index for 525, remainders for 974).

**The real gaps, in priority order:**

1. **Stock (121, 122)** — the last two items in 2.4; 121 is Kadane-shaped
   (running min instead of running sum).
2. **Finish prefix sum** — longest subarray with sum = k (with negatives) and
   product of array except self (238). Both are small once 525 is solid.
3. **Merge sort** — you already wrote the merge step for two sorted arrays;
   wrapping recursion around it is the natural next step, and it feeds directly
   into Sort List (LeetCode 148) on the linked-list side.
4. **Modified binary search** (rotated array, peak element) — a direct extension
   of what `03_searching/search.py` already does.
5. **2D arrays** — needed before any grid/matrix or graph work.

**Suggested order:**

> ~~prefix sum~~ → ~~Kadane~~ → stock (121, 122) → merge sort →
> modified binary search → 2D arrays

The week-by-week version of this is in `Phase2_Roadmap.md`.

**Do not** start trees or graphs until 2D array traversal is
comfortable (prefix sum is now covered) — trees and graphs assume both.
