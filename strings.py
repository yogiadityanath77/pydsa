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









