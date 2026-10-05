# Key fact: cut a rotated sorted array at mid -> at least ONE half is fully sorted.
def search_rotated(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right :

        mid = (left + right) // 2

        if nums[mid] == target :
            return mid
        # 1) Which half is sorted?
        if nums[left] <= nums[mid]:  # LEFT half nums[left..mid] is sorted
# LEFT half is sorted: its values go from nums[left] up to nums[mid]
            smallest = nums[left]
            biggest = nums[mid]

            if smallest <= target and target <= biggest:
                right = mid- 1 # target's value fits in the left half -> go left

            else:
                left = mid + 1 # doesn't fit -> can only be on the right

        else:
# RIGHT half is sorted: its values go from nums[mid] up to nums[right]
            smallest = nums[mid]
            biggest = nums[right]

            if smallest <= target and target <= biggest:
                left = mid + 1 # target's value fits in the right half -> go right
            else:
                right = mid -1  # doesn't fit -> can only be on the left

    return -1 


# nums        4  5  6  7  0  1  2        last = 2
# <= 2 ?      ✗  ✗  ✗  ✗  ✓  ✓  ✓
#                         ↑
#                     first ✓ = the minimum
def find_min(nums):

    last = nums[-1]
    left = 0 
    right = len(nums) - 1
    answer = len(nums) - 1 # the last element is always a ✓

    while left <= right :

        mid = ( left + right) // 2

        if nums[mid] <= last:
            answer =mid # mid is in ramp 2 -> could be its start, save it
            right = mid - 1 # look LEFT for an earlier ramp-2 element

        else :
            left = mid + 1 # mid is in ramp 1 -> minimum is to the right

    return nums[answer]

# Time O(log n) · Space O(1)