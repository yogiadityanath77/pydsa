# Arrays — Level 4 patterns
# Order: sliding window (fixed, variable) -> prefix sum -> Kadane -> stock
# Same order as Level 4 in Basics_Arrays_Search_Sort_Checklist.md.
# Replace each `pass` with your solution, then run this file.
# Every test prints PASS or FAIL.
# Write the time and space complexity as a comment above each function.


# sliding window — fixed size

def max_sum_k(nums, k):
    # (E) Largest sum of any k consecutive elements.
    # max_sum_k([2,1,5,1,3,2], 3) -> 9   ([5,1,3])
    pass


def find_max_average(nums, k):
    # LeetCode 643 (E). Largest average of any k consecutive elements.
    # find_max_average([1,12,-5,-6,50,3], 4) -> 12.75
    pass


def max_score_cards(card_points, k):
    # LeetCode 1423 (M). Take exactly k cards, each from the start or the end.
    # Return the largest possible total.
    # max_score_cards([1,2,3,4,5,6,1], 3) -> 12   (take 1, 6, 5 from the end)
    pass


# sliding window — variable size

def min_subarray_len(target, nums):
    # LeetCode 209 (M). Length of the smallest subarray whose sum is >= target.
    # Return 0 if no such subarray exists. All nums are positive.
    # min_subarray_len(7, [2,3,1,2,4,3]) -> 2   ([4,3])
    pass


def longest_subarray_sum_k_positive(nums, k):
    # (M) Length of the longest subarray whose sum is exactly k.
    # All nums are POSITIVE. Return 0 if none.
    # longest_subarray_sum_k_positive([2,3,5,1,9], 10) -> 3   ([2,3,5])
    pass


def longest_ones_flip_k(nums, k):
    # LeetCode 1004 (M). Longest run of 1s if you may flip at most k zeroes.
    # longest_ones_flip_k([1,1,1,0,0,0,1,1,1,1,0], 2) -> 6
    pass


def total_fruit(fruits):
    # LeetCode 904 (M). Two baskets, each holds one type of fruit. Walk right from
    # any start, picking one fruit per tree. Return the most fruit you can pick.
    # (= longest subarray with at most 2 distinct values)
    # total_fruit([1,2,3,2,2]) -> 4
    pass


def num_subarrays_with_sum(nums, goal):
    # LeetCode 930 (M). Binary array. Count subarrays whose sum is exactly goal.
    # num_subarrays_with_sum([1,0,1,0,1], 2) -> 4
    pass


# prefix sum

def build_prefix_sum(nums):
    # LeetCode 303 (E). Return a prefix array of length len(nums) + 1 with prefix[0] = 0,
    # so prefix[i] is the sum of nums[0 .. i-1].
    # build_prefix_sum([2,4,1,3,5]) -> [0,2,6,7,10,15]
    pass


def range_sum(prefix, left, right):
    # Sum of nums[left .. right] (inclusive) in O(1), using the prefix array.
    # prefix = build_prefix_sum([2,4,1,3,5]); range_sum(prefix, 1, 3) -> 8
    pass


def pivot_index(nums):
    # LeetCode 724 (E). Leftmost index where sum of elements to the left equals
    # sum of elements to the right. Return -1 if none.
    # pivot_index([1,7,3,6,5,6]) -> 3
    pass


def subarray_sum_equals_k(nums, k):
    # LeetCode 560 (M). Count subarrays whose sum is exactly k.
    # nums can contain negatives, so sliding window does NOT work here.
    # subarray_sum_equals_k([1,1,1], 2) -> 2
    pass


def longest_subarray_sum_k(nums, k):
    # (M) Length of the longest subarray whose sum is exactly k.
    # nums CAN contain negatives and zeros. Return 0 if none.
    # longest_subarray_sum_k([1,-1,5,-2,3], 3) -> 4   ([1,-1,5,-2])
    pass


def product_except_self(nums):
    # LeetCode 238 (M). answer[i] = product of every element except nums[i].
    # No division, O(n) time.
    # product_except_self([1,2,3,4]) -> [24,12,8,6]
    pass


# kadane

def max_subarray_sum(nums):
    # LeetCode 53 (M). Largest sum of any non-empty contiguous subarray.
    # max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]) -> 6   ([4,-1,2,1])
    pass


def max_subarray_with_indices(nums):
    # (M) Same as above, but return (best_sum, start_index, end_index).
    # max_subarray_with_indices([-2,1,-3,4,-1,2,1,-5,4]) -> (6, 3, 6)
    pass


def max_product_subarray(nums):
    # LeetCode 152 (M). Largest product of any non-empty contiguous subarray.
    # max_product_subarray([2,3,-2,4]) -> 6
    pass


# stock

def max_profit_one_transaction(prices):
    # LeetCode 121 (E). Buy once, sell once later. Return the best profit, or 0.
    # max_profit_one_transaction([7,1,5,3,6,4]) -> 5
    pass


def max_profit_many_transactions(prices):
    # LeetCode 122 (M). Buy and sell as many times as you like
    # (hold at most one share at a time). Return the best total profit.
    # max_profit_many_transactions([7,1,5,3,6,4]) -> 7
    pass


# tests

def check(name, got, expected):
    status = "PASS" if got == expected else "FAIL"
    print(f"{status}  {name}: got {got}, expected {expected}")


def main():
    print("=== Sliding Window — Fixed Size ===")
    check("max_sum_k", max_sum_k([2,1,5,1,3,2], 3), 9)
    check("max_sum_k", max_sum_k([1,2,3,4,5], 2), 9)
    check("find_max_average", find_max_average([1,12,-5,-6,50,3], 4), 12.75)
    check("find_max_average (single)", find_max_average([5], 1), 5.0)
    check("max_score_cards", max_score_cards([1,2,3,4,5,6,1], 3), 12)
    check("max_score_cards", max_score_cards([2,2,2], 2), 4)
    check("max_score_cards (take all)", max_score_cards([9,7,7,9,7,7,9], 7), 55)

    print("\n=== Sliding Window — Variable Size ===")
    check("min_subarray_len", min_subarray_len(7, [2,3,1,2,4,3]), 2)
    check("min_subarray_len", min_subarray_len(4, [1,4,4]), 1)
    check("min_subarray_len (none)", min_subarray_len(11, [1,1,1,1,1,1,1,1]), 0)
    check("longest_subarray_sum_k_positive", longest_subarray_sum_k_positive([2,3,5,1,9], 10), 3)
    check("longest_subarray_sum_k_positive", longest_subarray_sum_k_positive([1,2,3,1,1,1,1,4,2,3], 3), 3)
    check("longest_subarray_sum_k_positive (none)", longest_subarray_sum_k_positive([1,2,3], 10), 0)
    check("longest_ones_flip_k", longest_ones_flip_k([1,1,1,0,0,0,1,1,1,1,0], 2), 6)
    check("longest_ones_flip_k", longest_ones_flip_k([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3), 10)
    check("total_fruit", total_fruit([1,2,1]), 3)
    check("total_fruit", total_fruit([0,1,2,2]), 3)
    check("total_fruit", total_fruit([1,2,3,2,2]), 4)
    check("total_fruit", total_fruit([3,3,3,1,2,1,1,2,3,3,4]), 5)
    check("num_subarrays_with_sum", num_subarrays_with_sum([1,0,1,0,1], 2), 4)
    check("num_subarrays_with_sum (all zero)", num_subarrays_with_sum([0,0,0,0,0], 0), 15)

    print("\n=== Prefix Sum ===")
    check("build_prefix_sum", build_prefix_sum([2,4,1,3,5]), [0,2,6,7,10,15])
    prefix = [0,2,6,7,10,15]
    check("range_sum(1, 3)", range_sum(prefix, 1, 3), 8)
    check("range_sum(0, 4)", range_sum(prefix, 0, 4), 15)
    check("range_sum(2, 2)", range_sum(prefix, 2, 2), 1)
    check("pivot_index", pivot_index([1,7,3,6,5,6]), 3)
    check("pivot_index (none)", pivot_index([1,2,3]), -1)
    check("pivot_index (at 0)", pivot_index([2,1,-1]), 0)
    check("subarray_sum_equals_k", subarray_sum_equals_k([1,1,1], 2), 2)
    check("subarray_sum_equals_k", subarray_sum_equals_k([1,2,3], 3), 2)
    check("subarray_sum_equals_k (negatives)", subarray_sum_equals_k([1,-1,0], 0), 3)
    check("longest_subarray_sum_k", longest_subarray_sum_k([1,-1,5,-2,3], 3), 4)
    check("longest_subarray_sum_k", longest_subarray_sum_k([-2,-1,2,1], 1), 2)
    check("longest_subarray_sum_k (none)", longest_subarray_sum_k([1,2,3], 7), 0)
    check("product_except_self", product_except_self([1,2,3,4]), [24,12,8,6])
    check("product_except_self (zero)", product_except_self([-1,1,0,-3,3]), [0,0,9,0,0])

    print("\n=== Kadane ===")
    check("max_subarray_sum", max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]), 6)
    check("max_subarray_sum (all negative)", max_subarray_sum([-3,-1,-2]), -1)
    check("max_subarray_sum", max_subarray_sum([5,4,-1,7,8]), 23)
    check("max_subarray_with_indices", max_subarray_with_indices([-2,1,-3,4,-1,2,1,-5,4]), (6, 3, 6))
    check("max_product_subarray", max_product_subarray([2,3,-2,4]), 6)
    check("max_product_subarray (zero)", max_product_subarray([-2,0,-1]), 0)
    check("max_product_subarray (two negatives)", max_product_subarray([-2,3,-4]), 24)

    print("\n=== Stock ===")
    check("max_profit_one_transaction", max_profit_one_transaction([7,1,5,3,6,4]), 5)
    check("max_profit_one_transaction (falling)", max_profit_one_transaction([7,6,4,3,1]), 0)
    check("max_profit_many_transactions", max_profit_many_transactions([7,1,5,3,6,4]), 7)
    check("max_profit_many_transactions", max_profit_many_transactions([1,2,3,4,5]), 4)
    check("max_profit_many_transactions (falling)", max_profit_many_transactions([7,6,4,3,1]), 0)


if __name__ == "__main__":
    main()
