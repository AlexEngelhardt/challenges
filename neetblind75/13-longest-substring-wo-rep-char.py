# Given a string s, find the length of the longest substring without duplicate characters.
#
# A substring is a contiguous sequence of characters within a string.
#
# Example 1:
#
# Input: s = "zxyzxyz"
#
# Output: 3
#
# Explanation: The string "xyz" is the longest without duplicate characters.
#
# Example 2:
#
# Input: s = "xxxx"
#
# Output: 1
#
# Constraints:
#
#     0 <= s.length <= 1000
#     s may consist of printable ASCII characters.
#

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        window_start = 0
        while window_start < len(s):
            seen_characters = set()
            this_window_length = 0
            window_end = window_start
            while window_end < len(s):
                if s[window_end] not in seen_characters:
                    this_window_length += 1
                    seen_characters.add(s[window_end])
                    window_end += 1
                    if this_window_length > max_length:
                        max_length = this_window_length
                    if window_end == len(s):
                        # exit all loops == set window_start to len(s)
                        window_start = len(s)+1
                else:
                    # window_start = window_end  # this fails for s="dvdf" e.g.
                    window_start += 1  # This is inefficient though.
                    break
        return max_length


def test_lols():
    sol = Solution()
    assert sol.lengthOfLongestSubstring("zxyzxyz") == 3
    assert sol.lengthOfLongestSubstring("xxxx") == 1
    assert sol.lengthOfLongestSubstring("x") == 1
    assert sol.lengthOfLongestSubstring(" ") == 1
    assert sol.lengthOfLongestSubstring("") == 0
    assert sol.lengthOfLongestSubstring("dvdf") == 3
