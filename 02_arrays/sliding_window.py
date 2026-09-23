# for right in range(len(nums)):

#     # add right element

#     while window_is_invalid:
#         # remove left element
#         left += 1

#     # current window is valid
#     # update answer



def max_sum_arrays(nums,k):
    window_sum = 0

    # build first window
    for i in range(k):
        window_sum += nums[i]

    max_sum = window_sum

    for i in range(k,len(nums)):

        window_sum += nums[i]
        window_sum -= nums[i-k]

        max_sum = max(max_sum,window_sum)

    return max_sum

def max_average(nums,k):
    window_sum = 0

    # build first window
    for i in range(k):
        window_sum += nums[i]

    max_sum = window_sum

    for i in range(k,len(nums)):

        window_sum += nums[i]
        window_sum -= nums[i-k]

        max_sum = max(max_sum,window_sum)

    return max_sum/k

def max_score(cards,k):

    n = len(cards)
# Number of cards we leave behind
    window_size = n-k

     # If we take all cards
    if window_size == 0:
        return sum(cards)

    window_sum = 0

    for i in range(window_size):
        window_sum += cards[i]

    min_sum = window_sum

    for i in range (window_size,n):
        window_sum += cards[i]
        window_sum -= cards[i - window_size]

        min_sum = min(min_sum,window_sum)

 # Maximum score = total - minimum window
    return sum(cards) - min_sum

def min_subarray_len(nums,target):

    left = 0
    window_sum = 0

    min_length = float('inf') #Python's floating-point infinity. It's larger than every real number

    for right in range(len(nums)):

        window_sum += nums[right]

        while window_sum >= target:

            current_length = right - left + 1

            min_length = min(min_length,current_length)

            window_sum -= nums[left]

            left += 1

    if min_length == float('inf') :
        return 0

    return min_length

def longest_subarray_sum_k(nums, k):

    left = 0
    window_sum = 0
    max_length = 0 

    for right in range(len(nums)):

        window_sum += nums[right]


        while window_sum > k :

            window_sum -= nums[left]

            left += 1

        if window_sum == k:
            current_length = right - left + 1
            max_length = max(current_length,max_length)

    return max_length

def longest_ones(nums, k):

    left = 0
    zero_count = 0
    max_length = 0

    for right in range(len(nums)):

        if nums[right] == 0 :
            zero_count += 1

        while zero_count > k:

            if nums[left] == 0:
                zero_count -= 1

            left += 1

        currrent_length = right - left + 1

        max_length = max(currrent_length,max_length)

    return max_length


def total_fruit(fruits):

    left = 0
    freq = {}

    max_length = 0

    for right in range(len(fruits)):

        if fruits[right] in freq:
            freq[fruits[right]] += 1
        else :
            freq[fruits[right]] = 1

        while len(freq) > 2:

            freq[fruits[left]] -= 1

            if freq[fruits[left]] == 0:
                del freq[fruits[left]]

            left += 1

        current_length = right - left + 1

        max_length = max(max_length,current_length)

    return max_length


def at_most(nums,k):

    if k<0:
        return 0

    left = 0
    count = 0
    window_sum = 0

    for right in range(len(nums)):

        window_sum += nums[right]

        while window_sum > k:

            window_sum -= nums[left]
            left += 1

        count += right - left + 1

    return count

def num_subarrays_with_sum(nums, goal):

    return at_most(nums,goal) - at_most(nums,goal-1)




