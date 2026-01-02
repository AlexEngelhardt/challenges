# You are given an unsigned integer n. Return the number of 1 bits in its binary representation.
#
# You may assume n is a non-negative integer which fits within 32-bits.
#
# Example 1:
#
# Input: n = 00000000000000000000000000010111
#
# Output: 4
#
# Example 2:
#
# Input: n = 01111111111111111111111111111101
#
# Output: 30

import pytest

class Solution:
    def hammingWeight(self, n: int) -> int:
        # You could use bin(n):
        # return sum([1 for x in bin(n)[2:] if x == '1'])

        # but use bit-operators instead for practice:
        count = 0
        while n:
            if n % 2:
                count += 1
            n = n >> 1
        return count
        # There's a more optimal solution using n = n & (n-1).

@pytest.mark.parametrize("n,expected", [(23, 4), (2147483645, 30)])
def test_hamming_weight(n, expected):
    sol = Solution()
    assert sol.hammingWeight(n) == expected
