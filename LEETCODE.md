# LeetCode Problems Solved

Every LeetCode problem that is actually solved somewhere in this repo, grouped by
topic. Built by reading the code, not the checklists.

**Total: 30 problems — 17 Easy, 13 Medium, 0 Hard.**
✅ = verified correct · ⚠️ = solved but has a known bug (see 🐞 in the checklists)

| Topic | Solved |
|---|:-:|
| Arrays & hashing | 7 |
| Two pointers | 3 |
| Sliding window | 10 |
| Strings | 1 |
| Binary search | 2 |
| Linked list | 7 |

---

## Arrays & hashing

| # | Problem | Diff | Where | |
|---|---|:-:|---|:-:|
| 1 | Two Sum | E | `02_arrays/questions.py:125` (complement + set) | ✅ |
| 167 | Two Sum II — Input Array Is Sorted | M | `02_arrays/questions.py:139` (two pointers) | ✅ |
| 217 | Contains Duplicate | E | `revision/revision.py` → `has_duplicates` | ✅ |
| 26 | Remove Duplicates from Sorted Array | E | `02_arrays/questions.py:43` | ✅ |
| 283 | Move Zeroes | E | `02_arrays/questions.py:31`, `02_arrays/questions_explained.py:90` | ✅ |
| 88 | Merge Sorted Array | E | `02_arrays/questions.py:161`, `02_arrays/questions_explained.py:308` | ✅ |
| 169 | Majority Element | E | `02_arrays/questions.py:200` (frequency map) | ✅ |

## Two pointers

| # | Problem | Diff | Where | |
|---|---|:-:|---|:-:|
| 125 | Valid Palindrome | E | `05_strings/strings.py` → `is_valid_palindrome` | ✅ |
| 344 | Reverse String | E | `05_strings/strings.py` → `reverse_using_list` | ✅ |
| 345 | Reverse Vowels of a String | E | `05_strings/strings.py` → `reverse_vowels` | ✅ |

## Sliding window

**Fixed size**

| # | Problem | Diff | Where | |
|---|---|:-:|---|:-:|
| 643 | Maximum Average Subarray I | E | `02_arrays/sliding_window.py` → `max_average` | ✅ |
| 1423 | Maximum Points You Can Obtain from Cards | M | `02_arrays/sliding_window.py` → `max_score` | ✅ |
| 1456 | Maximum Number of Vowels in a Substring of Given Length | M | `05_strings/strings.py` → `max_vowels` | ✅ |
| 567 | Permutation in String | M | `05_strings/strings.py` → `check_inclusion` | ✅ |
| 438 | Find All Anagrams in a String | M | `05_strings/strings.py` → `find_anagrams` | ✅ |

**Variable size**

| # | Problem | Diff | Where | |
|---|---|:-:|---|:-:|
| 209 | Minimum Size Subarray Sum | M | `02_arrays/sliding_window.py` → `min_subarray_len` | ✅ |
| 1004 | Max Consecutive Ones III | M | `02_arrays/sliding_window.py` → `longest_ones` | ✅ |
| 3 | Longest Substring Without Repeating Characters | M | `05_strings/strings.py` → `longest_unique_substring` | ✅ |
| 424 | Longest Repeating Character Replacement | M | `05_strings/strings.py` → `character_replacement` | ✅ |
| 340 | Longest Substring with At Most K Distinct Characters 🔒 | M | `05_strings/strings.py` → `longest_at_most_k_distinct` | ✅ |

## Strings

| # | Problem | Diff | Where | |
|---|---|:-:|---|:-:|
| 242 | Valid Anagram | E | `05_strings/strings.py` → `is_anagram` (hashmap) and `is_anagram_using_Frequency_array` (26 slots) | ✅ |

## Binary search

| # | Problem | Diff | Where | |
|---|---|:-:|---|:-:|
| 704 | Binary Search | E | `03_searching/search.py` → `binary_search` | ✅ |
| 34 | Find First and Last Position of Element in Sorted Array | M | `03_searching/search.py` → `binary_search_first_occurrence` + `binary_search_last_occurrence` | ✅ |

## Linked list

All in `06_linked_list/LL.py` unless noted.

| # | Problem | Diff | Where | |
|---|---|:-:|---|:-:|
| 707 | Design Linked List | M | the `LinkedList` class (`get`, `insert`, `remove`, `append`, `prepend`) · doubly version in `DLL.py` | ✅ |
| 206 | Reverse Linked List | E | `reverse` (iterative) | ✅ |
| 876 | Middle of the Linked List | E | `find_middle_node` | ✅ |
| 141 | Linked List Cycle | E | `has_loop` | ✅ |
| 234 | Palindrome Linked List | E | `is_palindrome` | ✅ |
| 19 | Remove Nth Node From End of List | M | `remove_nth_from_end` | ✅ |
| 203 | Remove Linked List Elements | E | `delete_occurances` | ✅ |

---

## Solved here, but not a LeetCode problem

These are classic exercises without a direct LeetCode equivalent. They still
count as practice, they just don't have a number.

**Arrays** (`02_arrays/questions.py`, `revision/revision.py`)
- Reverse an array in place · palindrome check on an array
- Frequency count with a dict · count distinct elements
- First repeating element (dict and set versions) · first non-repeating element
- Second largest · check if sorted · left rotate by one · min and max in one pass
- Count even and odd

**Sliding window** (`02_arrays/sliding_window.py`, `05_strings/strings.py`)
- Max sum of k consecutive elements — `max_sum_arrays`
- Longest subarray with sum = k, positives only — `longest_subarray_sum_k`
- Count substrings with at most k distinct — `count_at_most_K`
- Count substrings with exactly k distinct — `count_exactly_k`
  (the string version of LC 992, which is Hard on arrays)

**Strings** (`05_strings/strings.py`)
- Palindrome check — `is_palindrome` · most frequent character

**Searching** (`03_searching/search.py`)
- Linear search · lower bound · upper bound

**Sorting** (`04_sorting/sorting.py`)
- Bubble sort · selection sort · insertion sort

**Linked list** (`06_linked_list/LL.py`, `DLL.py`)
- Find max · find min · count occurrences · insert after a value
- Kth node from the beginning · kth node from the end
- Doubly linked list: build, traverse, insert and delete at both ends

**Python basics** (`01_basics/basics.py`, `revision/revision.py`)
- Lists, tuples, sets, dicts: frequency maps, merge and sum, invert a dict,
  key with max value, set intersection, unique values

---

## Keeping this file up to date

Add a row whenever you finish a problem, with its number, difficulty and the
function that solves it. Tick the matching line in `DSA_Master_Checklist.md` and
in the topic checklist under `checklists/` at the same time.
