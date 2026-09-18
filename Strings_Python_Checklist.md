# Strings DSA Checklist — Python

**Current level:** Beginner → early pattern work  
**Progress:** String basics and the two-pointer set are done (anagram, palindrome,
valid palindrome, reverse vowels). Fixed-size sliding window is done and the
`max_vowels` bug is fixed. Variable-size sliding window has started (longest
unique substring, longest substring with at most k distinct chars). The big
gaps are **window + frequency map, substring/prefix problems, and string
building/parsing**.  
**Last updated:** 2026-09-18

Companion files: `Basics_Arrays_Search_Sort_Checklist.md`, `Linked_List_Python_Checklist.md`

---

## 🟢 Level 0 — Python Basics: Strings

- [x] Index and iterate a string by position (`s[i]`, `range(len(s))`)
- [x] Iterate characters directly (`for ch in s`)
- [x] Traverse a string backwards (`range(len(s)-1, -1, -1)`)
- [x] Count occurrences of a character with a manual loop
- [x] Build a character frequency map with a dict
- [x] Build a character frequency array with `ord(ch) - ord('a')`
- [x] Understand immutability — convert to `list`, mutate, `"".join()` back
- [x] `.isalnum()` and `.lower()` for filtering / normalising
- [ ] Slicing (`s[1:4]`, `s[::-1]`, `s[::2]`)
- [ ] `.split()` / `.join()` / `.strip()`
- [ ] `.find()` / `.index()` / `in` for substring search
- [ ] `.startswith()` / `.endswith()`
- [ ] `.replace()` and `.count()`
- [ ] f-strings and `str()` conversion
- [ ] `ord()` / `chr()` beyond the frequency-array idiom
- [ ] `collections.Counter` for character counts
- [ ] Why `s += ch` in a loop is O(n^2) — build a list and `join()` instead

---

## 🟢 Level 1 — Easy Classics

- [x] Reverse a string (two-pointer on a list)
- [x] Check whether a string is a palindrome
- [x] Valid palindrome — ignore non-alphanumerics, case-insensitive
- [x] Valid anagram (hash map)
- [x] Valid anagram (frequency array, 26 letters)
- [x] Most frequent character
- [x] First repeating character (set, single pass)
- [ ] First **non**-repeating character (return its index)
- [ ] Reverse the words in a sentence
- [ ] Reverse each word but keep the word order
- [ ] Count vowels and consonants
- [ ] Remove all duplicate characters, preserving order
- [ ] Check whether two strings are rotations of each other
- [ ] Isomorphic strings (two-way character mapping)
- [ ] Longest common prefix across a list of strings

## 🟡 Level 2 — Two-Pointer Patterns

- [x] Opposite-ends convergence (palindrome, reverse)
- [x] Skip characters that fail a predicate (valid palindrome)
- [x] Reverse only the vowels
- [ ] Is subsequence (`"abc"` inside `"ahbgdc"`)
- [ ] Backspace string compare (`"ab#c"` vs `"ad#c"`)
- [ ] Longest palindromic substring (expand around centre)
- [ ] Count palindromic substrings
- [ ] Valid palindrome II — allow deleting at most one character

## 🟡 Level 3 — Sliding Window

### Fixed size
- [x] Max sum of `k` consecutive elements (in `strings.py`, on a list)
- [x] Max vowels in any substring of length `k`
- [ ] Average of every window of size `k`
- [ ] Find all anagrams of a pattern in a string (fixed window + frequency compare)
- [ ] Permutation in string

### Variable size
- [x] Longest substring without repeating characters
- [x] Longest substring with at most `k` distinct characters
- [ ] Longest repeating character replacement
- [ ] Longest substring with exactly `k` distinct characters
- [ ] Smallest window containing all characters of another string (hard, later)

## 🟡 Level 4 — Hashing Patterns

- [x] Character frequency map
- [x] Frequency array for lowercase letters
- [ ] Group anagrams (sorted string or frequency tuple as the key)
- [ ] Ransom note — can one string be built from the letters of another?
- [ ] Find the difference (the extra character between two strings)
- [ ] Word frequency count in a sentence
- [ ] Top k frequent words
- [ ] Check whether two strings are one edit apart

## 🔵 Level 5 — String Building & Parsing

- [ ] String compression (`"aabcccccaaa"` → `"a2b1c5a3"`)
- [ ] Run-length encoding and decoding
- [ ] Roman numeral → integer
- [ ] Integer → Roman numeral
- [ ] `atoi` — string to integer with sign and whitespace handling
- [ ] Add two numbers given as digit strings (no int conversion)
- [ ] Multiply two number strings
- [ ] Valid parentheses (stack)
- [ ] Remove adjacent duplicates (stack)

## 🔵 Level 6 — Advanced (much later)

- [ ] Naive pattern matching, and why it is O(n*m)
- [ ] KMP / prefix function
- [ ] Rabin-Karp rolling hash
- [ ] Z-algorithm
- [ ] Trie basics (prefix insert / search)
- [ ] Edit distance (DP)
- [ ] Longest common subsequence (DP)

---

## 🐞 Fixes to revisit

- [x] `strings.py` — `max_vowels()`: first-window loop fixed to
      `for i in range(k)`. Verified: `max_vowels("abciiidef", 3)` now returns 3.
- [ ] `strings.py` — `is_anagram_using_Frequency_array()` assumes lowercase a–z.
      Note the assumption in a comment, or guard it, so it is not reused blindly
      on mixed-case or non-letter input
- [ ] `strings.py` — `max_sum_arrays()` is an *array* function living in the
      strings file. Move it next to the array code, or keep one clearly labelled
      sliding-window section, so the pattern has a single home
- [ ] `strings.py` — the top ~55 lines are commented-out scratch work. Convert
      the useful ones into functions (the same cleanup already noted for
      `arrays.py`)

---

## ⭐ Must-Solve Before Moving On

- [x] Valid Anagram
- [x] Valid Palindrome
- [x] Reverse String
- [x] Reverse Vowels of a String
- [x] Longest Substring Without Repeating Characters
- [ ] Longest Repeating Character Replacement
- [ ] Find All Anagrams in a String
- [ ] Group Anagrams
- [ ] Longest Common Prefix
- [ ] Valid Parentheses
- [ ] String Compression
- [ ] Is Subsequence
- [ ] Longest Palindromic Substring

---

## 🎯 Core Patterns to Master

- [x] Character-by-character scan with an accumulator
- [x] Frequency map / frequency array
- [x] Two pointers — opposite ends converging
- [x] Two pointers — skip characters failing a predicate
- [x] Sliding window — fixed size
- [x] Sliding window — variable size (expand right, shrink left)
- [ ] Window + frequency map compared against a target map
- [ ] Stack for matching / adjacent-pair elimination
- [ ] Expand around centre (palindromic substrings)
- [ ] Building strings efficiently with a list + `join()`

---

### Current assessment

**What is genuinely solid:** the two-pointer string set. Palindrome, valid
palindrome with alphanumeric filtering, reverse via list, and reverse vowels are
all done — and reverse vowels in particular is the one people usually get wrong
on the convergence edge case, which is now fixed. Both anagram approaches (hash
map and 26-slot frequency array) are written, which is the right way to learn it.
Sliding window is also solid now: fixed-size (`max_sum_arrays`, fixed `max_vowels`)
and the two core variable-size templates (`longest_unique_substring`,
`longest_at_most_k_distinct`) are all written and verified.

**The real gaps, in priority order:**

1. **Window + frequency map** — Find All Anagrams, Permutation in String. This
   is where the anagram work and the window work combine.
2. **String building / parsing** — compression, valid parentheses, Roman
   numerals. A different muscle from the pointer work, and asked constantly.
3. **Python string methods** — split / join / slicing. Everything so far is
   manual loops, which is good for learning but slow to write under time
   pressure.
4. **Level 1 easy classics still open** — first non-repeating character,
   reverse words, longest common prefix, isomorphic strings.

**Suggested order:**

> Longest repeating character replacement → find all anagrams → group
> anagrams → valid parentheses → string compression → longest palindromic
> substring

Sliding window is shared with the arrays checklist — clearing it here clears the
matching gap there too.

**Legend:** `[x]` done · `[ ]` not started · `[~]` written but not yet correct
