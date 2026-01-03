# You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.
#
# The input string s is valid if and only if:
#
#     Every open bracket is closed by the same type of close bracket.
#     Open brackets are closed in the correct order.
#     Every close bracket has a corresponding open bracket of the same type.
#
# Return true if s is a valid string, and false otherwise.
#
# Example 1:
#
# Input: s = "[]"
#
# Output: true
#
# Example 2:
#
# Input: s = "([{}])"
#
# Output: true
#
# Example 3:
#
# Input: s = "[(])"
#
# Output: false
#
# Explanation: The brackets are not closed in the correct order.
#
# Constraints:
#
#     1 <= s.length <= 1000
#

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        open_chars = set(("(", "[", "{"))
        close_chars = set((")", "]", "}"))
        close_to_open = {")": "(", "]": "[", "}": "{"}

        for char in s:
            if char in open_chars:
                stack.append(char)
            elif char in close_chars:
                if len(stack) == 0:  # i.e. more close-chars than open-chars in that string
                    return False
                if stack[-1] == close_to_open[char]:
                    stack.pop()
                else:
                    return False
            else:
                raise ValueError("Unexpected char in string")
        
        return len(stack) == 0

