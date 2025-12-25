# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
#
# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
#
# Return the answer with the smaller index first.
#
# Example 1:
#
# Input: 
# nums = [3,4,5,6], target = 7
#
# Output: [0,1]
#
# Explanation: nums[0] + nums[1] == 7, so we return [0, 1].
#
# Example 2:
#
# Input: nums = [4,5,6], target = 10
#
# Output: [0,2]
#
# Example 3:
#
# Input: nums = [5,5], target = 10
#
# Output: [0,1]
#
# Constraints:
#
#     2 <= nums.length <= 1000
#     -10,000,000 <= nums[i] <= 10,000,000
#     -10,000,000 <= target <= 10,000,000
#     Only one valid answer exists.
#
# Recommended Time & Space Complexity
#
# You should aim for a solution with O(n) time and O(n) space, where n is the size of the input array.
#

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_idx = dict()
        for i in range(len(nums)):
            if target - nums[i] in num_to_idx:
                return [num_to_idx[target - nums[i]], i]
            num_to_idx[nums[i]] = i


import pytest
def test_twosum():
    sol = Solution()
    assert sol.twoSum([3,4,5,6], 7) == [0, 1]
    assert sol.twoSum([4,5,6], 10) == [0,2]
    assert sol.twoSum([5,5], 10) == [0,1]

# def test_thisfails():
#     assert 2 == 3

