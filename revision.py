# ============================================================
# REVISION FILE — starting from the ground up
# ============================================================
# Rules:
# - Do NOT look at your old files while solving.
# - Write your solution inside each function, replacing `pass`.
# - Test with the main() calls at the bottom.
# - Once a batch of 5 is done, tell Claude to check it, then we add
#   the next 5.
#
# Order of revision (ground up):
#   Batch 1-3: Python basics (lists, tuples/sets, dicts)
#   Batch 4-5: Arrays (fundamentals, two-pointer patterns)
#   Batch 6:   Searching (linear, binary + variants)
#   Batch 7:   Sorting (bubble, selection, insertion)
#   Batch 8+:  Mixed review (hashmap/set patterns, everything combined)
# ============================================================


# ---------------- BATCH 1: Python basics — LISTS ----------------

# Q1. Given a list of numbers, return their sum and average as a tuple
# (sum, average).
# numbers = [1, 2, 9, 2, 5] -> expected (19, 3.8)
def sum_and_average(numbers):
    total = 0
    for num in numbers:
        total += num

    avg = total / len(numbers) 

    return (total, avg)


# Q2. Given a list of numbers, return the largest number in it.
# (Do it manually with a loop, don't use max().)
# numbers = [1, 2, 9, 2, 5] -> expected 9
def find_largest(numbers):

    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num

    return largest



# Q3. Given a list, count how many times a given value appears in it.
# numbers = [1, 2, 2, 3, 2, 5], value = 2 -> expected 3
def count_occurrences(numbers, value):

    count = 0
    for num in numbers:
        if num == value:
            count += 1

    return count
    


# Q4. Given a list with possible duplicates, return a new list with only
# the unique values, preserving order of first appearance.
# nums = [1, 2, 2, 3, 4, 4] -> expected [1, 2, 3, 4]
def unique_values(nums):
    unique = []
    for num in nums:
        if num not in unique:
            unique.append(num)
    return unique
    


# Q5. Given a list, reverse it manually (without using .reverse() or
# slicing like list[::-1]).
# items = [1, 2, 3, 4, 5] -> expected [5, 4, 3, 2, 1]
def reverse_list(items):

    left = 0
    right = len(items) - 1

    while left < right:
        items[left], items[right] = items[right], items[left]
        left += 1
        right -= 1
    return items


# ---------------- BATCH 2: Python basics — TUPLES & SETS ----------------

# Q1. Given a tuple, return a new tuple with the first and last elements
# swapped. (Tuples are immutable, so build a new one.)
# t = (1, 2, 3, 4) -> expected (4, 2, 3, 1)
def swap_first_last(t):

    if len(t) < 2:
        return t  # No swap needed for tuples with 0 or 1 element

    # Convert to list to swap, then back to tuple
    t_list = list(t)
    t_list[0], t_list[-1] = t_list[-1], t_list[0]
    return tuple(t_list)


# Q2. Given a tuple of numbers, return the sum of all elements using
# tuple unpacking with a loop (no sum()).
# t = (10, 20, 30) -> expected 60
def sum_tuple(t):

    total = 0
    for num in t:
        total += num
    return total


# Q3. Given two sets, return their intersection (common elements)
# without using the built-in `&` operator or `.intersection()`.
# a = {1, 2, 3, 4}, b = {3, 4, 5, 6} -> expected {3, 4}
def set_intersection(a, b):
    intersection = set()
    for elem in a:
        if elem in b:
            intersection.add(elem)
    return intersection


# Q4. Given a list with duplicates, use a set to check: does the list
# contain any duplicate at all? Return True/False.
# nums = [1, 2, 3, 2] -> expected True
# nums = [1, 2, 3, 4] -> expected False
def has_duplicates(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


# Q5. Given a list of numbers, convert it to a tuple, then return
# how many times a given value appears in that tuple using .count().
# nums = [1, 2, 2, 3, 2], value = 2 -> expected 3
def count_in_tuple(nums, value):
    t = tuple(nums)
    return t.count(value)


# ---------------- BATCH 3: Python basics — DICTS ----------------

# Q1. Given a list of words, build a frequency dict mapping each word to
# how many times it appears.
# words = ["a", "b", "a", "c", "b", "a"] -> expected {"a": 3, "b": 2, "c": 1}
def word_frequency(words):
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq
    


# Q2. Given a dict, return the key with the highest value.
# (Do it manually with a loop, don't use max() with a key function.)
# d = {"a": 3, "b": 7, "c": 5} -> expected "b"
def key_with_max_value(d):
    max_key = None
    max_value = float('-inf')  # Start with the smallest possible value

    for key, value in d.items():
        if value > max_value:
            max_value = value
            max_key = key
    return max_key


# Q3. Given two dicts, merge them into a new dict. If a key exists in
# both, sum their values.
# a = {"x": 1, "y": 2}, b = {"y": 3, "z": 4} -> expected {"x": 1, "y": 5, "z": 4}
def merge_and_sum(a, b):
    merged = a.copy()  # Start with all items from a
    for key, value in b.items():
        if key in merged:
            merged[key] += value  # Sum values if key exists
        else:
            merged[key] = value  # Add new key-value pair
    return merged
    


# Q4. Given a dict, return a new dict with keys and values swapped.
# d = {"a": 1, "b": 2} -> expected {1: "a", 2: "b"}
def invert_dict(d):
    inverted = {}
    for key, value in d.items():
        inverted[value] = key
    return inverted
    


# Q5. Given a list of numbers, use a dict to find and return the first
# number that repeats (same idea as before, but built with dict.get()).
# nums = [4, 5, 6, 5, 4] -> expected 5
def first_repeating_dict(nums):
    freq = {}
    for num in nums:
        if freq.get(num, 0) > 0:
            return num
        freq[num] = 1


def main():
    print(sum_and_average([1, 2, 9, 2, 5]))
    print(find_largest([1, 2, 9, 2, 5]))
    print(count_occurrences([1, 2, 2, 3, 2, 5], 2))
    print(unique_values([1, 2, 2, 3, 4, 4]))
    print(reverse_list([1, 2, 3, 4, 5]))

    print(swap_first_last((1, 2, 3, 4)))
    print(sum_tuple((10, 20, 30)))
    print(set_intersection({1, 2, 3, 4}, {3, 4, 5, 6}))
    print(has_duplicates([1, 2, 3, 2]))
    print(count_in_tuple([1, 2, 2, 3, 2], 2))

    print(word_frequency(["a", "b", "a", "c", "b", "a"]))
    print(key_with_max_value({"a": 3, "b": 7, "c": 5}))
    print(merge_and_sum({"x": 1, "y": 2}, {"y": 3, "z": 4}))
    print(invert_dict({"a": 1, "b": 2}))
    print(first_repeating_dict([4, 5, 6, 5, 4]))


if __name__ == "__main__":
    main()
