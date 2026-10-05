# Searching & Binary Search — Complete Notes

> Searching — Level A + C · Code lives in `03_searching/search.py`
>
> Read top to bottom to relearn the topic from zero. Every solution in this
> file was run and checked against Python's `bisect` / `math.isqrt` or a brute
> force on thousands of inputs.
>
> Rotated arrays and the other Step 3 problems are in `modified_binary_search.md`.

---

## 0. Quick recall (read this first when revising)

- **Binary search needs a sorted yes/no condition:** all ✗ then all ✓ (or the
  reverse). A sorted array is one example; a range of numbers is another.
- **Invariant:** *if the target exists, it is in `nums[left..right]`* (both ends
  included). Every line of the template follows from this.
- **`while left <= right`** — one element is still a search space.
- **`left = mid + 1` / `right = mid - 1`** — `mid` is already checked, so skip it.
  `left = mid` can loop forever.
- **Save the answer and keep going** when you want a boundary:
  - first ✓ → `answer = mid`, `right = mid - 1` (go left)
  - last ✓ → `answer = mid`, `left = mid + 1` (go right)
- **Lower bound** = first index with `nums[i] >= target`.
  **Upper bound** = first index with `nums[i] > target`. Both return
  `len(nums)` if nothing qualifies. One character apart: `>=` vs `>`.
- **When the loop ends without a match:** `left` is on the first bigger
  element, `right` on the last smaller one, and `left = right + 1`.
- **Count of target** = `upper_bound − lower_bound` (no `+1`, no special case).
- **Insert position (35)** = lower bound = `left` at the end of plain binary search.
- **Recursive binary search** costs O(log n) space (call stack). Use iterative.
- **Python never overflows.** In Java/C++ write `mid = left + (right - left) / 2`.

---

## 1. The concept

### 1.1 Linear vs binary search

Linear search checks every element: O(n), works on anything.
Binary search checks the middle, then **throws half away**: O(log n), but only
works when the data is sorted.

```
n           linear (worst)   binary (worst)
1,000           1,000             10
1,000,000   1,000,000             20
2.1 billion 2.1 billion           31
```

### 1.2 Why throwing half away is safe

Sorted array, target 23, you look at the middle and see 16:

```
[2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
               ↑
              16 < 23
```

Every element left of 16 is **even smaller**, so none of them can be 23.
Throw away 16 and everything to its left. One comparison removed half the array.

### 1.3 The invariant

> *If the target exists, it is somewhere in `nums[left..right]`, both ends included.*

| line | why it is written this way |
|---|---|
| `right = len(nums) - 1` | both ends included → `right` must be a real index |
| `while left <= right` | `left == right` is one element — still worth checking |
| `left = mid + 1` | `mid` was checked and was too small → exclude it |
| `right = mid - 1` | `mid` was checked and was too big → exclude it |
| `return -1` after the loop | `left > right` → search space is empty |

**Empty array needs no special case:** `right = -1`, so `0 <= -1` is false and
the loop never runs.

### 1.4 The ✗/✓ picture (the most useful way to think about it)

Write a yes/no question for every position. If the answers are **all ✗ then
all ✓**, binary search can find the boundary.

```
nums        1  2  4  4  4  6  8
>= 4 ?      ✗  ✗  ✓  ✓  ✓  ✓  ✓      ← lower bound = first ✓ = 2
>  4 ?      ✗  ✗  ✗  ✗  ✗  ✓  ✓      ← upper bound = first ✓ = 5
```

```
m           0  1  2  3  4  5
m*m <= 8 ?  ✓  ✓  ✓  ✗  ✗  ✗         ← sqrt(8) = last ✓ = 2
```

```
version     1  2  3  4  5
bad ?       ✗  ✗  ✗  ✓  ✓            ← first bad version = first ✓ = 4
```

Almost every binary search problem is "find the first ✓" or "find the last ✓".

### 1.5 Are the two halves equal?

With `mid = (left + right) // 2`, ignoring `mid` itself:

| window | size | mid | left side | right side |
|---|:-:|:-:|---|---|
| 0..6 | 7 (odd) | 3 | 0..2 → 3 | 4..6 → 3 |
| 0..5 | 6 (even) | 2 | 0..1 → 2 | 3..5 → 3 |
| 0..1 | 2 | 0 | empty → 0 | 1 → 1 |

Equal, or the right side has one more (`//` rounds down). It doesn't matter:
each step drops `mid` plus one side, so the window at least halves → O(log n).

---

## 2. Recognising the pattern

Reach for binary search when you see:

- a **sorted** array and "find / first / last / count / insert position"
- "**O(log n)**" in the constraints or the problem statement
- "**minimise the number of calls**" to some API (278)
- "find the **smallest / largest** value such that …" where the answer lives
  in a range of numbers (69, and later Koko / ship packages)
- a yes/no condition that **flips once** as the value grows

---

## 3. The three templates

### Template A — exact match

```python
left, right = 0, len(nums) - 1
while left <= right:
    mid = (left + right) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
return -1          # or `return left` for the insert position (35)
```

### Template B — first ✓ (save, go left)

```python
answer = len(nums)                 # or -1, depending on the problem
while left <= right:
    mid = (left + right) // 2
    if condition(mid):             # ✓
        answer = mid
        right = mid - 1
    else:                          # ✗
        left = mid + 1
return answer
```

Used by: first occurrence, lower bound, upper bound, 35, 278.

### Template C — last ✓ (save, go right)

```python
answer = -1
while left <= right:
    mid = (left + right) // 2
    if condition(mid):             # ✓
        answer = mid
        left = mid + 1
    else:                          # ✗
        right = mid - 1
return answer
```

Used by: last occurrence, floor, 69.

### Side by side

| | on a match / ✓ | then | finds |
|---|---|---|---|
| Template A | `return mid` | — | any match |
| Template B | `answer = mid` | `right = mid - 1` | first ✓ |
| Template C | `answer = mid` | `left = mid + 1` | last ✓ |

---

## 4. Linear search

### Question

Return the index of the first element equal to `target`, or `-1`.
The array does **not** need to be sorted.

### Code

```python
def linear_search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1
```

### Notes

- Use it when the array is unsorted and you search only once.
  Sorting first costs O(n log n), which is more than one O(n) scan.
- `return i` exits immediately, so no `found` flag or `break` is needed.

### Complexity

O(n) time, O(1) space.

---

## 5. LC 704 · Binary Search (Easy)

### Question

Sorted array of **distinct** integers. Return the index of `target`, or `-1`.
Must be O(log n).

```
[-1, 0, 3, 5, 9, 12], target 9 → 4
[-1, 0, 3, 5, 9, 12], target 2 → -1
```

### Code

```python
def binary_search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
```

### Trace — found (`[2, 5, 8, 12, 16, 23, 38, 56, 72, 91]`, target 23)

```
left  right  mid  nums[mid]  action
 0      9     4      16      16 < 23 → left = 5
 5      9     7      56      56 > 23 → right = 6
 5      6     5      23      found → return 5
```

### Trace — not found (same array, target 20)

```
left  right  mid  nums[mid]  action
 0      9     4      16      left = 5
 5      9     7      56      right = 6
 5      6     5      23      right = 4
 5      4     —       —      left > right → return -1
```

`left` ended at 5 — exactly where 20 would be inserted (see section 10).

### Pitfalls

- `left < right` skips the last element: `binary_search([7], 7)` returns -1.
- `left = mid` instead of `mid + 1` → infinite loop when `left = 5, right = 6`.
- The array **must** be sorted: `binary_search([4, 1, 3], 4)` returns -1.

### Complexity

O(log n) time, O(1) space.

---

## 6. Recursive binary search

### Question

Same as 704, but no loop — the function calls itself on the half that's left.

### Mapping the loop to recursion

| iterative | recursive |
|---|---|
| `while left <= right` keeps going | call again while `left <= right` |
| loop ends → `return -1` | **base case:** `if left > right: return -1` |
| `left = mid + 1` | call with `(mid + 1, right)` |
| `right = mid - 1` | call with `(left, mid - 1)` |

### Code

```python
def binary_search_recursive(nums, target, left, right):
    if left > right:                      # base case: empty → not found
        return -1

    mid = (left + right) // 2

    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return binary_search_recursive(nums, target, mid + 1, right)
    else:
        return binary_search_recursive(nums, target, left, mid - 1)

# first call: binary_search_recursive(nums, target, 0, len(nums) - 1)
```

### Trace — the call stack (target 23)

```
call(0, 9)   mid=4, 16 < 23 → call(5, 9), wait
  call(5, 9)   mid=7, 56 > 23 → call(5, 6), wait
    call(5, 6)   mid=5, found → return 5
  receives 5 → returns 5
receives 5 → returns 5
```

### Pitfalls

- **Forgetting `return` in front of the recursive call.** The answer is found
  deep down, then thrown away, and the function returns `None`.
- **Slicing** (`nums[mid+1:]`) copies the list (O(n)) and breaks the indices.
  Pass `left` and `right` instead.
- **No base case** → `RecursionError`.

### Complexity

O(log n) time, **O(log n) space** — each waiting call sits on the call stack.
The iterative version is O(1) space, so prefer it in interviews.

---

## 7. First and last occurrence

### Question

Sorted array **with duplicates**. Return the index of the first (or last)
copy of `target`, or `-1`.

```
[1, 2, 4, 4, 4, 6, 8], target 4 → first 2, last 4
```

### Why plain binary search isn't enough

It stops at the first match it lands on: `mid = 3`, returns 3. That's *a* 4,
not *the first* 4.

### Logic

When `nums[mid] == target`, you learn two things:

1. The target exists — `mid` is a valid answer if nothing better turns up.
2. The **first** copy is `mid` or somewhere to its **left**.

So: **save `mid`, then keep searching left.** For the last copy, save and
search right. Only that one line differs.

### Code

```python
def first_occurrence(nums, target):
    left = 0
    right = len(nums) - 1
    answer = -1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            answer = mid
            right = mid - 1         # look LEFT for an earlier copy
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return answer


def last_occurrence(nums, target):
    left = 0
    right = len(nums) - 1
    answer = -1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            answer = mid
            left = mid + 1          # look RIGHT for a later copy
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return answer
```

### Trace — first 4 in `[1, 2, 4, 4, 4, 6, 8]`

```
left  right  mid  nums[mid]  action
 0      6     3       4      match → answer = 3, right = 2
 0      2     1       2      2 < 4 → left = 2
 2      2     2       4      match → answer = 2, right = 1
 2      1     —       —      stop → return 2
```

### Trace — last 4

```
left  right  mid  nums[mid]  action
 0      6     3       4      match → answer = 3, left = 4
 4      6     5       6      6 > 4 → right = 4
 4      4     4       4      match → answer = 4, left = 5
 5      4     —       —      stop → return 4
```

### Trace — missing (first 5)

```
 0      6     3       4      4 < 5 → left = 4
 4      6     5       6      6 > 5 → right = 4
 4      4     4       4      4 < 5 → left = 5
 5      4     —       —      stop → answer never set → -1
```

### Pitfalls

- `return mid` on a match → that's plain binary search again.
- Forgetting `answer = -1` before the loop.
- `right = mid` instead of `mid - 1` → infinite loop when `left == right == mid`.
  Excluding `mid` is safe because it's saved in `answer`.
- "Find any match, then walk left with a `while`" is correct but O(n) on
  `[4, 4, 4, ..., 4]`.

### Complexity

O(log n) time, O(1) space each.

---

## 8. LC 34 · Find First and Last Position of Element in Sorted Array (Medium)

### Question

Sorted array (duplicates allowed). Return `[first, last]` index of `target`,
or `[-1, -1]`. Must be O(log n).

```
[5, 7, 7, 8, 8, 10], target 8 → [3, 4]
[5, 7, 7, 8, 8, 10], target 6 → [-1, -1]
[], target 0                  → [-1, -1]
[1], target 1                 → [0, 0]
```

### Logic

Two questions → two functions you already have. If the first search returns
-1, skip the second one.

### Code

```python
def search_range(nums, target):
    first = first_occurrence(nums, target)
    if first == -1:
        return [-1, -1]
    last = last_occurrence(nums, target)
    return [first, last]
```

### Complexity

Two binary searches = 2 log n → O(log n) time. O(1) space.

---

## 9. Count occurrences

### Question

How many times does `target` appear in a sorted array? O(log n).

```
[1, 2, 4, 4, 4, 6, 8]: count(4) = 3, count(6) = 1, count(5) = 0
```

### Logic

All copies sit in one block from `first` to `last`. Elements from index 2 to
index 4 = 2, 3, 4 = **3** elements, so `last − first + 1`.

**Trap:** if the target is missing, `−1 − (−1) + 1 = 1`. Check first.

### Code

```python
def count_occurrences(nums, target):
    first = first_occurrence(nums, target)
    if first == -1:
        return 0
    last = last_occurrence(nums, target)
    return last - first + 1
```

Simpler with bounds (section 10): `upper_bound(nums, t) - lower_bound(nums, t)`.

### Complexity

O(log n) time, O(1) space.

---

## 10. Lower bound and upper bound

### Question

- **Lower bound:** first index with `nums[i] >= target`.
- **Upper bound:** first index with `nums[i] > target`.
- If nothing qualifies, return `len(nums)` ("after the last element").

```
nums     1  2  4  4  4  6  8
index    0  1  2  3  4  5  6
```

| target | lower bound | upper bound |
|:-:|:-:|:-:|
| 4 | 2 | 5 |
| 5 (missing) | 5 | 5 |
| 0 | 0 | 0 |
| 8 | 6 | 7 |
| 10 | 7 | 7 |

For a missing target, both land on the same spot — where it would be inserted.

### Why `len(nums)` and not -1

The question is "where does it belong?". If it's bigger than everything, it
belongs at the end — index `len(nums)`. That's a real position (insert here,
count zero elements after it). Python's `bisect_left` / `bisect_right` do the same.

### Logic

```
nums      1  2  4  4  4  6  8
>= 4 ?    ✗  ✗  ✓  ✓  ✓  ✓  ✓   → lower bound = first ✓
>  4 ?    ✗  ✗  ✗  ✗  ✗  ✓  ✓   → upper bound = first ✓
```

Template B. Only two cases (`==` is part of `>=`).

### Code

```python
def lower_bound(nums, target):
    left = 0
    right = len(nums) - 1
    answer = len(nums)

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] >= target:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer


def upper_bound(nums, target):
    left = 0
    right = len(nums) - 1
    answer = len(nums)

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > target:           # the ONLY difference
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer
```

### Trace — lower bound of 4

```
left  right  mid  nums[mid]  >= 4?  action
 0      6     3       4       yes    answer = 3, right = 2
 0      2     1       2       no     left = 2
 2      2     2       4       yes    answer = 2, right = 1
 2      1     —       —        —     return 2
```

### Trace — upper bound of 4

```
left  right  mid  nums[mid]  > 4?   action
 0      6     3       4       no     left = 4
 4      6     5       6       yes    answer = 5, right = 4
 4      4     4       4       no     left = 5
 5      4     —       —        —     return 5
```

At `mid = 3`, lower bound says "yes, go left" and upper bound says "no, go
right". That one character sends them to opposite ends of the block of 4s.

### What they give you

| you want | use |
|---|---|
| count of target | `upper_bound − lower_bound` |
| insert position (35) | `lower_bound` |
| first occurrence | `i = lower_bound`; valid if `i < len(nums)` and `nums[i] == target` |
| last occurrence | `i = upper_bound − 1`; valid if `i >= 0` and `nums[i] == target` |
| **floor** (last index with `nums[i] <= target`) | `upper_bound − 1` |
| **ceiling** (first index with `nums[i] >= target`) | `lower_bound` |

Note: the old `higher_bound_binary_search` found the last index with
`nums[i] <= target`. That's the **floor**, not the upper bound.

### Complexity

O(log n) time, O(1) space each.

---

## 11. LC 35 · Search Insert Position (Easy)

### Question

Sorted array of **distinct** integers. Return the index of `target` if found,
otherwise the index where it would be inserted to keep the array sorted.
O(log n).

```
[1, 3, 5, 6], target 5 → 2   (found)
[1, 3, 5, 6], target 2 → 1   (between 1 and 3)
[1, 3, 5, 6], target 7 → 4   (end)
[1, 3, 5, 6], target 0 → 0   (front)
```

### Logic

A number is inserted right before the **first element ≥ it**. That is
lower bound, word for word.

### Code — version 1 (reuse)

```python
def search_insert(nums, target):
    return lower_bound(nums, target)
```

### Code — version 2 (standalone: plain binary search, return `left`)

```python
def search_insert_v2(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left
```

### Why `left` is the insert position

- `left = mid + 1` only happens when `nums[mid] < target` → everything
  **before `left`** is smaller (S).
- `right = mid - 1` only happens when `nums[mid] > target` → everything
  **after `right`** is bigger (B).
- In between is "not checked yet" (?). The loop stops the moment that zone is
  empty, so `left = right + 1`.

Trace with S / B / ? labels (`[1, 3, 5, 6, 8, 10]`, target 7):

```
start     1  3  5  6  8  10
          ?  ?  ?  ?  ?  ?
          L              R

mid=2 (5 < 7) → left = 3
          S  S  S  ?  ?  ?
                   L     R

mid=4 (8 > 7) → right = 3
          S  S  S  ?  B  B
                  L,R

mid=3 (6 < 7) → left = 4
          S  S  S  S  B  B
                   R  L          ← stop: left = 4
```

`right` sits on the last smaller element, `left` on the first bigger one.
7 goes between them, at `left`. (`right + 1` is the same number.)

Edge cases fall out on their own:

- bigger than everything → only `left` moves → ends at `len(nums)`
- smaller than everything → only `right` moves → `left` stays 0

### Complexity

O(log n) time, O(1) space.

---

## 12. LC 69 · Sqrt(x) (Easy)

### Question

Non-negative integer `x`. Return its square root **rounded down**, without
`** 0.5`, `math.sqrt` or `pow`.

```
4 → 2      8 → 2 (2.828…)      16 → 4      15 → 3      0 → 0      1 → 1
```

Same as: **the biggest whole `m` with `m * m <= x`.**

### What's new

There's no array. You search **numbers** `0..x`. `mid` is a candidate
answer, not an index.

### Logic

```
m           0  1  2  3  4  5  6  7  8
m * m       0  1  4  9 16 25 36 49 64
<= 8 ?      ✓  ✓  ✓  ✗  ✗  ✗  ✗  ✗  ✗    → last ✓ = 2
```

Template C (last ✓).

### Code

```python
def my_sqrt(x):
    left = 0
    right = x
    answer = 0

    while left <= right:
        mid = (left + right) // 2
        if mid * mid <= x:
            answer = mid
            left = mid + 1          # a bigger number might also fit
        else:
            right = mid - 1         # too big, and so is everything above

    return answer
```

### Trace (`x = 8`)

```
left  right  mid  mid*mid  <= 8?  action
 0      8     4     16      no    right = 3
 0      3     1      1      yes   answer = 1, left = 2
 2      3     2      4      yes   answer = 2, left = 3
 3      3     3      9      no    right = 2
 3      2     —      —       —    return 2
```

At the end `right` is on the last ✓, so `return right` also works.

### Pitfalls

- `mid * mid < x` instead of `<=` → `my_sqrt(16)` returns 3.
- Java/C++: `mid * mid` can overflow — use `mid <= x / mid`.

### Complexity

O(log x) time (about 31 steps for x ≈ 2.1 billion), O(1) space.

---

## 13. LC 278 · First Bad Version (Easy)

### Question

Versions `1..n`. One version is bad, and every version after it is bad too.
An API `isBadVersion(v)` is given. Find the first bad version with as few
API calls as possible.

```
n = 5, first bad = 4 → 4
n = 1, first bad = 1 → 1
```

### Logic

```
version   1  2  3  4  5
bad?      ✗  ✗  ✗  ✓  ✓     → first ✓
```

Template B — lower bound with a function call as the condition.

### Code

```python
# fake API for local testing (LeetCode provides isBadVersion)
first_bad = 4

def is_bad_version(version):
    return version >= first_bad


def first_bad_version(n):
    left = 1                    # versions start at 1, not 0
    right = n
    answer = n                  # at least one bad version is guaranteed

    while left <= right:
        mid = (left + right) // 2
        if is_bad_version(mid):
            answer = mid
            right = mid - 1     # an earlier one might be bad too
        else:
            left = mid + 1      # mid is good → everything before it is good

    return answer
```

On LeetCode: rename to `firstBadVersion` inside `class Solution`, call
`isBadVersion`, and don't paste the fake API.

### Trace (`n = 5`, first bad = 4)

```
left  right  mid  bad?  action
 1      5     3    no   left = 4
 4      5     4    yes  answer = 4, right = 3
 4      3     —     —   return 4          (2 API calls)
```

### The overflow note

This is the classic problem where `(left + right) / 2` overflows in Java/C++:
with `n` near 2.1 billion, `left + right` exceeds the `int` limit.
Use `left + (right - left) / 2` there. Python is unaffected.

### Complexity

O(log n) time, O(1) space.

---

## 14. Side by side

| problem | search over | condition | finds | on ✓ / match |
|---|---|---|---|---|
| 704 | indices | `nums[mid] == target` | any match | `return mid` |
| first occurrence | indices | `== target` | first ✓ | save, go left |
| last occurrence | indices | `== target` | last ✓ | save, go right |
| lower bound / 35 | indices | `nums[mid] >= target` | first ✓ | save, go left |
| upper bound | indices | `nums[mid] > target` | first ✓ | save, go left |
| 69 | numbers `0..x` | `mid * mid <= x` | last ✓ | save, go right |
| 278 | numbers `1..n` | `isBadVersion(mid)` | first ✓ | save, go left |

All O(log n) time, O(1) space (recursive version: O(log n) space).

---

## 15. Common mistakes checklist

- [ ] `while left < right` with the inclusive template → misses the last element.
- [ ] `left = mid` or `right = mid` → infinite loop.
- [ ] `return mid` on a match when you need first/last.
- [ ] Forgetting to set `answer` before the loop (`-1` or `len(nums)`).
- [ ] Count = `last − first + 1` without checking for "not found" first.
- [ ] Lower bound returning -1 instead of `len(nums)` when nothing qualifies.
- [ ] Mixing up `>=` (lower) and `>` (upper).
- [ ] Recursive version without `return` in front of the recursive call.
- [ ] Slicing the list in recursive binary search.
- [ ] Running binary search on an unsorted array.
- [ ] 69: `<` instead of `<=`. 278: starting `left` at 0.
- [ ] Functions that `print` instead of `return` — LeetCode needs the value.

---

## 16. Extra practice (not yet done)

Try each one **before** opening the solution.

### Floor and ceiling of a number (checklist item)

Return the **value** of the floor (largest element `<= target`) and ceiling
(smallest element `>= target`), or -1 if it doesn't exist.

<details>
<summary>Hint</summary>

Floor index = `upper_bound − 1`. Ceiling index = `lower_bound`. Check the
index is inside the array before reading the value.

</details>

<details>
<summary>Solution</summary>

```python
def floor_value(nums, target):
    i = upper_bound(nums, target) - 1
    if i >= 0:
        return nums[i]
    return -1

def ceil_value(nums, target):
    i = lower_bound(nums, target)
    if i < len(nums):
        return nums[i]
    return -1
# [1, 2, 4, 4, 4, 6, 8]: floor(5) = 4, ceil(5) = 6, floor(0) = -1,
#                        ceil(9) = -1, floor(4) = 4, ceil(4) = 4
```

</details>

### LC 374 · Guess Number Higher or Lower (E) — 704 with an API

`guess(num)` returns `-1` if your guess is too high, `1` if too low, `0` if right.

<details>
<summary>Hint</summary>

Template A over the numbers `1..n`. Careful: `-1` means **your guess** is too
high → go left.

</details>

<details>
<summary>Solution</summary>

```python
def guess_number(n):
    left = 1
    right = n
    while left <= right:
        mid = (left + right) // 2
        result = guess(mid)
        if result == 0:
            return mid
        elif result == 1:         # pick is higher
            left = mid + 1
        else:                     # pick is lower
            right = mid - 1
    return -1
# n = 10, pick = 6 → 6
```

</details>

### LC 367 · Valid Perfect Square (E) — 69's sibling

Return `True` if `num` is a perfect square, without `sqrt`.

<details>
<summary>Hint</summary>

Template A over `1..num`, comparing `mid * mid` with `num`.

</details>

<details>
<summary>Solution</summary>

```python
def is_perfect_square(num):
    left = 1
    right = num
    while left <= right:
        mid = (left + right) // 2
        if mid * mid == num:
            return True
        elif mid * mid < num:
            left = mid + 1
        else:
            right = mid - 1
    return False
# 16 → True    14 → False    1 → True
```

</details>

### LC 744 · Find Smallest Letter Greater Than Target (E) — upper bound

Sorted list of letters. Return the smallest letter **strictly greater** than
`target`. If none, wrap around to the first letter.

<details>
<summary>Hint</summary>

Upper bound (`>`), on characters instead of numbers. If it returns
`len(letters)`, return `letters[0]`.

</details>

<details>
<summary>Solution</summary>

```python
def next_greatest_letter(letters, target):
    left = 0
    right = len(letters) - 1
    answer = len(letters)
    while left <= right:
        mid = (left + right) // 2
        if letters[mid] > target:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    if answer == len(letters):
        return letters[0]         # wrap around
    return letters[answer]
# ["c", "f", "j"], "a" → "c"    ["c", "f", "j"], "c" → "f"
# ["x", "x", "y", "y"], "z" → "x"
```

</details>

### LC 2529 · Maximum Count of Positive Integer and Negative Integer (E) — both bounds

Sorted array. Return `max(number of negatives, number of positives)`.
Zeros count as neither. O(log n).

<details>
<summary>Hint</summary>

Negatives = everything before the first element `>= 0` → `lower_bound(nums, 0)`.
Positives = everything from the first element `> 0` → `len − upper_bound(nums, 0)`.

</details>

<details>
<summary>Solution</summary>

```python
def maximum_count(nums):
    negatives = lower_bound(nums, 0)
    positives = len(nums) - upper_bound(nums, 0)
    return max(negatives, positives)
# [-2, -1, -1, 1, 2, 3] → 3    [-3, -2, -1, 0, 0, 1, 2] → 3
# [5, 20, 66, 1314] → 4
```

</details>

---

## 17. Self-test (from memory, no peeking)

1. State the invariant. Use it to explain `<=`, `mid + 1` and `mid - 1`.
2. What does `binary_search([7], 7)` return with `while left < right`? Why?
3. Why does the template handle `[]` with no special case?
4. Write first and last occurrence. Which single line differs?
5. Why is count = `last − first + 1` wrong for a missing target, and why does
   `upper − lower` not have that problem?
6. Lower bound vs upper bound: what's the one-character difference? What do
   they return for target 4 and target 5 in `[1, 2, 4, 4, 4, 6, 8]`?
7. When plain binary search ends without a match, where are `left` and `right`?
   Use that to write 35 without `lower_bound`.
8. 69 and 278: draw the ✗/✓ row. Which one wants the first ✓ and which the last?
9. Why is recursive binary search O(log n) space? What happens without `return`?
10. Why does Java need `left + (right - left) / 2` but Python doesn't?

---

## 18. Progress

| # | Problem | Diff | Template | Where |
|---|---|---|---|---|
| — | Linear search | — | scan | `search.py` → `linear_search` |
| 704 | Binary Search | E | A | `search.py` → `binary_search` |
| — | Recursive binary search | — | A | `search.py` → `binary_search_recursive` |
| — | First / last occurrence | — | B / C | `search.py` → `first_occurrence`, `last_occurrence` |
| 34 | Find First and Last Position | M | B + C | `search.py` → `search_range` |
| — | Count occurrences | — | B + C | `search.py` → `count_occurrences` |
| — | Lower / upper bound | — | B | `search.py` → `lower_bound`, `upper_bound` |
| 35 | Search Insert Position | E | B / A + `left` | `search.py` → `search_insert`, `search_insert_v2` |
| 69 | Sqrt(x) | E | C | `search.py` → `my_sqrt` |
| 278 | First Bad Version | E | B | `search.py` → `first_bad_version` |
| — | Floor and ceiling | — | bounds | ☐ |
| 374 | Guess Number Higher or Lower | E | A | ☐ |
| 367 | Valid Perfect Square | E | A | ☐ |
| 744 | Find Smallest Letter Greater Than Target | E | upper bound | ☐ |
| 2529 | Max Count of Positive and Negative Integer | E | both bounds | ☐ |

Reminder: tick these in `DSA_Master_Checklist.md` and `Phase2_Roadmap.md`
only after solving them from a blank file.
