# Given an array nums containing n integers in the range [0, n] without any duplicates, return the single number in the range that is missing from nums.
#
# Follow-up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?
#
# Example 1:
#
# Input: nums = [1,2,3]
#
# Output: 0
#
# Explanation: Since there are 3 numbers, the range is [0,3]. The missing number is 0 since it does not appear in nums.
#
# Example 2:
#
# Input: nums = [0,2]
#
# Output: 1
#
# Constraints:
#
#     1 <= nums.length <= 1000
#

from typing import List
import pytest

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # This is Gauss' algorithm! The sum from 1 to n is (n+1) * n / 2.
        # 1 - 100 was 5050. That is 101 * 50.
        # Subtract each num from that sum, the remainder is the missing number.
        n = len(nums)
        # The 0 doesn't matter, it won't contribute to the sum.
        target = (n+1)*n/2
        for n_i in nums:
            target -= n_i
        return int(target)  # cast to int so 0.0 doesn't throw a TypeError


def test_missing_number():
    sol = Solution()
    assert sol.missingNumber([1, 2, 3]) == 0
    assert sol.missingNumber([0, 2]) == 1

