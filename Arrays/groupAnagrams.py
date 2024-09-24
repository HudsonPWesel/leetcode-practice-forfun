from typing import List
# input: strs = ["act","pots","tops","cat","stop","hat"]Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    current_word_letters = {}
    subsequent_word_letters = {}
    anagram_groups = []
    current_anagram_grouping = []
    should_group_anagram = True
    current_remaining_word_index = 0
    for current_word_index in range(len(strs) - 1):
        for letter in strs[current_word_index]:
            current_word_letters[letter] = current_word_letters.get(
                letter, 0) + 1
        for current_remaining_word_index in range(current_word_index + 1, len(strs)):
            for letter in strs[current_remaining_word_index]:
                subsequent_word_letters[letter] = subsequent_word_letters.get(
                    letter, 0) + 1

            # Checking if next anagram is false
            for letter in current_word_letters:
                if current_word_letters[letter] != subsequent_word_letters.get(letter, 0):
                    should_group_anagram = False
            if should_group_anagram:
                current_anagram_grouping.append(strs[current_word_index])

            should_group_anagram = True
            subsequent_word_letters = {}
            current_remaining_word_index = current_word_index + 1

        if len(current_anagram_grouping) > 0:
            current_anagram_grouping.append(strs[current_remaining_word_index])

        anagram_groups.append(current_anagram_grouping)
        current_anagram_grouping = []

    return anagram_groups


print(groupAnagrams(["act", "pots", "tops", "cat", "stop", "hat"]))
