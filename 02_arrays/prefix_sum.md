# Prefix Sum — Complete Notes

> Level 4 — Arrays: Patterns · Code lives in `02_arrays/prefix_sum.py`
>
> Read top to bottom to relearn the topic from zero. Every solution in this
> file has been run and checked against a brute force.

---

## 0. Quick recall (read this first when revising)

- **Prefix sum = running total.** `prefix[i]` = sum of the first `i` numbers.
- **Pad with a 0 at the front.** `prefix = [0, ...]`, length `n + 1`.
- **Range sum:** `sum(nums[l..r]) = prefix[r + 1] - prefix[l]`
- **Every subarray sum = later running total − earlier running total.**
- **Counting subarrays with a property?** Walk once, keep a running total, and
  ask a dictionary *"how many earlier totals would pair with me?"*
- **Longest subarray with a property?** Same walk, but the dictionary stores
  the **first index** of each total, never overwritten.
- **Divisible by k?** Same walk, but use the **remainder** `total % k` as the key.
- **Negatives in the array?** Sliding window breaks. Prefix sum doesn't care.
- **Starting value of the dictionary** plays the role of the padding 0:
  `{0: 1}` for counting, `{0: -1}` for longest.
- **Order inside the loop:** look up first, then record yourself.

---

## 1. The concept

### 1.1 The problem prefix sums solve

"What is the sum of `nums[l..r]`?" A loop answers it in O(n). But if you are
asked many such questions on the same array, you keep re-adding the same
numbers. Prefix sums do the adding once, then answer every question in O(1).

### 1.2 Odometer analogy

A car's odometer shows total km driven:

```
Start:      0 km
Pune:      20 km
Lonavala:  70 km
Mumbai:   150 km
```

Pune → Mumbai = `150 - 20 = 130 km`. You never re-add the roads.
**Distance between two points = later reading − earlier reading.**
A prefix array is the odometer of an array.

### 1.3 Building it

```
index:     0   1   2   3   4   5
nums:          3   1   4   1   5
prefix:    0   3   4   8   9  14
```

Rule: `prefix[i + 1] = prefix[i] + nums[i]`, starting from `prefix[0] = 0`.

### 1.4 Why the leading 0 (padding)

Without it, a range starting at index 0 has no "before" slot and needs an
`if l == 0` special case — the classic off-by-one bug. With it:

- `prefix[i]` = sum of the first `i` numbers
- `prefix[0]` = sum of zero numbers = 0
- `prefix[r + 1]` = everything up to and including `r`
- `prefix[l]` = everything strictly before `l`

### 1.5 The formula, checked

```
sum(nums[l..r]) = prefix[r + 1] - prefix[l]
```

- `l = 1, r = 3`: `prefix[4] - prefix[1] = 9 - 3 = 6` → `1 + 4 + 1` ✓
- `l = 0, r = 2`: `prefix[3] - prefix[0] = 8 - 0 = 8` → `3 + 1 + 4` ✓ (no special case)
- `l = r = 1`:   `prefix[2] - prefix[1] = 4 - 3 = 1` → just `nums[1]` ✓

Negatives change nothing: `[4, -2, 3]` → `[0, 4, 2, 5]`, and `sum(0..1) = 2 - 0 = 2` ✓

### 1.6 Code

```python
def build_prefix(nums):
    prefix = [0]
    for num in nums:
        prefix.append(prefix[-1] + num)   # previous total + current number
    return prefix


def range_sum(prefix, left, right):
    return prefix[right + 1] - prefix[left]
```

Build: O(n) time, O(n) space. Each query: O(1).

Python shortcut (know it, but write the loop in interviews until it's automatic):

```python
from itertools import accumulate
prefix = [0] + list(accumulate(nums))
```

---

## 2. Recognising the pattern

Reach for prefix sums when you see:

- "sum of a **range** / subarray", especially **many** range queries
- "**count** subarrays whose sum equals / is divisible by ..."
- "**longest** subarray whose sum ..."
- "left side sum vs right side sum"
- "**equal number** of X and Y" (turn one into +1, the other into −1)
- the array **contains negatives or zeros** and the question is about subarray sums

### Prefix sum vs sliding window

| | Sliding window | Prefix sum + hashmap |
|---|---|---|
| Works with negatives? | No — the sum must grow when the window grows | Yes |
| Typical question | longest/shortest window satisfying a condition | count / longest subarray with exact sum, divisibility |
| Space | O(1) | O(n) (or O(k) for remainders) |

Rule of thumb: **all positive → window is often enough. Negatives, zeros, "exactly k", or "divisible by" → prefix sum.**

---

## 3. The four templates

### Template A — range queries

```python
prefix = [0]
for num in nums:
    prefix.append(prefix[-1] + num)
# sum(l..r) = prefix[r + 1] - prefix[l]
```

### Template B — count subarrays (dictionary of counts)

```python
count = 0
total = 0
seen = {0: 1}                 # total 0 exists once, before the list starts
for num in nums:
    total += num
    key = total - k           # what earlier total would pair with me?
    if key in seen:
        count += seen[key]
    if total in seen:
        seen[total] += 1
    else:
        seen[total] = 1
```

### Template C — longest subarray (dictionary of first index)

```python
best = 0
total = 0
first_seen = {0: -1}          # total 0 "at index -1", before the list starts
for i, num in enumerate(nums):
    total += num
    if total in first_seen:
        best = max(best, i - first_seen[total])
    else:
        first_seen[total] = i # only the first time — never overwrite
```

### Template D — divisibility (remainder as the key)

Same as B, but the key is `total % k`, and you look up that same remainder.

### Side by side

| | 560 (count, = k) | 525 (longest, balanced) | 974 (count, divisible) |
|---|---|---|---|
| Transform numbers? | no | `0 → -1` | no |
| Dictionary key | running total | running total | `total % k` |
| Look up | `total - k` | `total` | `total % k` |
| Dictionary value | how many times | first index | how many times |
| Start | `{0: 1}` | `{0: -1}` | `{0: 1}` |
| Update | always `+1` | only if new | always `+1` |
| Answer | add to count | max of lengths | add to count |

---

## 4. LC 303 · Range Sum Query – Immutable (Easy)

### Question

You get an array once. Then `sumRange(left, right)` is called many times. Return
the sum of `nums[left..right]` (inclusive) each time.

```
NumArray([-2, 0, 3, -5, 2, -1])
sumRange(0, 2) → 1
sumRange(2, 5) → -1
sumRange(0, 5) → -3
```

### Logic

Many queries on the same array = Template A. Build the prefix array once in
`__init__`, answer each query with one subtraction.

### Trace

```
index:    0    1    2    3    4    5    6
prefix:   0   -2   -2    1   -4   -2   -3
```

- `sumRange(0, 2)` → `prefix[3] - prefix[0] = 1 - 0 = 1`
- `sumRange(2, 5)` → `prefix[6] - prefix[2] = -3 - (-2) = -1`
- `sumRange(0, 5)` → `prefix[6] - prefix[0] = -3`

### Code

```python
class NumArray:
    def __init__(self, nums):
        self.prefix = [0]
        for num in nums:
            self.prefix.append(self.prefix[-1] + num)

    def sumRange(self, left, right):
        return self.prefix[right + 1] - self.prefix[left]
```

### Explanation

- `__init__` runs **once**, so the O(n) work goes there.
- The prefix array is stored on `self`. A plain local variable would vanish
  when `__init__` ends and `sumRange` couldn't see it.
- `sumRange` runs **many times** and is O(1).

### Complexity

Build O(n) time, O(n) space. Each query O(1).

---

## 5. LC 724 · Find Pivot Index (Easy)

### Question

Find an index where the sum of everything **left** of it equals the sum of
everything **right** of it. The pivot itself is on neither side. Return the
leftmost such index, or `-1`.

```
[1, 7, 3, 6, 5, 6] → 3     (1+7+3 = 11 = 5+6)
[1, 2, 3]          → -1
[2, 1, -1]         → 0     (left is empty = 0, right = 1 + -1 = 0)
```

### Logic

Everything is either left, at `i`, or right. So:

```
right = total - left - nums[i]
```

Keep `left` as a running total. You only ever need the current left sum, so one
variable replaces the whole prefix array.

### Trace (`total = 28`)

```
i  nums[i]  left  right = 28 - left - nums[i]  equal?
0     1       0         27                      no
1     7       1         20                      no
2     3       8         17                      no
3     6      11         11                      yes → 3
```

### Code

```python
def pivot_index(nums):
    total = sum(nums)
    left = 0
    for i, num in enumerate(nums):
        right = total - left - num
        if left == right:
            return i
        left += num          # AFTER the check
    return -1
```

Without `enumerate`:

```python
def pivot_index(nums):
    total = sum(nums)
    left = 0
    for i in range(len(nums)):
        right = total - left - nums[i]
        if left == right:
            return i
        left += nums[i]
    return -1
```

### Pitfalls

- `left += num` must come **after** the check. At index `i`, the left side must
  not include `nums[i]`.
- Index 0 can be the answer (empty left side counts as 0).
- Scanning left to right means the first match is automatically the leftmost.

### Complexity

O(n) time, O(1) space.

### Side note: `enumerate`

```python
for i, num in enumerate(nums):     # i = index, num = value
for i in range(len(nums)):         # same thing; value is nums[i]
enumerate(nums, start=1)           # counter starts at 1, values unchanged
```

Use `range(len(...))` when you also need neighbours like `nums[i + 1]`.

---

## 6. LC 560 · Subarray Sum Equals K (Medium) ⭐ the core problem

### Question

Count how many **subarrays** (continuous, no gaps, original order, non-empty)
have sum exactly `k`. Numbers can be negative.

```
[1, 2, 3], k = 3                 → 2    ([1,2], [3])
[1, 1, 1], k = 2                 → 2    (two different [1,1] — positions matter)
[1, -1, 1], k = 1                → 3
[3, 4, 7, 2, -3, 1, 4, 2], k = 7 → 4
```

### Brute force (O(n²))

Every start, extend the end one step at a time, keep a running total.

```python
def subarray_sum_brute(nums, k):
    count = 0
    for start in range(len(nums)):
        total = 0                          # new start → reset
        for end in range(start, len(nums)):
            total += nums[end]
            if total == k:
                count += 1
    return count
```

Too slow for n = 20,000. The waste: every new start re-adds numbers.

### Idea 1 — a subarray sum is a difference of running totals

`[2, 1, 3]` → running totals `0, 2, 3, 6`.

```
subarray    later − earlier   sum
[2]            2 − 0           2
[2, 1]         3 − 0           3 ✓
[2, 1, 3]      6 − 0           6
[1]            3 − 2           1
[1, 3]         6 − 2           4
[3]            6 − 3           3 ✓
```

So the question becomes: **count pairs (earlier, later) of running totals with
`later − earlier = k`.**

### Idea 2 — walk forward, look back for one number

Standing at running total `current`, you need an earlier total with
`current − earlier = k`, i.e.

```
earlier = current − k
```

Look first, then record yourself (so a total never pairs with itself).

### Idea 3 — a dictionary makes the lookup instant

Store `running total → how many times seen`. Counts matter because with
negatives the same total can appear more than once, and each appearance is a
different subarray.

### Trace (`[1, -1, 1]`, `k = 1`)

```
num  current  need = current − 1  in seen?  count  seen after
 —      0            —               —        0    {0:1}
 1      1            0            yes (1)     1    {0:1, 1:1}
-1      0           -1            no          1    {0:2, 1:1}
 1      1            0            yes (2)     3    {0:2, 1:2}
```

At the last step 0 was seen **twice** → two subarrays end here:
`[1, -1, 1]` and the last `[1]`. A set would wrongly count 1.

### Stepping stone (list version, O(n²) — for understanding only)

```python
def subarray_sum_list(nums, k):
    count = 0
    current = 0
    passed = [0]
    for num in nums:
        current += num
        count += passed.count(current - k)
        passed.append(current)
    return count
```

### Final code

```python
def subarray_sum(nums, k):
    count = 0
    current = 0
    seen = {0: 1}                 # total 0 seen once, before we start

    for num in nums:
        current += num
        need = current - k
        if need in seen:
            count += seen[need]
        if current in seen:
            seen[current] += 1
        else:
            seen[current] = 1

    return count
```

Short form with `.get` (returns 0 when the key is missing):

```python
def subarray_sum(nums, k):
    count = 0
    current = 0
    seen = {0: 1}
    for num in nums:
        current += num
        count += seen.get(current - k, 0)
        seen[current] = seen.get(current, 0) + 1
    return count
```

### Why `{0: 1}`

It's the padding 0. Without it, subarrays starting at index 0 are never
counted (in `[1, 2, 3]`, `k = 3`, the subarray `[1, 2]` is found only because
0 is already in `seen`).

### Link to Two Sum

Two Sum: "have I seen `target − num`?" (set/dict of values).
560: "how many times have I seen `current − k`?" (dict of counts of running totals).

### Complexity

O(n) time, O(n) space.

---

## 7. LC 525 · Contiguous Array (Medium)

### Question

Array of only 0s and 1s. Return the **length of the longest** subarray with an
**equal number** of 0s and 1s (0 if none).

```
[0, 1]          → 2
[0, 1, 0]       → 2
[0, 1, 1, 0, 1] → 4     ([0, 1, 1, 0])
[1, 1, 1]       → 0
```

### Brute force (O(n²))

```python
def find_max_length_brute(nums):
    best = 0
    for start in range(len(nums)):
        zeros = 0
        ones = 0
        for end in range(start, len(nums)):
            if nums[end] == 0:
                zeros += 1
            else:
                ones += 1
            if zeros == ones:
                best = max(best, end - start + 1)
    return best
```

`end - start + 1` = length of `nums[start..end]`.

### Idea 1 — turn 0 into −1

Balanced means the +1s and −1s cancel: **balanced ⇔ sum 0**.

```
[0, 1]       → -1 + 1         = 0 ✓
[0, 1, 1, 0] → -1 + 1 + 1 - 1 = 0 ✓
[1, 1]       →  1 + 1         = 2 ✗
```

### Idea 2 — sum 0 ⇔ the same running total appears twice

`later − earlier = 0` ⇒ `later = earlier`. The subarray is everything between
the two appearances.

### Idea 3 — longest ⇒ remember the FIRST index of each total

The farthest-back match gives the longest subarray, so store the first index
and never overwrite it. Length = `i − first_seen[total]`.

Start with `{0: -1}`: total 0 exists "before index 0", so a total of 0 at index
`i` gives length `i − (−1) = i + 1` (the whole prefix).

### Trace (`[0, 1, 1, 0, 1]`)

```
i  num  ±1  total  seen before?     length          best  first_seen after
0   0   -1   -1    no → store          —              0   {0:-1, -1:0}
1   1   +1    0    yes, at -1     1 - (-1) = 2        2   (unchanged)
2   1   +1    1    no → store          —              2   {0:-1, -1:0, 1:2}
3   0   -1    0    yes, at -1     3 - (-1) = 4        4   (unchanged)
4   1   +1    1    yes, at 2       4 - 2 = 2          4   (unchanged)
```

### Code

```python
def find_max_length(nums):
    first_seen = {0: -1}
    total = 0
    best = 0

    for i, num in enumerate(nums):
        if num == 0:
            total -= 1
        else:
            total += 1

        if total in first_seen:
            best = max(best, i - first_seen[total])
        else:
            first_seen[total] = i

    return best
```

### Pitfalls

- Overwriting `first_seen[total]` on later appearances → shorter answers.
- Starting with `{0: 0}` instead of `{0: -1}` → every length from the start is 1 too short.

### Complexity

O(n) time, O(n) space.

---

## 8. LC 974 · Subarray Sums Divisible by K (Medium)

### Question

Count subarrays whose sum is **divisible by `k`** (`sum % k == 0`; note that
0 and negative multiples like −5 also count).

```
[2, 3, 5], k = 5              → 3   ([5], [2, 3], [2, 3, 5])
[5, 0], k = 5                 → 3   ([5], [0], [5, 0])
[4, 5, 0, -2, -3, 1], k = 5   → 7
```

### Brute force (O(n²))

560's brute force with one change: `total == k` → `total % k == 0`.

```python
def subarrays_div_by_k_brute(nums, k):
    count = 0
    for start in range(len(nums)):
        total = 0
        for end in range(start, len(nums)):
            total += nums[end]
            if total % k == 0:
                count += 1
    return count
```

### Idea — same remainder ⇒ difference divisible

```
later  earlier  later % 5  earlier % 5  difference  divisible?
 17       7         2           2           10         yes
 10       5         0           0            5         yes
 17       8         2           3            9         no
```

**Two running totals with the same remainder differ by a multiple of `k`.**
(Clock analogy: 3 o'clock and 15 o'clock land on the same spot because they
differ by exactly 12.)

So: dictionary of `remainder → how many times seen`, look up the current
remainder itself, start with `{0: 1}`.

### Trace (`[4, 5, 0, -2, -3, 1]`, `k = 5`)

```
num  total  rem  seen before?  count  seen after
 —     0     0       —           0    {0:1}
 4     4     4      no           0    {0:1, 4:1}
 5     9     4      yes (1)      1    {0:1, 4:2}
 0     9     4      yes (2)      3    {0:1, 4:3}
-2     7     2      no           3    {0:1, 4:3, 2:1}
-3     4     4      yes (3)      6    {0:1, 4:4, 2:1}
 1     5     0      yes (1)      7    {0:2, 4:4, 2:1}
```

### Code

```python
def subarrays_div_by_k(nums, k):
    count = 0
    total = 0
    seen = {0: 1}

    for num in nums:
        total += num
        rem = total % k
        if rem in seen:
            count += seen[rem]      # count BEFORE incrementing
            seen[rem] += 1
        else:
            seen[rem] = 1

    return count
```

With `.get`:

```python
        count += seen.get(rem, 0)
        seen[rem] = seen.get(rem, 0) + 1
```

### Negative numbers and `%`

Python always returns a remainder in `0..k-1`: `-3 % 5 == 2`, `-7 % 5 == 3`.
That's correct here (−3 and 2 differ by 5). Java/C++ return `-3`, so there
you'd need `((total % k) + k) % k`. In Python, nothing extra is needed.

### Complexity

O(n) time. At most `k` distinct remainders → O(k) space.

---

## 9. Common mistakes checklist

- [ ] Forgetting the padding 0 / starting dictionary (`{0: 1}` or `{0: -1}`).
- [ ] `prefix[r] - prefix[l]` instead of `prefix[r + 1] - prefix[l]`.
- [ ] Recording the current total **before** looking it up (counts empty
      subarrays when `k = 0`, or pairs a total with itself).
- [ ] Using a **set** when you need **counts** (breaks with negatives / zeros).
- [ ] Overwriting the first index in "longest" problems.
- [ ] Using sliding window when the array has negatives.
- [ ] In 724, adding `nums[i]` to `left` before the comparison.
- [ ] Reading `seen[key]` without checking `key in seen` → `KeyError`.

---

## 10. Extra practice (not yet done)

Try each one **before** opening the solution. The hint names the template.

### LC 930 · Binary Subarrays With Sum (M) — redo with prefix sum

Already solved with sliding window (`at_most` trick). Now solve with Template B.

<details>
<summary>Hint</summary>

It is exactly LC 560 with `k = goal`. Nothing else changes.

</details>

<details>
<summary>Solution</summary>

```python
def num_subarrays_with_sum_prefix(nums, goal):
    count = 0
    total = 0
    seen = {0: 1}
    for num in nums:
        total += num
        count += seen.get(total - goal, 0)
        seen[total] = seen.get(total, 0) + 1
    return count
# [1, 0, 1, 0, 1], goal = 2 → 4
```

</details>

### LC 1248 · Count Number of Nice Subarrays (M) — pattern spotting test

Count subarrays with exactly `k` odd numbers.

<details>
<summary>Hint</summary>

Turn each number into `1` if odd, `0` if even (`num % 2`). "Exactly k odd
numbers" becomes "sum equals k" → LC 560. Same trick family as 0 → −1 in 525.

</details>

<details>
<summary>Solution</summary>

```python
def number_of_subarrays(nums, k):
    count = 0
    total = 0
    seen = {0: 1}
    for num in nums:
        total += num % 2          # 1 if odd, 0 if even
        count += seen.get(total - k, 0)
        seen[total] = seen.get(total, 0) + 1
    return count
# [1, 1, 2, 1, 1], k = 3 → 2
# [2, 4, 6], k = 1 → 0
# [2, 2, 2, 1, 2, 2, 1, 2, 2, 2], k = 2 → 16
```

</details>

### LC 523 · Continuous Subarray Sum (M) — 974 + 525 combined

Return `True` if some subarray of **length ≥ 2** has a sum that is a multiple of `k`.

<details>
<summary>Hint</summary>

Remainders as keys (like 974), but store the **first index** (like 525),
start with `{0: -1}`, and only accept a match if `i − first_index >= 2`.

</details>

<details>
<summary>Solution</summary>

```python
def check_subarray_sum(nums, k):
    first_seen = {0: -1}
    total = 0
    for i, num in enumerate(nums):
        total += num
        rem = total % k
        if rem in first_seen:
            if i - first_seen[rem] >= 2:
                return True
        else:
            first_seen[rem] = i       # keep the earliest index
    return False
# [23, 2, 4, 6, 7], k = 6  → True   ([2, 4])
# [23, 2, 6, 4, 7], k = 13 → False
# [5, 0, 0, 0], k = 3      → True   ([0, 0])
# [1, 0], k = 2            → False
```

Why not overwrite: in `[5, 0, 0, 0]` the remainder 2 repeats every step;
keeping the earliest index is what lets the length reach 2.

</details>

### LC 238 · Product of Array Except Self (M) — next item in the checklist

For each index, the product of every other element, **without division**, O(n).

<details>
<summary>Hint</summary>

Answer at `i` = (product of everything left of `i`) × (product of everything
right of `i`). Build the left products in one pass (prefix), then multiply in
the right products in a backwards pass (suffix). Like 724, a single running
variable per direction is enough.

</details>

<details>
<summary>Solution</summary>

```python
def product_except_self(nums):
    n = len(nums)
    answer = [1] * n

    left = 1
    for i in range(n):
        answer[i] = left          # product of everything before i
        left *= nums[i]

    right = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= right        # times product of everything after i
        right *= nums[i]

    return answer
# [1, 2, 3, 4]      → [24, 12, 8, 6]
# [-1, 1, 0, -3, 3] → [0, 0, 9, 0, 0]
```

Same "record before you add yourself" order as every problem above.

</details>

### Later (after Level 5 — 2D arrays)

- **LC 304 · Range Sum Query 2D (M)** — prefix sums on a grid:
  `P[r+1][c+1] = grid[r][c] + P[r][c+1] + P[r+1][c] - P[r][c]`.
- **LC 1109 · Corporate Flight Bookings (M)** — *difference arrays*, the
  reverse of prefix sums: add `v` at `start`, subtract `v` at `end + 1`, then
  take the prefix sum once at the end to apply every range update.

---

## 11. Self-test (do from memory, no peeking)

1. Build the padded prefix array for `[2, 5, 1, 3]`, then find `sum(1..2)`.
   *(Answer: `[0, 2, 7, 8, 11]`, `8 − 2 = 6`)*
2. Write LC 560 from a blank file in under 10 minutes. Explain why `{0: 1}`.
3. Say out loud the three changes that turn 560 into 525, and the one change
   that turns 560 into 974.
4. Solve LC 1248 without looking at section 10.
5. Why does sliding window fail on `[1, -1, 1]`, `k = 1`, but prefix sum works?

---

## 12. Progress

| # | Problem | Diff | Template | Where |
|---|---|---|---|---|
| — | Build prefix + range sum | — | A | `prefix_sum.py` → `build_prefix`, `range_sum` |
| 303 | Range Sum Query – Immutable | E | A | `prefix_sum.py` → `NumArray` |
| 724 | Find Pivot Index | E | running total | `prefix_sum.py` → `pivot_index` |
| 560 | Subarray Sum Equals K | M | B | `prefix_sum.py` → `subarray_sum` |
| 525 | Contiguous Array | M | C | `prefix_sum.py` → `find_max_length` |
| 974 | Subarray Sums Divisible by K | M | D | `prefix_sum.py` → `subarrays_div_by_k` |
| 930 | Binary Subarrays With Sum (redo) | M | B | ☐ |
| 1248 | Count Number of Nice Subarrays | M | B | ☐ |
| 523 | Continuous Subarray Sum | M | C + D | ☐ |
| 238 | Product of Array Except Self | M | prefix/suffix | ☐ |
