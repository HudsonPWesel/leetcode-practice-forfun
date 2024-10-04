from collections import defaultdict
from typing import List
# input: strs = ["act","pots","tops","cat","stop","hat"]Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]


# Reattmpt of groupAnagrams
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    res = defaultdict(list)
    for s in strs:
        key = [0] * 26
        for l in s:
            key[ord(l) - ord('a')] += 1
        res[tuple(key)].append(s)
        print(res[tuple(key)])
    return res.values()
