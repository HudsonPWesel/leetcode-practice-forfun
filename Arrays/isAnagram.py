'''
Given two strings s and t, return true if t is an
anagram
 of s, and false otherwise.



Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false'''


def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    s_letters = {}
    t_letters = {}

    for i in range(len(s)):
        s_letters[s[i]] = s_letters.get(s[i], 0) + 1
        t_letters[t[i]] = t_letters.get(t[i], 0) + 1

    for letter in s_letters:
        if t_letters.get(letter, 0) != s_letters.get(letter, 0):
            return False
    return True
    # return sort(s) == sort(t)


print(isAnagram('anagram', 'nagaram'))
print(isAnagram('cat', 'rat'))
