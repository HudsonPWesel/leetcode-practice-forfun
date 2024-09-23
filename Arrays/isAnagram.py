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
    s_chars, t_chars = {}, {}
    for i in range(0, len(s)):
        s_chars[s[i]] = 1 + s_chars.get(s[i], 0)
        t_chars[t[i]] = 1 + t_chars.get(t[i], 0)
    for key in s_chars:
        if s_chars[key] != t_chars.get(key, 0):
            return False
    return True
    '''for i in range(len(s)):
        if s[i] != t[len(s) - (1 + i)]:
            return False'''


print(isAnagram('anagram', 'nagaram'))
