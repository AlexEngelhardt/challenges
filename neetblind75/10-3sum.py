# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.
#
# The output should not contain any duplicate triplets. You may return the output and the triplets in any order.
#
# Example 1:
#
# Input: nums = [-1,0,1,2,-1,-4]
#
# Output: [[-1,-1,2],[-1,0,1]]
#
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
#
# Example 2:
#
# Input: nums = [0,1,1]
#
# Output: []
#
# Explanation: The only possible triplet does not sum up to 0.
#
# Example 3:
#
# Input: nums = [0,0,0]
#
# Output: [[0,0,0]]
#
# Explanation: The only possible triplet sums up to 0.
#
# Constraints:
#
#     3 <= nums.length <= 1000
#     -10^5 <= nums[i] <= 10^5
#

from typing import List
import pytest

class Solution:
    def threeSum_ON3(self, nums: List[int]) -> List[List[int]]:
        # This is an O(N^3) solution

        results = []

        for i_1 in range(len(nums)-2):
            for i_2 in range(i_1+1, len(nums)-1):
                for i_3 in range(i_2+1, len(nums)):
                    num_1 = nums[i_1]
                    num_2 = nums[i_2]
                    num_3 = nums[i_3]
                    if num_1+num_2+num_3 == 0:
                        # match is already sorted and we don't need this line.
                        match = sorted([num_1, num_2, num_3])
                        if not match in results:  # Only add if nonduplicate
                            results.append(match)

        return results

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # twoSum was O(n) time and O(n) space and worked with a dictionary num_to_idx (goal was to return the two indices
        # Here, O(n^2) time is okay, but try for O(1) space
        nums.sort()
        results = []

        for i_target in range(len(nums)-2):
            target = nums[i_target]
            i_left = i_target+1
            i_right = len(nums)-1
            while i_left < i_right:
                if nums[i_left] + nums[i_right] == -target:
                    # The numbers in 'match' are already sorted
                    match = [target, nums[i_left], nums[i_right]]
                    if match not in results:
                        results.append(match)
                    i_left += 1
                    i_right -= 1
                elif nums[i_left] + nums[i_right] < -target:
                    i_left += 1
                elif nums[i_left] + nums[i_right] > -target:
                    i_right -= 1
                else:
                    raise Exception("This should never be reached")

        return results


@pytest.mark.parametrize("input,expected_output", [
    ([-1,0,1,2,-1,-4], [[-1,-1,2],[-1,0,1]]),
    ([0,1,1], []),
    ([0,0,0], [[0,0,0]]),
])
def test_three_sum(input, expected_output):
    sol = Solution()
    result = sol.threeSum(input)
    result = sorted([sorted(x) for x in result])
    expected_output = sorted([sorted(x) for x in expected_output])
    assert result == expected_output
