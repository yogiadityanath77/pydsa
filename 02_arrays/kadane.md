# Kadane's Algorithm & Stock Problems — Complete Notes

> Level 4 — Arrays: Patterns · Code lives in `02_arrays/kadane.py` (Kadane) and `02_arrays/stock.py` (stock)
>
> Read top to bottom to relearn the topic from zero. Every solution in this
> file was checked against a brute force on thousands of random inputs.

---

## 0. Quick recall (read this first when revising)

- **Group subarrays by where they END.** The best subarray ends somewhere, so
  best overall = best of "best ending at each index".
- **Kadane (sums):** `current = max(num, current + num)`, `best = max(best, current)`.
  Start fresh when the running sum is negative (it would only drag `num` down).
- **`best` must not start at 0** for max subarray — all-negative arrays have a
  negative answer. Use `nums[0]` (loop from 1) or `float('-inf')` (loop from 0).
- **Keep `best` separate from `current`** — the best subarray may have ended earlier.
- **Products (152):** a negative flips the order, so carry **both** the biggest
  and the smallest product ending here. Compute both from the OLD values.
- **Products + `-inf` breaks** (`-inf × -2 = +inf`, `-inf × 0 = nan`).
  Use `nums[0]`, or `1` for the running max/min.
- **Stock 121 (one trade):** for each sell day, the best buy is the cheapest
  price before it → running minimum. `best` starts at 0 (don't trade).
- **Stock 122 (unlimited trades):** add every day-to-day rise.

---

## 1. The core idea: group by where the subarray ends

For `[2, -3, 4, -1, 2]`, list every subarray by its **last** index:

```
ends at 0 (2):   [2]=2
ends at 1 (-3):  [-3]=-3   [2,-3]=-1
ends at 2 (4):   [4]=4     [-3,4]=1      [2,-3,4]=3
ends at 3 (-1):  [-1]=-1   [4,-1]=3      [-3,4,-1]=0   [2,-3,4,-1]=2
ends at 4 (2):   [2]=2     [-1,2]=1      [4,-1,2]=5    [-3,4,-1,2]=2   [2,-3,4,-1,2]=4
```

Two observations do all the work:

1. **Every group is built from the previous one.** Each subarray ending at `i`
   is either `nums[i]` alone, or a subarray ending at `i − 1` with `nums[i]`
   added on.
2. **You only need each group's winner.** Adding the same number to every item
   in a list keeps the biggest item the biggest. So the previous group's
   biggest is all you need to build this group's biggest.

```
biggest ending here = max(num alone, previous biggest + num)
best overall        = biggest of all the "biggest ending here" values
```

Tournament analogy: each group has a winner; the champion is the strongest
group winner. You never re-check every player.

This "group by end" view is the same one that makes prefix sum + hashmap work
(LC 560): at each end, ask a question about the subarrays ending there.

---

## 2. Recognising the pattern

- "maximum / minimum **sum** of a contiguous subarray" → Kadane
- "maximum **product** of a contiguous subarray" → Kadane with max **and** min
- "best **difference** where the larger comes after the smaller" → running minimum (121)
- "sum of all profitable moves, unlimited moves" → add every positive step (122)
- The answer for position `i` depends only on the answer for `i − 1` → a
  one-pass running variable (this is the simplest form of dynamic programming)

### Starting values — the rule from the checklist

| Looking for | Answer can be negative? | Start `best` at |
|---|---|---|
| Maximum | yes (Kadane, 152) | `nums[0]` or `float('-inf')` |
| Maximum | no (121, 122 — "don't trade" = 0) | `0` |
| Minimum | — | `float('inf')` (convert back at the end if needed) |

---

## 3. LC 53 · Maximum Subarray (Medium)

### Question

Return the largest sum of a non-empty contiguous subarray.

```
[2, -3, 4, -1, 2]                 → 5    ([4, -1, 2])
[-2, 1, -3, 4, -1, 2, 1, -5, 4]   → 6    ([4, -1, 2, 1])
[-3, -1, -2]                      → -1   (must pick at least one number)
```

Notes:

- The best subarray can **include negatives** (`[4, -1, 2]` beats `[4]`).
- Taking everything isn't always best — a negative-sum prefix drags it down.

### Brute force (O(n²))

```python
def max_subarray_brute(nums):
    best = float('-inf')                   # not 0: the answer can be negative
    for start in range(len(nums)):
        total = 0
        for end in range(start, len(nums)):
            total += nums[end]
            best = max(best, total)
    return best
```

### Logic

At each index, the biggest sum ending here is either start fresh (`num`) or
extend (`current + num`). Fresh wins exactly when `current < 0` — "throw away
a bag that's in debt".

### Trace (`[2, -3, 4, -1, 2]`)

```
i  num   extend: current + num   fresh   current   best
0   2            —                  2        2        2
1  -3        2 + (-3) = -1         -3       -1        2
2   4       -1 + 4    =  3          4        4        4    ← fresh start
3  -1        4 + (-1) =  3         -1        3        4
4   2        3 + 2    =  5          2        5        5
```

Check against section 1: the group winners are 2, −1, 4, 3, 5 ✓.

### Why `best` is separate from `current`

`[5, -10, 1]` → `current` goes 5, −5, 1. Returning `current` gives 1, but the
answer is 5 (`[5]` ended at index 0). `best` is a running max of `current`.

### Code — `nums[0]` version

```python
def max_subarray(nums):
    current = nums[0]              # biggest sum ending at index 0
    best = nums[0]
    for i in range(1, len(nums)):  # index 0 already handled
        current = max(nums[i], current + nums[i])
        best = max(best, current)
    return best
```

**Why `range(1, ...)`?** Index 0 has no previous group; its only subarray is
`[nums[0]]`, set before the loop. Starting at 0 would add `nums[0]` twice
(`max(2, 2 + 2) = 4` → final answer 7 instead of 5).

### Code — `float('-inf')` version

```python
def max_subarray(nums):
    current = float('-inf')
    best = float('-inf')
    for num in nums:               # index 0 handled by the loop
        current = max(num, current + num)   # -inf + num = -inf → picks num
        best = max(best, current)
    return best
```

### Another form you'll see online

```python
current = 0
best = float('-inf')
for num in nums:
    current += num
    best = max(best, current)     # update BEFORE resetting
    if current < 0:
        current = 0
```

Same idea. The trap: resetting before updating `best` breaks all-negative
arrays. The `max(num, current + num)` form avoids that trap.

### Complexity

O(n) time, O(1) space.

---

## 4. Maximum Subarray with Indices (Medium, interview follow-up)

### Question

Same as LC 53, but also return where the best subarray starts and ends.

```
[2, -3, 4, -1, 2]                 → (5, 2, 4)    nums[2:5] = [4, -1, 2]
[-3, -1, -2]                      → (-1, 1, 1)
[-2, 1, -3, 4, -1, 2, 1, -5, 4]   → (6, 3, 6)    nums[3:7] = [4, -1, 2, 1]
```

### Logic

Kadane already decides "fresh or extend" at each index. Record *where*:

- Start fresh at `i` → `current_start = i`. Extend → start unchanged.
- `current` beats `best` → `best_start = current_start`, `best_end = i`.

`max()` can't tell you which option won, so both `max()` calls become `if/else`.

### Trace (`[2, -3, 4, -1, 2]`)

```
i  num  decision  current  current_start  new best?  best  best_start  best_end
0   2      —         2          0            —         2       0          0
1  -3   extend      -1          0           no         2       0          0
2   4   fresh        4          2           yes        4       2          2
3  -1   extend       3          2           no         4       2          2
4   2   extend       5          2           yes        5       2          4
```

### Code — `nums[0]` version

```python
def max_subarray_with_indices(nums):
    current = nums[0]
    best = nums[0]
    current_start = 0
    best_start = 0
    best_end = 0

    for i in range(1, len(nums)):
        if nums[i] > current + nums[i]:     # same as: current < 0
            current = nums[i]
            current_start = i
        else:
            current = current + nums[i]

        if current > best:
            best = current
            best_start = current_start
            best_end = i

    return best, best_start, best_end
```

### Code — `float('-inf')` version

```python
def max_subarray_with_indices(nums):
    current = float('-inf')
    best = float('-inf')
    current_start = 0
    best_start = 0
    best_end = 0

    for i in range(len(nums)):              # from 0
        if nums[i] > current + nums[i]:     # always true at i = 0
            current = nums[i]
            current_start = i
        else:
            current = current + nums[i]

        if current > best:
            best = current
            best_start = current_start
            best_end = i

    return best, best_start, best_end
```

### Details

- `nums[i] > current + nums[i]` simplifies to `current < 0`.
- Ties (`current == 0`): this code extends. Same sum either way; be consistent.

---

## 5. LC 152 · Maximum Product Subarray (Medium)

### Question

Return the largest product of a non-empty contiguous subarray.

```
[2, 3, -2, 4]   → 6     ([2, 3])
[-2, 0, -1]     → 0     ([0])
[-2, 3, -4]     → 24    (whole array)
```

### What's different from sums

- **Negative × negative = positive.** A very negative product is one negative
  away from being the answer (`-2 × 3 = -6`, then `-6 × -4 = 24`).
- **Zero wipes everything.** It effectively splits the array into pieces.

### Brute force (O(n²))

```python
def max_product_brute(nums):
    best = float('-inf')
    for start in range(len(nums)):
        product = 1                         # 1 = "nothing yet" for ×
        for end in range(start, len(nums)):
            product *= nums[end]
            best = max(best, product)
    return best
```

### Why plain Kadane fails

Kadane with `×` on `[-2, 3, -4]`: at index 1 it keeps `max(3, -6) = 3` and
throws away −6. At index 2: `max(-4, 3 × -4) = -4`. Returns 3; answer is 24.

### The fix: keep the biggest AND the smallest

Multiplying keeps the order for a positive number but **flips** it for a
negative one:

```
products ending at index 1:   3     -6      biggest 3, smallest -6
× 2:                          6    -12      order kept
× -4:                       -12     24      order flipped: smallest → biggest
```

So carry both. The new biggest and new smallest come from the same three
candidates:

```
num alone,   old biggest × num,   old smallest × num
```

### Trace (`[-2, 3, -4]`)

```
i  num  alone  old max × num   old min × num   new max  new min  best
0  -2    -2        —               —             -2       -2      -2
1   3     3    -2 × 3 = -6     -2 × 3 = -6        3       -6       3
2  -4    -4    3 × -4 = -12    -6 × -4 = 24      24      -12      24
```

### Trace (`[2, 3, -2, 4]`)

```
i  num  alone  max × num  min × num  new max  new min  best
0   2     2       —          —          2        2       2
1   3     3       6          6          6        3       6
2  -2    -2     -12         -6         -2      -12       6
3   4     4      -8        -48          4      -48       6
```

### Zeros handle themselves (`[-2, 0, -1]`)

At the 0, all three candidates are 0, so max and min reset. "`num` alone"
then starts a fresh subarray. Answer 0 ✓.

### Code — `nums[0]` version

```python
def max_product(nums):
    cur_max = nums[0]
    cur_min = nums[0]
    best = nums[0]

    for i in range(1, len(nums)):
        num = nums[i]
        a = cur_max * num          # compute both from the OLD values
        b = cur_min * num
        cur_max = max(num, a, b)
        cur_min = min(num, a, b)
        best = max(best, cur_max)

    return best
```

### Code — loop from 0 (start the running max/min at 1)

```python
def max_product(nums):
    cur_max = 1                    # 1 = "nothing yet" for multiplication
    cur_min = 1
    best = float('-inf')           # only best uses -inf
    for num in nums:
        a = cur_max * num
        b = cur_min * num
        cur_max = max(num, a, b)
        cur_min = min(num, a, b)
        best = max(best, cur_max)
    return best
```

### Pitfalls

- **Update-order bug:**
  ```python
  cur_max = max(num, cur_max * num, cur_min * num)
  cur_min = min(num, cur_max * num, cur_min * num)   # ✗ uses the NEW cur_max
  ```
  Compute `a` and `b` first (or use tuple assignment).
- **`float('-inf')` for `cur_max`/`cur_min` breaks:** `-inf × -2 = +inf`
  (fake huge answer), `-inf × 0 = nan`. In Kadane it was safe because
  `-inf + num` stays `-inf`; multiplication can flip it.

### Complexity

O(n) time, O(1) space.

---

## 6. LC 121 · Best Time to Buy and Sell Stock (Easy)

### Question

`prices[i]` = price on day `i`. Buy once, sell once, on a **later** day.
Return the max profit, or 0 if no trade makes money.

```
[7, 1, 5, 3, 6, 4] → 5    (buy 1 on day 1, sell 6 on day 4)
[7, 6, 4, 3, 1]    → 0    (don't trade)
[3, 1, 4]          → 3
```

You can't "buy 1, sell 7" — 7 is on day 0, before day 1.

### Brute force (O(n²))

```python
def max_profit_brute(prices):
    best = 0                                        # "don't trade" = 0
    for buy in range(len(prices)):
        for sell in range(buy + 1, len(prices)):    # strictly after buy
            best = max(best, prices[sell] - prices[buy])
    return best
```

### Logic — look from the sell day

If you sell on a given day, the best buy is the **cheapest price before it**.
Carry that as a running minimum. (Group by end again: every trade ends on a
sell day.)

### Trace (`[7, 1, 5, 3, 6, 4]`)

```
day  price  min so far  profit if sold today  best
 0     7        7            0                  0
 1     1        1            0                  0
 2     5        1            4                  4
 3     3        1            2                  4
 4     6        1            5                  5
 5     4        1            3                  5
```

### Code

```python
def max_profit(prices):
    min_price = float('inf')    # minimum → start at inf
    best = 0                    # answer can't be negative → start at 0
    for price in prices:
        min_price = min(min_price, price)
        best = max(best, price - min_price)
    return best
```

Updating `min_price` first means "buy and sell the same day" is possible, but
that profit is 0, which can never beat `best ≥ 0` — harmless.

### Complexity

O(n) time, O(1) space.

---

## 7. LC 122 · Best Time to Buy and Sell Stock II (Medium)

### Question

Unlimited trades, but hold at most one share at a time (you may sell and
re-buy on the same day). Return the max total profit.

```
[7, 1, 5, 3, 6, 4] → 7    ((5 − 1) + (6 − 3))
[1, 2, 3, 4, 5]    → 4
[7, 6, 4, 3, 1]    → 0
```

No brute force: choosing buy/sell/nothing on every day is exponential.

### Logic — collect every step up

Profit only happens on the way up. And a long climb equals the sum of its
daily steps:

```
[1, 2, 3, 4, 5]:  one trade 5 − 1 = 4  =  1 + 1 + 1 + 1
```

So compare each day with the day before: rise → add it; fall → skip it.

### Trace (`[7, 1, 5, 3, 6, 4]`)

```
day  price  yesterday  change  add?    profit
 1     1        7        −6     no        0
 2     5        1        +4     yes       4
 3     3        5        −2     no        4
 4     6        3        +3     yes       7
 5     4        6        −2     no        7
```

### Code

```python
def max_profit_ii(prices):
    profit = 0
    for i in range(1, len(prices)):             # compare with yesterday
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]
    return profit
```

`range(1, ...)` because day 0 has no yesterday — and `range(len(...))` beats
`enumerate` here since you need `prices[i - 1]`.

### Complexity

O(n) time, O(1) space.

---

## 8. Side by side

| | 53 (max sum) | 152 (max product) | 121 (one trade) | 122 (unlimited) |
|---|---|---|---|---|
| Carry forward | best sum ending here | best **and** worst product ending here | lowest price so far | yesterday's price |
| Each step | `max(num, cur + num)` | max/min of `num, max×num, min×num` | `price − min_price` | add the rise if positive |
| `best` starts | `nums[0]` / `-inf` | `nums[0]` / `-inf` | `0` | `0` |
| Time / space | O(n) / O(1) | O(n) / O(1) | O(n) / O(1) | O(n) / O(1) |

### Connection: LC 53 is LC 121 on prefix sums

Subarray sum = `current prefix − earlier prefix` (from `prefix_sum.md`). To make
it as large as possible, subtract the **smallest earlier prefix** — exactly
121's "cheapest earlier price":

```python
def max_subarray_via_prefix(nums):
    total = 0
    min_prefix = 0                  # the padding 0: empty prefix before index 0
    best = float('-inf')
    for num in nums:
        total += num
        best = max(best, total - min_prefix)   # sell today
        min_prefix = min(min_prefix, total)    # update AFTER (subarray must be non-empty)
    return best
```

Same answers as Kadane. Seeing this link means prices ≈ prefix sums and
"buy low, sell high" ≈ "maximum subarray".

---

## 9. Common mistakes checklist

- [ ] `best = 0` in Kadane / 152 → wrong on all-negative arrays.
- [ ] Returning `current` instead of `best`.
- [ ] Looping from 0 after already setting `current = nums[0]` (double-counts index 0).
- [ ] 152: updating `cur_max` then using the new value to compute `cur_min`.
- [ ] 152: starting `cur_max`/`cur_min` at `float('-inf')`.
- [ ] 121: letting the sell day come before the buy day (e.g. max − min of the whole array).
- [ ] 121: `min_price = 0` instead of `float('inf')` (min never moves).
- [ ] "Reset when negative" form: resetting `current` before updating `best`.

---

## 10. Extra practice (not yet done)

Try each one **before** opening the solution.

### LC 2016 · Maximum Difference Between Increasing Elements (E) — 121 in disguise

Max `nums[j] − nums[i]` with `i < j` and `nums[i] < nums[j]`; return −1 if none.

<details>
<summary>Hint</summary>

Exactly 121's running minimum. The only differences: the pair must be
*strictly* increasing, and "none" returns −1 instead of 0.

</details>

<details>
<summary>Solution</summary>

```python
def maximum_difference(nums):
    min_so_far = nums[0]
    best = -1
    for x in nums[1:]:
        if x > min_so_far:
            best = max(best, x - min_so_far)
        min_so_far = min(min_so_far, x)
    return best
# [7, 1, 5, 4] → 4    [9, 4, 3, 2] → -1    [1, 5, 2, 10] → 9
```

</details>

### LC 1749 · Maximum Absolute Sum of Any Subarray (M)

Return the max of `abs(sum)` over all subarrays.

<details>
<summary>Hint</summary>

The biggest absolute value is either the biggest sum or the most negative sum.
Run Kadane for the max and a mirrored Kadane for the min, at the same time
(like 152 carries max and min).

</details>

<details>
<summary>Solution</summary>

```python
def max_absolute_sum(nums):
    cur_max = 0
    cur_min = 0
    best = 0                       # abs is never negative → 0 is safe
    for num in nums:
        cur_max = max(num, cur_max + num)
        cur_min = min(num, cur_min + num)
        best = max(best, cur_max, -cur_min)
    return best
# [1, -3, 2, 3, -4] → 5        [2, -5, 1, -4, 3, -2] → 8
```

</details>

### LC 918 · Maximum Sum Circular Subarray (M)

The array wraps around (the end connects to the start). Return the max subarray sum.

<details>
<summary>Hint</summary>

The best subarray either doesn't wrap (plain Kadane), or it wraps — and a
wrapping subarray is "everything except a middle chunk". To make it biggest,
remove the **smallest** middle chunk: `total − min_subarray`. Edge case: if
every number is negative, removing the min chunk removes everything (empty),
so return the plain Kadane max.

</details>

<details>
<summary>Solution</summary>

```python
def max_subarray_sum_circular(nums):
    total = 0
    cur_max = 0
    cur_min = 0
    best_max = float('-inf')
    best_min = float('inf')
    for num in nums:
        total += num
        cur_max = max(num, cur_max + num)
        best_max = max(best_max, cur_max)
        cur_min = min(num, cur_min + num)
        best_min = min(best_min, cur_min)
    if best_max < 0:               # all negative
        return best_max
    return max(best_max, total - best_min)
# [1, -2, 3, -2] → 3     [5, -3, 5] → 10     [-3, -2, -3] → -2
```

</details>

### Later (dynamic programming, after the basics)

The rest of the stock family — **LC 123** (at most 2 trades), **LC 188**
(at most k trades), **LC 309** (cooldown), **LC 714** (fee) — use a
"state machine" DP: track the best profit while *holding* vs *not holding* a
share each day. Revisit them once you reach the DP level.

---

## 11. Self-test (from memory, no peeking)

1. Write LC 53 in both versions (`nums[0]` and `float('-inf')`). Why is
   `best = 0` wrong?
2. For `[5, -10, 1]`, what do `current` and `best` end at, and why do you
   need both?
3. Explain in two sentences why 152 needs the minimum as well as the maximum.
4. Why does `float('-inf')` work for Kadane but not for 152's running max/min?
5. Write 121 and 122 from a blank file. Why does 121 start `best` at 0 but 53
   doesn't?
6. Explain how LC 53 turns into LC 121 using prefix sums.

---

## 12. Progress

| # | Problem | Diff | Idea | Where |
|---|---|---|---|---|
| 53 | Maximum Subarray | M | Kadane | `kadane.py` → `max_subarray` |
| — | Max subarray with indices | M | Kadane + record start | `kadane.py` → `max_subarray_with_indices` |
| 152 | Maximum Product Subarray | M | Kadane, max + min | `kadane.py` → `max_product` |
| 121 | Best Time to Buy and Sell Stock | E | running min | `stock.py` → `max_profit` |
| 122 | Best Time to Buy and Sell Stock II | M | add every rise | `stock.py` → `max_profit_ii` |
| 2016 | Max Difference Between Increasing Elements | E | running min | ☐ |
| 1749 | Maximum Absolute Sum of Any Subarray | M | Kadane max + min | ☐ |
| 918 | Maximum Sum Circular Subarray | M | Kadane + total − min | ☐ |
