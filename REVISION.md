# DSA Revision Tracker

Started revision: 2026-08-03 (after a ~45 day gap). Goal is to **revise what's
already covered**, not learn new topics — new topics come after revision is solid.

## Topics already covered (before the gap)

### Python basics (`basics.py`)
- Lists: indexing, mutation, append/pop, iteration, sum/max/count
- Tuples: indexing, unpacking, count/index, immutability
- Sets: add/discard, membership check, dedup via `set()`
- Dicts: get/set, keys/values/items, building frequency maps

### Arrays (`arrays.py`)
- Traversal, sum, max, min, even/odd counts
- Linear search (found/not found)
- Second largest element
- Check if array is sorted
- Reverse array (two-pointer swap)
- Left rotate by 1
- Move zeroes to end (two-pointer)
- Remove duplicates from a **sorted** array (two-pointer)
- First repeating element (dict method + set method)
- First non-repeating element

### Searching (`search.py`)
- Linear search
- Binary search
- Binary search: first occurrence, last occurrence
- Binary search: lower bound, upper bound

### Sorting (`sorting.py`)
- Bubble sort (with early-exit optimization)
- Selection sort
- Insertion sort

### More array patterns (`questions.py`)
- Palindrome check (two-pointer)
- Frequency count via dict
- Two-sum / pair-sum (hashset method + two-pointer method on sorted array)
- Merge two sorted arrays
- Count distinct elements
- Majority element (> n/2 occurrences)

## Not yet covered (park these for later, after revision)
Recursion, stacks/queues, linked lists, trees, graphs, sliding window,
prefix sum, Kadane's algorithm, heaps, dynamic programming.

---

## Revision Plan

Ground-up revision, in the same order it was originally learned. Batches of
**5 questions at a time** in `revision.py`. Flow:
1. Claude adds 5 questions (stub functions) to `revision.py`.
2. You solve them without looking at the old files.
3. Claude reviews your solutions, gives feedback.
4. Move to the next batch only once the current one is solid.

Batch sequence (ground up):
- **Batch 1**: Python basics — lists (sum/avg, largest, count occurrences, unique values, reverse)
- **Batch 2**: Python basics — tuples & sets
- **Batch 3**: Python basics — dicts & frequency maps
- **Batch 4**: Arrays — fundamentals (traversal, second largest, sorted check, rotate)
- **Batch 5**: Arrays — two-pointer patterns (move zeroes, remove dupes, palindrome, pair sum)
- **Batch 6**: Searching — linear + binary search + first/last occurrence + lower/upper bound
- **Batch 7**: Sorting — bubble, selection, insertion (implement from scratch)
- **Batch 8+**: Mixed review pulling from all of the above
- After revision feels solid across all batches -> move to new topics
  (recursion / stacks / linked lists).

---

## Progress Log

| Date | Batch | Status | Notes |
|------------|---------|-------------|-------|
| 2026-08-03 | Batch 1 (lists) | Passed | sum_and_average, find_largest, count_occurrences, unique_values, reverse_list — all correct |
| 2026-08-03 | Batch 2 (tuples & sets) | Assigned | swap_first_last, sum_tuple, set_intersection, has_duplicates, count_in_tuple |
| 2026-08-16 | Batch 2 (tuples & sets) | Passed | swap_first_last, sum_tuple, set_intersection, has_duplicates, count_in_tuple — all correct |
| 2026-08-16 | Batch 3 (dicts) | Passed | word_frequency, key_with_max_value, merge_and_sum, invert_dict, first_repeating_dict — all correct |
