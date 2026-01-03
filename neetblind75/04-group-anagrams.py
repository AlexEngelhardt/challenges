# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
#
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
#
# Example 1:
#
# Input: strs = ["act","pots","tops","cat","stop","hat"]
#
# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
#
# Example 2:
#
# Input: strs = ["x"]
#
# Output: [["x"]]
#
# Example 3:
#
# Input: strs = [""]
#
# Output: [[""]]
#
# Constraints:
#
#     1 <= strs.length <= 1000.
#     0 <= strs[i].length <= 100
#     strs[i] is made up of lowercase English letters.
#

from typing import List
import pytest
from typing import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for word in strs:
            result["".join(sorted(word))].append(word)
        return list(result.values())

@pytest.mark.parametrize("in_list,expected_out_list",[
    (["act","pots","tops","cat","stop","hat"],[["hat"],["act", "cat"],["stop", "pots", "tops"]]),
    (["x"], [["x"]]),
    ([""], [[""]]),
])
def test_group_anagrams(in_list, expected_out_list):
    sol = Solution()
    result = sol.groupAnagrams(in_list)
    result = sorted([sorted(x) for x in result])
    expected_out_list = sorted([sorted(x) for x in expected_out_list])
    assert result == expected_out_list
