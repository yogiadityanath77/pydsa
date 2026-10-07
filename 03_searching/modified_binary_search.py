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

def find_min2(nums):
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid           # keep mid: it might be the minimum
    return nums[left]

def find_peak_element(nums):

    left = 0
    right = len(nums) - 1
    answer = len(nums) - 1 
    
    while left <= right :
        
        mid = (left + right) // 2

        if mid == len(nums) - 1 or nums[mid] > nums[mid + 1]:
 # going DOWN at mid (the last element always counts as going down)
            # -> a peak is at mid or to its left
            answer = mid   # mid could be the peak, save it
            right = mid - 1 # look LEFT

        else :
# going UP at mid -> keep climbing, a peak is to the right
            left = mid + 1

    return answer
# Time O(log n) · Space O(1)

def single_non_duplicate(nums):

    left = 0
    right = len(nums) - 1
    answer = len(nums) -1 

    while left <= right :

        mid = (left + right ) // 2

        if mid % 2 == 1:
            mid -= 1 # always stand on an EVEN index (start of a pair)

        if mid == len(nums) - 1 or nums[mid] != nums[mid + 1]:
# pair is broken here -> single element is at mid or to the left
            answer = mid
            right = mid - 1

        else:
            # nums[mid] == nums[mid + 1]: a healthy pair -> single is to the right
            left = mid + 2          # skip the whole pair (keeps left even)

    return nums[answer]

# LC 875 · Koko Eating Bananas · M
def hours_needed(piles, k):
    total = 0
    for pile in piles:
        total += pile // k          # full hours
        if pile % k != 0:
            total += 1              # leftover bananas need one more hour
    return total
# Time O(n)
def min_eating_speed_brute(piles, h):
    k = 1
    while hours_needed(piles, k) > h:   # try 1, 2, 3, ... until one works
        k += 1
    return k
# Time O(n * max(piles))
def min_eating_speed(piles, h):

    left = 1                        # slowest possible speed
    right = max(piles)              # fast enough: every pile takes 1 hour
    answer = right

    while left <= right:

        mid = (left + right) // 2   # a candidate SPEED, not an index

        if hours_needed(piles, mid) <= h:
            answer = mid            # speed mid works -> save it
            right = mid - 1         # try SLOWER
        else:
            left = mid + 1          # too slow -> must go faster

    return answer

# Time O(n log m), m = max(piles) · Space O(1)

# LC 1011 · Capacity To Ship Packages Within D Days · M
def days_needed(weights, capacity):
    # load packages IN ORDER; when the next one doesn't fit, start a new day
    days = 1
    load = 0
    for w in weights:
        if load + w > capacity:
            days += 1               # ship is full -> next day
            load = 0
        load += w
    return days
 
# Time O(n)  (assumes capacity >= max(weights), which the range guarantees)

def ship_within_days_brute(weights, days):
    capacity = max(weights)
    while days_needed(weights, capacity) > days:
        capacity += 1
    return capacity
 
# Time O(n * (sum - max))

def ship_within_days(weights, days):
 
    left = max(weights)             # smallest possible: the heaviest package must fit
    right = sum(weights)            # always works: everything in one day
    answer = right
 
    while left <= right:
 
        mid = (left + right) // 2   # a candidate CAPACITY
 
        if days_needed(weights, mid) <= days:
            answer = mid            # works -> save it
            right = mid - 1         # try a SMALLER ship
        else:
            left = mid + 1          # too small -> need a bigger ship
 
    return answer
 
# Time O(n log(sum)) · Space O(1)