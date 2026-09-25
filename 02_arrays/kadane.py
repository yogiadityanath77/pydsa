def max_subarray_brute(nums):
    best = float('-inf')

    for start in range(len(nums)):
        total = 0

        for end in range(start,len(nums)):
            total += nums[end]
            best = max(best,total)

    return best

def max_subarray(nums):

    current = float('-inf')
    best = float('-inf')

    for i in range(len(nums)):
        current = max(nums[i], current + nums[i]) #biggest ending here = max( new number alone,  previous biggest + new number )
        best = max (current,best) # is it the best winner so far?

    return best

def max_subarray_with_indices(nums):

    current = float('-inf')
    best = float('-inf')
    current_start=0
    best_start = 0
    best_end = 0

    for i in range(len(nums)):

        if nums[i] > nums[i] + current :
            current = nums[i]
            current_start = i

        else:
            current = current + nums[i]

        if current > best:

            best = current

            best_start = current_start
            best_end = i

    return best,best_start , best_end

def max_product(nums):

    cur_max = nums[0]
    cur_min = nums[0]
    best = nums[0]

    for i in range(1,len(nums)):

        num = nums[i]

        a = cur_max * num
        b = cur_min * num

        cur_max = max(num,a,b)
        cur_min = min(num,a,b)

        best = max(best,cur_max)

    return best




    
print(max_subarray_brute([2, -3, 4, -1, 2]))                 # 5
print(max_subarray_brute([-3, -1, -2]))                      # -1
print(max_subarray_brute([-2, 1, -3, 4, -1, 2, 1, -5, 4]))   # 6  (LeetCode example)