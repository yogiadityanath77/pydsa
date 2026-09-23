"""
====================================================================
 QUESTIONS EXPLAINED
 A clean, explained walkthrough of every problem in questions.py
====================================================================
Each section below has:
  - PROBLEM   : what we're asked to do
  - APPROACH  : the technique/pattern used
  - CONCEPTS  : the underlying DSA ideas
  - COMPLEXITY: time / space
  - CODE      : the working solution
"""


# ====================================================================
# 1. REVERSE AN ARRAY
# ====================================================================
# PROBLEM   : Reverse the elements of an array in place.
# APPROACH  : Two Pointers — one pointer starts at the beginning (left),
#             one at the end (right). Swap the elements they point to,
#             then move left forward and right backward. Stop when
#             they meet/cross in the middle.
# CONCEPTS  : Two-pointer technique, in-place swapping (no extra array
#             needed), tuple-swap syntax `a, b = b, a`.
# COMPLEXITY: Time O(n) - each element visited once.
#             Space O(1) - reversed in place, no extra array.

arr = [1, 2, 2, 3, 1, 4]

left = 0
right = len(arr) - 1

while left < right:
    arr[left], arr[right] = arr[right], arr[left]  # swap ends inward
    left += 1   # move left pointer closer to center
    right -= 1  # move right pointer closer to center

print("1. Reversed array:", arr)


# ====================================================================
# 2. PALINDROME CHECK
# ====================================================================
# PROBLEM   : Check whether an array reads the same forwards and
#             backwards.
# APPROACH  : Two Pointers again — compare arr[left] with arr[right].
#             If they ever differ, it's not a palindrome, so stop
#             early. If pointers meet without a mismatch, it is one.
# CONCEPTS  : Two-pointer technique, early exit / short-circuiting
#             (`break`) to avoid unnecessary work once the answer
#             is known.
# COMPLEXITY: Time O(n) worst case, but can exit earlier on mismatch.
#             Space O(1).

arr1 = [1, 2, 3, 2, 1, 4]
left = 0
right = len(arr1) - 1
palindrome = True

while left < right:
    if arr1[left] != arr1[right]:
        palindrome = False  # mismatch found, can't be a palindrome
        break                # no need to check further
    left += 1
    right -= 1

print("2. Is palindrome:", palindrome)


# ====================================================================
# 3. PUSH ZEROES TO THE RIGHT (MOVE NON-ZEROES TO THE FRONT)
# ====================================================================
# PROBLEM   : Rearrange the array so all non-zero elements come first
#             (keeping their order) and zeroes get pushed to the end.
# APPROACH  : Slow/Fast Pointer (also called "write pointer" pattern).
#             `j` tracks the position where the next non-zero value
#             should be written. `i` scans through the array; whenever
#             a non-zero value is found, it is swapped into position
#             `j`, and `j` advances.
# CONCEPTS  : Slow-fast (read/write) pointer pattern used heavily in
#             in-place array partitioning problems.
# COMPLEXITY: Time O(n). Space O(1).
# NOTE      : This had two bugs, both fixed below — it swapped with
#             `arr[i]` (a leftover name from problem 1) instead of
#             `arr2[i]`, and the loop started at index 1, which skips
#             a leading zero and breaks the order of the non-zero
#             elements. The loop must start at 0.

arr2 = [1, 0, 2, 0, 3]
j = 0

for i in range(len(arr2)):
    if arr2[i] != 0:
        arr2[i], arr2[j] = arr2[j], arr2[i]  # swap non-zero into place
        j += 1  # tracks where next non-zero should go

print("3. After pushing zeroes:", arr2)


# ====================================================================
# 4. REMOVE DUPLICATES FROM A SORTED ARRAY
# ====================================================================
# PROBLEM   : Given a SORTED array, remove duplicates in place so each
#             value appears only once.
# APPROACH  : Slow/Fast Pointer. `j` marks the last position of the
#             "unique so far" section. `i` scans ahead; when a value
#             different from arr[j] is found, `j` moves forward and
#             the new unique value is written there. Works only
#             because the array is sorted (duplicates are adjacent).
# CONCEPTS  : Slow-fast pointer, in-place compaction, relies on sorted
#             order to detect duplicates with a single pass.
# COMPLEXITY: Time O(n). Space O(1) (excluding the output slice).
# NOTE      : Loop starts at i = 1, not 0 — arr3[0] can never differ                     
#             from arr3[j] while j is still 0, so comparing index 0
#             to itself is skipped as unnecessary work. 


arr3 = [1, 1, 2, 2, 3, 3, 3, 4, 4]
j = 0

for i in range(1, len(arr3)):
    if arr3[i] != arr3[j]:   # found a new, unseen value
        j += 1                # advance the "unique so far" boundary
        arr3[j] = arr3[i]     # write the new value there

print("4. Array without duplicates:", arr3[:j + 1])


# ====================================================================
# 5. FREQUENCY COUNT USING A DICTIONARY
# ====================================================================
# PROBLEM   : Count how many times each element appears in the array.
# APPROACH  : Hashing. Use a dict as a hash map — for each element,
#             increment its counter if seen before, otherwise
#             initialize it to 1.
# CONCEPTS  : Hash maps for O(1) average lookup/insert, the classic
#             "get-or-default and increment" pattern.
# COMPLEXITY: Time O(n). Space O(k) where k = number of distinct
#             elements.

arr4 = [1, 1, 2, 2, 3, 3, 3, 4, 4]
freq = {}

for num in arr4:
    if num in freq:
        freq[num] += 1  # already seen, bump the counter
    else:
        freq[num] = 1    # first time seeing this value

print("5. Frequency:", freq)


# ====================================================================
# 6. FIRST REPEATING ELEMENT (DICTIONARY APPROACH)
# ====================================================================
# PROBLEM   : Find the first element (by position) that occurs more
#             than once in the array.
# APPROACH  : Two-pass hashing. Pass 1 builds a frequency map of every
#             element. Pass 2 walks the array in order and returns the
#             first element whose frequency > 1.
# CONCEPTS  : Hash maps, separating "counting" from "searching" into
#             two clear passes.
# COMPLEXITY: Time O(n) (two linear passes). Space O(n).

arr6 = [1, 2, 3, 2, 5]
freq2 = {}

for num in arr6:
    freq2[num] = freq2.get(num, 0) + 1  # build counts, pass 1

first_repeating = None
for num in arr6:
    if freq2[num] > 1:      # this value occurred more than once
        first_repeating = num
        break                 # first one in array order wins

print("6. First repeating element:", first_repeating)


# ====================================================================
# 7. FIRST REPEATING ELEMENT (SET APPROACH — SINGLE PASS)
# ====================================================================
# PROBLEM   : Same as above, but more efficiently — find the first
#             element that repeats, in one pass.
# APPROACH  : Hashing with a Set. Walk through the array once, adding
#             each element to a `seen` set. The moment an element is
#             already in the set, that's the first repeat.
# CONCEPTS  : Hash sets for O(1) membership testing, single-pass
#             optimization vs. the two-pass dict version above.
# COMPLEXITY: Time O(n) single pass (better constant factor than #6).
#             Space O(n).

arrA = [1, 2, 3, 2, 5]
seen = set()
first_repeating_set = None

for num in arrA:
    if num in seen:          # already encountered this value before
        first_repeating_set = num
        break
    seen.add(num)              # remember this value for future checks

print("7. First repeating element (set method):", first_repeating_set)


# ====================================================================
# 8. FIRST NON-REPEATING ELEMENT
# ====================================================================
# PROBLEM   : Find the first element that appears exactly once.
# APPROACH  : Two-pass hashing, same pattern as #6 but checking for
#             frequency == 1 instead of > 1.
# CONCEPTS  : Hash maps, count-then-scan pattern.
# COMPLEXITY: Time O(n). Space O(n).

arr5 = [1, 1, 2, 2, 3, 3, 3, 4]
freq1 = {}

for num in arr5:
    freq1[num] = freq1.get(num, 0) + 1  # build counts, pass 1

first_non_repeating = None
for num in arr5:
    if freq1[num] == 1:     # this value occurred exactly once
        first_non_repeating = num
        break

print("8. First non-repeating element:", first_non_repeating)


# ====================================================================
# 9. PAIR WITH GIVEN SUM (HASHING APPROACH)
# ====================================================================
# PROBLEM   : Find two numbers in the array that add up to a target
#             value (works on unsorted arrays too).
# APPROACH  : Hashing. For each number, compute its "complement"
#             (target - number). If the complement was already seen,
#             we've found our pair. Otherwise, remember the current
#             number and keep going.
# CONCEPTS  : Hash sets, the "complement lookup" pattern — trading
#             space for a single linear pass instead of nested loops
#             (which would be O(n^2)).
# COMPLEXITY: Time O(n). Space O(n).

arr7 = [2, 7, 11, 15]
target = 18
seen = set()

for num in arr7:
    complement = target - num    # value needed to complete the pair
    if complement in seen:         # was that value seen earlier?
        print("9. Pair found (hashing):", (complement, num))
        break
    seen.add(num)                    # remember current value for later


# ====================================================================
# 10. PAIR WITH GIVEN SUM (TWO POINTERS — REQUIRES SORTED ARRAY)
# ====================================================================
# PROBLEM   : Same as above, but using O(1) extra space by exploiting
#             sorted order.
# APPROACH  : Two Pointers. `left` starts at the beginning, `right` at
#             the end. If the current sum is too small, move `left`
#             right (increase sum). If too large, move `right` left
#             (decrease sum). If equal, we found the pair.
# CONCEPTS  : Two-pointer technique on sorted arrays — a classic
#             space-saving alternative to hashing when the array is
#             already sorted.
# COMPLEXITY: Time O(n). Space O(1).

left = 0
right = len(arr7) - 1
found = False

while left < right:
    current_sum = arr7[left] + arr7[right]
    if current_sum == target:
        print("10. Pair found (two pointers):", (arr7[left], arr7[right]))
        found = True
        break
    elif current_sum < target:
        left += 1    # sum too small, need a bigger left value
    else:
        right -= 1     # sum too large, need a smaller right value

if not found:
    print("10. No pair found")


# ====================================================================
# 11. MERGE TWO SORTED ARRAYS
# ====================================================================
# PROBLEM   : Merge two already-sorted arrays into one sorted array.
# APPROACH  : Two Pointers (merge step of Merge Sort). Walk both
#             arrays simultaneously with pointers i and j, always
#             appending the smaller of the two current elements to
#             the result. Once one array is exhausted, dump the
#             remaining tail of the other array as-is (it's already
#             sorted and all its remaining elements are >= everything
#             merged so far).
# CONCEPTS  : Two-pointer merging, the core building block of Merge
#             Sort's combine step.
# COMPLEXITY: Time O(n + m). Space O(n + m) for the merged output.

arr8 = [1, 3, 5]
arr9 = [2, 4, 6]
i = 0
j = 0
merged = []

while i < len(arr8) and j < len(arr9):
    if arr8[i] < arr9[j]:
        merged.append(arr8[i])  # smaller element goes in next
        i += 1
    else:
        merged.append(arr9[j])
        j += 1

while i < len(arr8):             # drain any leftovers from arr8
    merged.append(arr8[i])
    i += 1

while j < len(arr9):             # drain any leftovers from arr9
    merged.append(arr9[j])
    j += 1

print("11. Merged array:", merged)


# ====================================================================
# 12. COUNT DISTINCT ELEMENTS
# ====================================================================
# PROBLEM   : Count how many unique values exist in the array.
# APPROACH  : Hashing via a Set. A set automatically discards
#             duplicates, so converting the array to a set and taking
#             its length gives the count of distinct elements.
# CONCEPTS  : Hash sets, using built-in data structure properties to
#             avoid manual duplicate-tracking logic.
# COMPLEXITY: Time O(n). Space O(n) worst case (all unique).

l1 = [1, 2, 2, 3, 1, 4]
distinct = set(l1)   # duplicates collapse automatically
count = len(distinct)

print("12. Distinct element count:", count)


# ====================================================================
# 13. MAJORITY ELEMENT (APPEARS MORE THAN N/2 TIMES)
# ====================================================================
# PROBLEM   : Find the element that occurs more than n/2 times in the
#             array (the "majority element"), if one exists.
# APPROACH  : Hashing (Boyer-Moore Voting Algorithm would be the O(1)
#             space alternative, but here a frequency map is used).
#             Build a frequency map in one pass, then scan the array
#             again and return the first element whose count exceeds
#             n // 2.
# CONCEPTS  : Hash maps for counting, majority-element definition
#             (count > n/2, not just "most frequent").
# COMPLEXITY: Time O(n). Space O(n).
#             (Boyer-Moore Voting achieves the same result in O(1)
#             space if extra memory is not allowed.)

l2 = [2, 2, 1, 2, 3, 2, 2]
n = len(l2) // 2   # threshold: need more occurrences than this
freq3 = {}

for num in l2:
    freq3[num] = freq3.get(num, 0) + 1  # count each value

majority = None
for num in l2:
    if freq3[num] > n:    # occurs more than n/2 times
        majority = num
        break

print("13. Majority element:", majority)
