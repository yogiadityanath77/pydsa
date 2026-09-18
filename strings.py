# p ="python"

# for i in range(len(p)):
#     print(p[i])

# freq = 0
# s = "banana"
# target = "a"
# for i in range(len(s)):
#     if target == s[i]:
#         freq += 1

# print("target count :", freq)

# for i in range(len(s)-1,-1,-1):

#     print(s[i], end= "")

# st = "madam"
# palindrome = True
# left = 0
# right = len(st)-1

# while left<right:
#     if st[left] != st[right]:
#         palindrome = False
#         break

#     left += 1
#     right -= 1

# print (" string is : ", palindrome)

# freq = {}

# for ch in s:
#     if ch in freq:
#         freq[ch] += 1
#     else:
#         freq[ch] = 1

# max = 0
# result = ""

# for ch in freq:
#     if freq[ch]> max:
#         max = freq[ch]
#         result = ch


# seen = set()

# for ch in s:
#     if ch in seen:
#         print(ch)

#     seen.add(ch)


def is_anagram(s, t):
    if len(s) != len(t):
        return False

    freq = {}

    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    for ch in t:
        if ch in freq:
            freq[ch] -= 1
        else:
            return False

    for ch in freq:
        if freq[ch] != 0:
            return False

    return True

def is_anagram_using_Frequency_array(s, t):
    if len(s) != len(t):
        return False

    freq = [0] * 26

    for ch in s:
        index = ord(ch) - ord('a')
        freq[index] += 1

    for ch in t:
        index = ord(ch) - ord('a')
        freq[index] -= 1

    for count in freq:
        if count != 0:
            return False

    return True

def is_palindrome(s):
    left = 0
    right = len(s)-1

    while left<right:
        if s[left] != s[right]:
            return False

        left += 1
        right -= 1

    return True

def reverse_using_list(s):

    s_list = list(s)

    left = 0 
    right = len(s) -1

    while left<right:

        s_list[left],s_list[right] = s_list[right],s_list[left]

        left += 1
        right -= 1

    return "".join(s_list)

def is_valid_palindrome(s):

    left = 0
    right = len(s)-1

    while left < right:

        while left < right and not s[left].isalnum():
            left += 1

        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True

def reverse_vowels(s):

    left = 0
    right = len(s)-1

    vowels = "aeiouAEIOU"
    chars = list(s)

    while left< right:

         # Move left until we find a vowel
        while left < right and chars[left] not in vowels:
            left += 1

         # Move right until we find a vowel
        while left < right and chars[right] not in vowels:
            right -= 1

        if left < right:
            chars[left], chars[right] = chars[right], chars[left]

            left += 1
            right -= 1

    return "".join(chars)

# sliding window

def max_sum_arrays(nums,k):

    window_sum = 0

    #build first window

    for i in range(k):
        window_sum += nums[i]

    max_sum = window_sum

    #slide window 

    for i in range(k,len(nums)):
        window_sum += nums[i]
        window_sum -= nums[i-k]

        max_sum = max(max_sum,window_sum)

    return max_sum

def max_vowels(s,k):

    vowels = 'aeiou'

    count = 0

    # first window

    for i in range(k):

        if s[i] in vowels:
            count += 1

    max_count = count

    #slide window

    for i in range(k,len(s)):

        # add incoming character 
        if s[i] in vowels:
            count += 1

        # Remove outgoing character

        if s[i-k] in vowels:
            count -=1

        max_count = max(max_count, count)

    return max_count

def longest_unique_substring(s):

    seen = set()
    left = 0
    max_length = 0

    for right in range(len(s)):

        while s[right] in seen: #Sometimes you need to remove multiple characters, so we use WHILE
            seen.remove(s[left]) #removes the oldest character in the window.
            left +=1 #moves the left boundary.

        seen.add(s[right]) #adds the new character.

        window_length = right - left + 1 # FORMULA
        max_length = max(max_length,window_length)

    return max_length      

def longest_at_most_k_distinct(s, k):

    freq = {}
    left = 0 
    max_length = 0

    for right in range(len(s)):

        if s[right] in freq:
            freq[s[right]] += 1
        else:
            freq [s[right]] = 1

        # If we have too many distinct characters,
        # shrink the window from the left

        while len(freq) > k:
            freq[s[left]] -= 1

            if freq[s[left]] == 0:
                del freq[s[left]]

            left += 1

        # Current window is valid
        window_length = right - left + 1
        max_length = max(max_length,window_length)

    return max_length










