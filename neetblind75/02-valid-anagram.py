# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
#
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
#
# Example 1:
#
# Input: s = "racecar", t = "carrace"
#
# Output: true
#
# Example 2:
#
# Input: s = "jar", t = "jam"
#
# Output: false
#
# Constraints:
#
#     s and t consist of lowercase English letters.
#

from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)

        for char in s:
            s_dict[char] += 1
        for char in t:
            t_dict[char] += 1
        
        return s_dict == t_dict

