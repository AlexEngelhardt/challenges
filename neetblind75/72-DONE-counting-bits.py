# Given an integer n, count the number of 1's in the binary representation of every number in the range [0, n].
#
# Return an array output where output[i] is the number of 1's in the binary representation of i.
#
# Example 1:
#
# Input: n = 4
#
# Output: [0,1,1,2,1]
#
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
#
# Constraints:
#
#     0 <= n <= 1000
#

from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        # simple solution: for each i in 0:n, do the solution from 71.
        # but I suspect there's a faster solution
        result = [0] * (n+1)
        for i in range(0, n+1):
            result[i] = bin(i).count("1")
        return result



def test_count_bits():
    assert Solution().countBits(4) == [0,1,1,2,1]
