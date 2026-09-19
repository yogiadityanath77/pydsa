# DSA Master Checklist — Topic-wise Roadmap (Python)

**Goal:** solve LeetCode **Medium** problems on your own. Hard problems are out of scope.
They are listed only where they are well-known next steps, marked ⚪, and they do
not count toward progress.  
**Last updated:** 2026-09-19

**Built by comparing against:** NeetCode Roadmap / NeetCode 150, Striver's A2Z DSA
Sheet, Blind 75, Grind 75 and LeetCode 75. The topic order below is the order most
of these roadmaps agree on. Every topic that all five treat as core for Medium-level
work is included here.

**Detail files (the item-by-item notes stay there):**
`checklists/Basics_Arrays_Search_Sort_Checklist.md` ·
`checklists/Strings_Python_Checklist.md` · `checklists/Linked_List_Python_Checklist.md` ·
`revision/REVISION.md` · step-by-step plan: `Phase2_Roadmap.md`

**Legend:** `[x]` done · `[ ]` not done · **E / M / H** = LeetCode difficulty ·
⚪ = optional stretch (Hard or rarely asked), not counted · numbers are LeetCode problem IDs.
Premium-only problems are marked 🔒.

---

## 📊 Progress Dashboard

Counts only the core items. ⚪ items are left out.

| # | Topic | Done / Total | Status |
|---|-------|:---:|---|
| 1.1 | Python toolkit for DSA | 8 / 18 | 🟡 In progress |
| 1.2 | Complexity analysis | 0 / 5 | 🔴 Not started |
| 1.3 | Sorting algorithms | 3 / 9 | 🟡 In progress |
| 2.1 | Arrays & hashing | 7 / 20 | 🟡 In progress |
| 2.2 | Two pointers | 4 / 12 | 🟡 In progress |
| 2.3 | Sliding window | 7 / 12 | 🟢 Strong |
| 2.4 | Prefix sum & Kadane | 0 / 10 | 🔴 Not started |
| 2.5 | Matrix / 2D arrays | 0 / 8 | 🔴 Not started |
| 2.6 | Binary search | 3 / 17 | 🟡 In progress |
| 2.7 | Strings | 3 / 20 | 🟡 In progress |
| 2.8 | Linked list | 9 / 24 | 🟡 In progress |
| 2.9 | Stack & queue (incl. monotonic stack) | 0 / 19 | 🔴 Not started |
| 3.1 | Recursion & backtracking | 0 / 17 | 🔴 Not started |
| 3.2 | Binary trees | 0 / 26 | 🔴 Not started |
| 3.3 | Binary search trees | 0 / 10 | 🔴 Not started |
| 3.4 | Heap / priority queue | 0 / 11 | 🔴 Not started |
| 3.5 | Trie | 0 / 4 | 🔴 Not started |
| 4.1 | Graphs | 0 / 28 | 🔴 Not started |
| 4.2 | Greedy | 0 / 10 | 🔴 Not started |
| 4.3 | Intervals | 0 / 6 | 🔴 Not started |
| 4.4 | Dynamic programming — 1D | 0 / 14 | 🔴 Not started |
| 4.5 | Dynamic programming — 2D / grid / strings | 0 / 16 | 🔴 Not started |
| 4.6 | Bit manipulation & math | 0 / 14 | 🔴 Not started |
| | **Total** | **44 / 330** (~13%) | |

### Where you stand against the roadmaps

- **Topics started (8 of 23):** Python basics, basic sorting, arrays, two
  pointers, sliding window, basic binary search, strings (two-pointer / window),
  and linked lists.
- **Your strongest area is sliding window.** It is further along than any other
  topic: you have both templates, the at-most-k → exactly-k trick, and all three
  frequency-array matching problems. Most roadmaps place this about 3 topics in, so
  you are ahead there.
- **The biggest gap is breadth.** Stack/queue, recursion, trees, heaps, graphs, DP
  and greedy are **not started**. On NeetCode 150, about **112 of 150** problems (~75%)
  come from topics you have not started. Most Medium interview questions come
  from trees, graphs, DP and backtracking.
- **Known-missing foundations:** recursion, merge sort, prefix sum, Kadane,
  matrices and stacks. Every roadmap teaches these before trees and graphs.
- **Blind 75 coverage:** **9 / 75** (Two Sum, Contains Duplicate, Valid Anagram,
  Valid Palindrome, Longest Substring Without Repeating Characters, Longest
  Repeating Character Replacement, Reverse Linked List, Linked List Cycle, Remove
  Nth Node From End). Permutation in String, Find All Anagrams and Binary Search
  are done too, and they appear on NeetCode 150 and Grind 75.

### Recommended order from here

> **Finish Phase 2 gaps** (prefix sum + Kadane → stack/queue → modified binary
> search → merge sort) → **recursion** → **backtracking** → **binary trees** →
> **BST** → **heaps** → **graphs** → **greedy + intervals** → **1D DP** →
> **2D DP** → tries, bits and math as you go.

Rule of thumb for "Medium-ready": aim for **~70% of the core items in every topic**,
not 100% of a few topics. A topic is done when you can solve an unseen Medium from
it in about 25–30 minutes.

---

# Phase 1 — Foundations

### 1.1 Python toolkit for DSA
- [x] Lists: index, slice-free mutation, append / pop, iterate
- [x] Tuples: unpacking, immutability
- [x] Sets: add / discard / membership, dedup
- [x] Dicts: get / items, frequency maps, `get(k, 0) + 1`
- [x] Strings: immutability, list + `join()` rebuild
- [x] `ord()` / `chr()` frequency-array idiom
- [x] Classes and nodes (`Node`, `LinkedList`)
- [x] `.isalnum()` / `.lower()` normalising
- [ ] Slicing: `a[i:j]`, `a[::-1]`, `a[::2]`
- [ ] List / dict / set comprehensions
- [ ] `enumerate()` and `zip()`
- [ ] `sorted()` / `.sort()` with `key=lambda` and `reverse=True`
- [ ] `collections.Counter` and `collections.defaultdict`
- [ ] `collections.deque` (queue and BFS)
- [ ] `heapq` (`heappush`, `heappop`, `heapify`, max-heap trick with negatives)
- [ ] `float('inf')`, `//`, `%`, `divmod`, `math.gcd`
- [ ] 2D lists: `[[0] * n for _ in range(m)]` (and why `[[0]*n]*m` is wrong)
- [ ] `@functools.cache` / `lru_cache` for memoisation, `sys.setrecursionlimit`

### 1.2 Complexity analysis
- [ ] Big-O of loops, nested loops, and halving loops (O(n), O(n²), O(log n))
- [ ] Space complexity, including the recursion stack
- [ ] Cost of Python operations: `list.pop(0)` O(n), `in list` O(n), `in set` O(1), slicing O(k)
- [ ] Amortised O(1) (`append`, dynamic arrays)
- [ ] Read constraints → target complexity (n ≤ 10⁵ → O(n log n) or better)

### 1.3 Sorting algorithms
- [x] Bubble sort (with early exit)
- [x] Selection sort
- [x] Insertion sort
- [ ] Merge sort (from scratch)
- [ ] Quick sort (Lomuto or Hoare partition)
- [ ] Stability, and the time/space of each sort by heart
- [ ] Counting sort
- [ ] Cycle sort idea (values in 1..n → index `v - 1`)
- [ ] 912 · Sort an Array · M (implement merge sort to pass it)

---

# Phase 2 — Linear Data Structures & Core Patterns

### 2.1 Arrays & hashing
- [x] 1 · Two Sum · E
- [x] 217 · Contains Duplicate · E
- [x] 26 · Remove Duplicates from Sorted Array · E
- [x] 283 · Move Zeroes · E
- [x] 88 · Merge Sorted Array · E
- [x] 169 · Majority Element · E (frequency-map version)
- [x] Second largest, is-sorted, rotate-by-one, first repeating / non-repeating (fundamentals)
- [ ] 169 again with Boyer–Moore voting (O(1) space)
- [ ] 189 · Rotate Array · M (reversal trick)
- [ ] 268 · Missing Number · E
- [ ] 136 · Single Number · E
- [ ] 485 · Max Consecutive Ones · E
- [ ] 1752 · Check if Array Is Sorted and Rotated · E
- [ ] 49 · Group Anagrams · M
- [ ] 347 · Top K Frequent Elements · M
- [ ] 238 · Product of Array Except Self · M
- [ ] 128 · Longest Consecutive Sequence · M
- [ ] 36 · Valid Sudoku · M
- [ ] 229 · Majority Element II · M
- [ ] 31 · Next Permutation · M
- [ ] ⚪ 41 · First Missing Positive · H

### 2.2 Two pointers
- [x] 125 · Valid Palindrome · E
- [x] 344 · Reverse String · E
- [x] 345 · Reverse Vowels of a String · E
- [x] 167 · Two Sum II – Input Array Is Sorted · M
- [ ] 977 · Squares of a Sorted Array · E
- [ ] 392 · Is Subsequence · E
- [ ] 844 · Backspace String Compare · E
- [ ] 680 · Valid Palindrome II · E
- [ ] 75 · Sort Colors · M (Dutch national flag)
- [ ] 15 · 3Sum · M
- [ ] 11 · Container With Most Water · M
- [ ] 18 · 4Sum · M
- [ ] ⚪ 42 · Trapping Rain Water · H

### 2.3 Sliding window
(Done in `strings.py`. The unticked items are array versions of the same templates.)
- [x] 643 · Maximum Average Subarray I · E (max-sum-of-k version done)
- [x] 1456 · Maximum Number of Vowels in a Substring of Given Length · M
- [x] 3 · Longest Substring Without Repeating Characters · M
- [x] 424 · Longest Repeating Character Replacement · M
- [x] 567 · Permutation in String · M
- [x] 438 · Find All Anagrams in a String · M
- [x] 340 · Longest Substring with At Most K Distinct Characters · M 🔒
- [ ] 209 · Minimum Size Subarray Sum · M
- [ ] 1004 · Max Consecutive Ones III · M
- [ ] 904 · Fruit Into Baskets · M
- [ ] 1423 · Maximum Points You Can Obtain from Cards · M
- [ ] 930 · Binary Subarrays With Sum · M
- [x] ⚪ 992 · Subarrays with K Different Integers · H (string version, `count_exactly_k`)
- [ ] ⚪ 76 · Minimum Window Substring · H
- [ ] ⚪ 239 · Sliding Window Maximum · H (monotonic deque)

### 2.4 Prefix sum & Kadane
- [ ] Build a prefix-sum array; range sum in O(1)
- [ ] 303 · Range Sum Query – Immutable · E
- [ ] 724 · Find Pivot Index · E
- [ ] 560 · Subarray Sum Equals K · M (prefix sum + hashmap)
- [ ] 525 · Contiguous Array · M
- [ ] 974 · Subarray Sums Divisible by K · M
- [ ] 53 · Maximum Subarray · M (Kadane)
- [ ] 152 · Maximum Product Subarray · M
- [ ] 121 · Best Time to Buy and Sell Stock · E
- [ ] 122 · Best Time to Buy and Sell Stock II · M
- [ ] ⚪ 918 · Maximum Sum Circular Subarray · M

### 2.5 Matrix / 2D arrays
- [ ] Row-wise, column-wise and diagonal traversal
- [ ] 867 · Transpose Matrix · E
- [ ] 118 · Pascal's Triangle · E
- [ ] 48 · Rotate Image · M
- [ ] 54 · Spiral Matrix · M
- [ ] 73 · Set Matrix Zeroes · M
- [ ] 74 · Search a 2D Matrix · M
- [ ] 240 · Search a 2D Matrix II · M

### 2.6 Binary search
- [x] 704 · Binary Search · E
- [x] 34 · Find First and Last Position of Element in Sorted Array · M
- [x] Lower bound / upper bound templates
- [ ] Recursive binary search
- [ ] 35 · Search Insert Position · E
- [ ] 69 · Sqrt(x) · E
- [ ] 278 · First Bad Version · E
- [ ] 33 · Search in Rotated Sorted Array · M
- [ ] 81 · Search in Rotated Sorted Array II · M
- [ ] 153 · Find Minimum in Rotated Sorted Array · M
- [ ] 162 · Find Peak Element · M
- [ ] 540 · Single Element in a Sorted Array · M
- [ ] Binary search on the answer (concept: monotonic predicate over a range)
- [ ] 875 · Koko Eating Bananas · M
- [ ] 1011 · Capacity To Ship Packages Within D Days · M
- [ ] 1482 · Minimum Number of Days to Make m Bouquets · M
- [ ] 981 · Time Based Key-Value Store · M
- [ ] ⚪ 410 · Split Array Largest Sum · H
- [ ] ⚪ 4 · Median of Two Sorted Arrays · H

### 2.7 Strings
- [x] 242 · Valid Anagram · E (hashmap + 26-slot array)
- [x] Palindrome / reverse / first repeating char (basics)
- [x] Most frequent character
- [ ] Python string methods: `split`, `join`, `strip`, `find`, `startswith`, `replace`
- [ ] 387 · First Unique Character in a String · E
- [ ] 14 · Longest Common Prefix · E
- [ ] 205 · Isomorphic Strings · E
- [ ] 796 · Rotate String · E
- [ ] 383 · Ransom Note · E
- [ ] 389 · Find the Difference · E
- [ ] 28 · Find the Index of the First Occurrence in a String · E
- [ ] 13 · Roman to Integer · E
- [ ] 415 · Add Strings · E
- [ ] 151 · Reverse Words in a String · M
- [ ] 5 · Longest Palindromic Substring · M (expand around centre)
- [ ] 647 · Palindromic Substrings · M
- [ ] 443 · String Compression · M
- [ ] 12 · Integer to Roman · M
- [ ] 8 · String to Integer (atoi) · M
- [ ] 43 · Multiply Strings · M
- [ ] ⚪ KMP / Rabin–Karp / Z-algorithm (rare at Medium)

### 2.8 Linked list
- [x] Implement a singly linked list (append / pop / insert / remove / get / set)
- [x] Implement a doubly linked list
- [x] 707 · Design Linked List · M
- [x] 206 · Reverse Linked List · E (iterative)
- [x] 876 · Middle of the Linked List · E
- [x] 141 · Linked List Cycle · E
- [x] 234 · Palindrome Linked List · E
- [x] 19 · Remove Nth Node From End of List · M
- [x] 203 · Remove Linked List Elements · E (delete all occurrences)
- [ ] 206 again, recursively
- [ ] Dummy-node technique
- [ ] 21 · Merge Two Sorted Lists · E
- [ ] 83 · Remove Duplicates from Sorted List · E
- [ ] 160 · Intersection of Two Linked Lists · E
- [ ] 142 · Linked List Cycle II · M
- [ ] 2 · Add Two Numbers · M
- [ ] 2095 · Delete the Middle Node of a Linked List · M
- [ ] 24 · Swap Nodes in Pairs · M
- [ ] 61 · Rotate List · M
- [ ] 328 · Odd Even Linked List · M
- [ ] 143 · Reorder List · M
- [ ] 148 · Sort List · M (merge sort on a list)
- [ ] 138 · Copy List with Random Pointer · M
- [ ] 146 · LRU Cache · M (hashmap + DLL)
- [ ] ⚪ 25 · Reverse Nodes in k-Group · H
- [ ] ⚪ 23 · Merge k Sorted Lists · H

### 2.9 Stack & queue (incl. monotonic stack)
- [ ] Stack with a list; queue with `collections.deque`
- [ ] 20 · Valid Parentheses · E
- [ ] 232 · Implement Queue using Stacks · E
- [ ] 225 · Implement Stack using Queues · E
- [ ] 1047 · Remove All Adjacent Duplicates In String · E
- [ ] 155 · Min Stack · M
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
- [ ] ⚪ 84 · Largest Rectangle in Histogram · H

---

# Phase 3 — Recursion & Non-linear Structures

### 3.1 Recursion & backtracking
- [ ] Recursion basics: base case, call stack, return values vs side effects
- [ ] 509 · Fibonacci Number · E
- [ ] 50 · Pow(x, n) · M (fast exponentiation)
- [ ] Generate all subsequences (pick / not-pick template)
- [ ] 78 · Subsets · M
- [ ] 90 · Subsets II · M
- [ ] 77 · Combinations · M
- [ ] 39 · Combination Sum · M
- [ ] 40 · Combination Sum II · M
- [ ] 216 · Combination Sum III · M
- [ ] 46 · Permutations · M
- [ ] 47 · Permutations II · M
- [ ] 17 · Letter Combinations of a Phone Number · M
- [ ] 22 · Generate Parentheses · M
- [ ] 79 · Word Search · M
- [ ] 131 · Palindrome Partitioning · M
- [ ] 1219 · Path with Maximum Gold · M
- [ ] ⚪ 51 · N-Queens · H
- [ ] ⚪ 37 · Sudoku Solver · H

### 3.2 Binary trees
- [ ] Build a `TreeNode`; recursive DFS (pre / in / post order)
- [ ] 144 · Binary Tree Preorder Traversal · E
- [ ] 94 · Binary Tree Inorder Traversal · E (also iteratively with a stack)
- [ ] 145 · Binary Tree Postorder Traversal · E
- [ ] 102 · Binary Tree Level Order Traversal · M (BFS with deque)
- [ ] 104 · Maximum Depth of Binary Tree · E
- [ ] 111 · Minimum Depth of Binary Tree · E
- [ ] 226 · Invert Binary Tree · E
- [ ] 100 · Same Tree · E
- [ ] 101 · Symmetric Tree · E
- [ ] 572 · Subtree of Another Tree · E
- [ ] 110 · Balanced Binary Tree · E
- [ ] 543 · Diameter of Binary Tree · E
- [ ] 112 · Path Sum · E
- [ ] 222 · Count Complete Tree Nodes · E
- [ ] 113 · Path Sum II · M
- [ ] 437 · Path Sum III · M
- [ ] 199 · Binary Tree Right Side View · M
- [ ] 103 · Binary Tree Zigzag Level Order Traversal · M
- [ ] 662 · Maximum Width of Binary Tree · M
- [ ] 236 · Lowest Common Ancestor of a Binary Tree · M
- [ ] 1448 · Count Good Nodes in Binary Tree · M
- [ ] 105 · Construct Binary Tree from Preorder and Inorder Traversal · M
- [ ] 114 · Flatten Binary Tree to Linked List · M
- [ ] 116 · Populating Next Right Pointers in Each Node · M
- [ ] 863 · All Nodes Distance K in Binary Tree · M
- [ ] ⚪ 124 · Binary Tree Maximum Path Sum · H
- [ ] ⚪ 297 · Serialize and Deserialize Binary Tree · H

### 3.3 Binary search trees
- [ ] BST property; why inorder traversal is sorted
- [ ] 700 · Search in a Binary Search Tree · E
- [ ] 108 · Convert Sorted Array to Binary Search Tree · E
- [ ] 653 · Two Sum IV – Input is a BST · E
- [ ] 701 · Insert into a Binary Search Tree · M
- [ ] 450 · Delete Node in a BST · M
- [ ] 98 · Validate Binary Search Tree · M
- [ ] 230 · Kth Smallest Element in a BST · M
- [ ] 235 · Lowest Common Ancestor of a Binary Search Tree · M
- [ ] 173 · Binary Search Tree Iterator · M

### 3.4 Heap / priority queue
- [ ] Heap basics with `heapq`; min-heap vs max-heap (negate values)
- [ ] 703 · Kth Largest Element in a Stream · E
- [ ] 1046 · Last Stone Weight · E
- [ ] 215 · Kth Largest Element in an Array · M
- [ ] 973 · K Closest Points to Origin · M
- [ ] 347 · Top K Frequent Elements · M (heap version)
- [ ] 692 · Top K Frequent Words · M
- [ ] 621 · Task Scheduler · M
- [ ] 767 · Reorganize String · M
- [ ] 355 · Design Twitter · M
- [ ] 1642 · Furthest Building You Can Reach · M
- [ ] ⚪ 295 · Find Median from Data Stream · H

### 3.5 Trie
- [ ] Trie node with a `children` dict and an `end` flag
- [ ] 208 · Implement Trie (Prefix Tree) · M
- [ ] 211 · Design Add and Search Words Data Structure · M
- [ ] 648 · Replace Words · M
- [ ] ⚪ 212 · Word Search II · H

---

# Phase 4 — Graphs, Greedy & Dynamic Programming

### 4.1 Graphs
- [ ] Representations: adjacency list (dict of lists), matrix, grid as an implicit graph
- [ ] BFS template (deque + visited set)
- [ ] DFS template (recursive and iterative)
- [ ] 733 · Flood Fill · E
- [ ] 1971 · Find if Path Exists in Graph · E
- [ ] 200 · Number of Islands · M
- [ ] 695 · Max Area of Island · M
- [ ] 547 · Number of Provinces · M
- [ ] 133 · Clone Graph · M
- [ ] 994 · Rotting Oranges · M (multi-source BFS)
- [ ] 542 · 01 Matrix · M
- [ ] 130 · Surrounded Regions · M
- [ ] 417 · Pacific Atlantic Water Flow · M
- [ ] 785 · Is Graph Bipartite? · M
- [ ] 1091 · Shortest Path in Binary Matrix · M
- [ ] Topological sort (Kahn's BFS and DFS versions)
- [ ] 207 · Course Schedule · M
- [ ] 210 · Course Schedule II · M
- [ ] 802 · Find Eventual Safe States · M
- [ ] Union–Find / DSU (path compression + union by rank)
- [ ] 684 · Redundant Connection · M
- [ ] 1319 · Number of Operations to Make Network Connected · M
- [ ] 721 · Accounts Merge · M
- [ ] Dijkstra with `heapq`
- [ ] 743 · Network Delay Time · M
- [ ] 1631 · Path With Minimum Effort · M
- [ ] 787 · Cheapest Flights Within K Stops · M
- [ ] 1584 · Min Cost to Connect All Points · M (Prim / Kruskal)
- [ ] ⚪ 127 · Word Ladder · H
- [ ] ⚪ 399 · Evaluate Division · M
- [ ] ⚪ Bellman–Ford, Floyd–Warshall (know what they are, rarely coded at Medium)

### 4.2 Greedy
- [ ] Greedy idea: when a local choice is provably safe (exchange argument)
- [ ] 455 · Assign Cookies · E
- [ ] 860 · Lemonade Change · E
- [ ] 55 · Jump Game · M
- [ ] 45 · Jump Game II · M
- [ ] 134 · Gas Station · M
- [ ] 846 · Hand of Straights · M
- [ ] 763 · Partition Labels · M
- [ ] 678 · Valid Parenthesis String · M
- [ ] 1899 · Merge Triplets to Form Target Triplet · M
- [ ] ⚪ 135 · Candy · H

### 4.3 Intervals
- [ ] Sort by start, then merge (the core template)
- [ ] 56 · Merge Intervals · M
- [ ] 57 · Insert Interval · M
- [ ] 435 · Non-overlapping Intervals · M
- [ ] 452 · Minimum Number of Arrows to Burst Balloons · M
- [ ] 986 · Interval List Intersections · M
- [ ] ⚪ 253 · Meeting Rooms II · M 🔒 (free as LintCode 919)

### 4.4 Dynamic programming — 1D
- [ ] Recursion → memoisation → tabulation → space optimisation (do all four on one problem)
- [ ] 70 · Climbing Stairs · E
- [ ] 746 · Min Cost Climbing Stairs · E
- [ ] 1137 · N-th Tribonacci Number · E
- [ ] 198 · House Robber · M
- [ ] 213 · House Robber II · M
- [ ] 740 · Delete and Earn · M
- [ ] 91 · Decode Ways · M
- [ ] 322 · Coin Change · M
- [ ] 139 · Word Break · M
- [ ] 300 · Longest Increasing Subsequence · M
- [ ] 416 · Partition Equal Subset Sum · M (0/1 knapsack)
- [ ] 377 · Combination Sum IV · M
- [ ] 337 · House Robber III · M (DP on trees)

### 4.5 Dynamic programming — 2D / grid / strings
- [ ] Define the state `dp[i][j]` in words before coding
- [ ] 62 · Unique Paths · M
- [ ] 63 · Unique Paths II · M
- [ ] 64 · Minimum Path Sum · M
- [ ] 120 · Triangle · M
- [ ] 931 · Minimum Falling Path Sum · M
- [ ] 221 · Maximal Square · M
- [ ] 1143 · Longest Common Subsequence · M
- [ ] 72 · Edit Distance · M
- [ ] 516 · Longest Palindromic Subsequence · M
- [ ] 97 · Interleaving String · M
- [ ] 518 · Coin Change II · M (unbounded knapsack)
- [ ] 494 · Target Sum · M
- [ ] 309 · Best Time to Buy and Sell Stock with Cooldown · M
- [ ] 714 · Best Time to Buy and Sell Stock with Transaction Fee · M
- [ ] 1049 · Last Stone Weight II · M
- [ ] ⚪ 115 · Distinct Subsequences · H
- [ ] ⚪ 312 · Burst Balloons · H (interval DP)

### 4.6 Bit manipulation & math
- [ ] Binary representation; `&`, `|`, `^`, `~`, `<<`, `>>`; `n & (n - 1)`
- [ ] 136 · Single Number · E (XOR)
- [ ] 191 · Number of 1 Bits · E
- [ ] 338 · Counting Bits · E
- [ ] 190 · Reverse Bits · E
- [ ] 231 · Power of Two · E
- [ ] 137 · Single Number II · M
- [ ] 260 · Single Number III · M
- [ ] 371 · Sum of Two Integers · M
- [ ] 9 · Palindrome Number · E
- [ ] 66 · Plus One · E
- [ ] 202 · Happy Number · E
- [ ] 7 · Reverse Integer · M
- [ ] 204 · Count Primes · M (sieve of Eratosthenes)
- [ ] ⚪ 172 · Factorial Trailing Zeroes · M

---

## 🚫 Out of scope for the Medium goal

These show up almost only in Hard problems or competitive programming. Skip them
until you are consistently solving Mediums:

Segment trees · Fenwick / binary indexed trees · sparse tables · KMP / Z-algorithm
(beyond knowing they exist) · suffix arrays · bitmask DP · digit DP · DP on
intervals beyond the basics · strongly connected components (Tarjan / Kosaraju) ·
bridges and articulation points · max flow · advanced geometry.

---

## 🐞 Open bugs carried over from the detail files

Checked on 2026-09-20. The DLL one is fixed; three are still open:

- [ ] `02_arrays/questions.py:169` — merge loop uses `j < len(arr8)`; should be `len(arr9)`
- [ ] `02_arrays/questions.py:36-38` — move zeroes starts at `range(1, ...)` and swaps in `arr[i]` instead of `arr2[i]`
- [ ] `02_arrays/questions_explained.py:90` — move zeroes still starts at `range(1, ...)`; should start at 0
- [x] `06_linked_list/DLL.py` — `prepend()` does not `return True`

---

## 🔁 How to use this file

1. Work top to bottom inside a phase. It is fine to overlap two topics, such as
   stacks alongside binary search.
2. For each problem, write the solution into the matching topic folder. Start a
   new numbered folder for each new topic: `07_stack_queue/`, `08_recursion/`,
   `09_trees/`, `10_graphs/`, `11_dp/`, ...
3. Tick `[x]` only when you have solved it **without looking at a solution**.
   If you needed help, leave it unticked and come back to it in a week.
4. Update the dashboard counts when you finish a section.
5. Keep using `revision/REVISION.md` batches to revisit older topics. Spaced revision is
   what makes the patterns stick.
