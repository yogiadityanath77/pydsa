
def build_prefix(nums):
    prefix = [0]

    for num in nums:
        prefix.append(prefix[-1] + num)

    return prefix

def range_sum(prefix,left,right):

    return prefix[right+1] - prefix[left]

def pivot_index(nums):
    total = sum(nums)
    left = 0

    for i in range(len(nums)):
        right = total - left - nums[i]
        if left == right:
            return i

        left += nums[i]

    return -1



class NumArray:
    def __init__(self, nums):
        self.prefix = [0]
        #It's stored on self so it survives after __init__ finishes. Without self., it would be a local variable and would disappear, and sumRange couldn't see it.
        for num in nums:
            self.prefix.append(self.prefix[-1] + num)

    def sumRange(self, left, right):
        return self.prefix[right + 1] - self.prefix[left]

def subarray_sum_brute(nums, k):
    count = 0

    for start in range(len(nums)):
        total = 0                              # new start → reset total

        for end in range(start, len(nums)):
            total += nums[end]                 # extend the subarray by one number
            if total == k:
                count += 1                     # found one

    return count
#Any subarray sum = one running total minus another
def subarray_sum(nums,k):
    #every subarray sum is the difference between two running totals.
#So at each step you ask one question: "how many times have I already seen the value current - k?" Every time you've seen it, that's one subarray ending right here with sum k.
    count =0 
    current = 0
    seen = {0: 1} #running total → how many times I've passed it.

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

def subarray_sum_list(nums, k):
    count = 0
    current = 0
    passed = [0]                      # running total 0, before we start

    for num in nums:
        current += num                # 1. new running total
        need = current - k            # 2. the earlier total we want
        count += passed.count(need)   # 3. look first: how many times did we pass it?
        passed.append(current)        # 4. then write ourselves in

    return count

def find_max_length(nums):
    first_seen = {0: -1}      # total 0 "appears" before the list starts
    total = 0
    best = 0

    for i, num in enumerate(nums):
        if num == 0:
            total -= 1        # treat 0 as −1
        else:
            total += 1

        if total in first_seen:
            best = max(best, i - first_seen[total])   # same total again → balanced
        else:
            first_seen[total] = i                     # first time → remember where

    return best

def subarrays_div_by_k(nums, k):
    count = 0
    total = 0
    seen = {0: 1}

    for num in nums:
        total += num
        rem = total % k

        if rem in seen:
            count += seen[rem]

        if rem in seen:
            seen[rem] += 1
        else:
            seen[rem] = 1

    return count


def main():
    nums = [4, -2, 3]
    prefix = build_prefix(nums)
    print(prefix)                   
    print(range_sum(prefix, 1, 1)) 
    print(range_sum(prefix, 0, 1))  


if __name__ == "__main__":
    main()