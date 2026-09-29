

def linear_search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
 
    return -1   # not found
 
# Time O(n) · Space O(1) — works on sorted AND unsorted arrays

def binary_search(nums, target):
    left = 0
    right = len(nums) - 1 # [] -> right = -1, loop never runs

    while left <= right : # <= because a single element is still worth checking

        mid = (left + right) // 2

        if nums[mid] == target: 
            return mid

        if nums[mid] < target:
            left = mid + 1 # mid is too small, throw away the left half (and mid)

        else:
            right = mid - 1 # mid is too big, throw away the right half (and mid)

    return -1  # left crossed right -> search space empty -> not found
 
# Time O(log n) · Space O(1) — array MUST be sorted



def first_occurrence(nums, target):
    left = 0
    right = len(nums) - 1
    answer = -1    # stays -1 if target never appears

    while left <= right :

        mid = (left + right) //2 

        if nums[mid] == target:
            answer = mid   # this MIGHT be the first one -> write it down
            right = mid - 1  # but keep looking LEFT for an earlier copy


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

        if nums[mid] == target :
            answer = mid   # this MIGHT be the last one -> write it down
            left = mid + 1  # but keep looking RIGHT for a later copy

        elif nums[mid] < target:
            left = mid + 1  

        else:
            right = mid - 1 

    return answer 

# Why not find any 4 and then walk left one step at a time?

# It's tempting: find a 4 with normal binary search, then while i > 0 and nums[i-1] == target: i -= 1. It gives the right answer, but if the array is a million 4s, that walk takes a million steps, which is O(n). The version above keeps halving even after it finds a match, so it's always about 20 steps for a million elements. That's O(log n).


def search_range(nums,target):

    first = first_occurrence(nums,target)

    if first == -1: # target not in array -> no need for a second search
        return [-1, -1]
        return [-1,-1]

    last = last_occurrence(nums,target)

    return [first,last]

# Time O(log n) (two binary searches = 2 log n -> O(log n)) · Space O(1)

def count_occurances(nums,target):

    first = first_occurrence(nums,target)

    if first == -1: ## without this, -1 - (-1) + 1 = 1  (wrong!)
        return 0

    last = last_occurrence(nums,target)

    return last - first + 1  # +1 because both ends are counted (2..4 is 3 items)
# Time O(log n) · Space O(1)

def lower_bound(nums, target):
    #where does this value belong in the sorted array?
    #Walking from left to right, where is the first element that is at least the target?
     # first index where nums[i] >= target
    left = 0
    right = len(nums) - 1
    answer = len(nums) # nothing is >= target -> "after the last element"


    while left <= right :

        mid = (left + right) // 2
        #two cases now, not three, because == is part of >=.
        if nums[mid] >= target:
            answer = mid  # mid qualifies -> save it
            right = mid -1   # look LEFT for an earlier index that also qualifies

        else:
            left = mid + 1 # mid (and everything left of it) is too small

    return answer 

       # Time O(log n) · Space O(1) 

def search_insert(nums, target):
    return lower_bound(nums, target)

# Time O(log n) · Space O(1)


def upper_bound(nums,target):
#Where is the first element that comes after all the copies of the target?
 # first index where nums[i] > target   (strictly greater)
    left = 0
    right = len(nums) -1 
    answer = len(nums)

    while left <= right:

        mid = (left + right) // 2

        if nums[mid] > target:
            answer = mid # mid qualifies -> save it
            right = mid - 1 # look LEFT for an earlier index that also qualifies

        else:
            left = mid + 1

    return answer 

def binary_search_recursive(nums, target, left , right):

    # BASE CASE: search space is empty -> target not here
    if left > right:
        return - 1
    
    mid =( left + right ) // 2

    if nums[mid] == target :
        return mid # found -> stop

    elif nums[mid] < target : # search right half
        return binary_search_recursive(nums,target , mid + 1, right)

    else: # search left half
        return binary_search_recursive(nums, target , left , mid - 1)

# Time O(log n) · Space O(log n)  <- each call waits on the call stack
# First call: binary_search_recursive(nums, target, 0, len(nums) - 1)
arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
binary_search_recursive(arr, 23, 0, len(arr) - 1)


