# Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), determine if a person could add all meetings to their schedule without any conflicts.
#
# Note: (0,8),(8,10) is not considered a conflict at 8
#
# Example 1:
#
# Input: intervals = [(0,30),(5,10),(15,20)]
#
# Output: false
#
# Explanation:
#
#     (0,30) and (5,10) will conflict
#     (0,30) and (15,20) will conflict
#
# Example 2:
#
# Input: intervals = [(5,8),(9,15)]
#
# Output: true
#
# Constraints:
#
#     0 <= intervals.length <= 500
#     0 <= intervals[i].start < intervals[i].end <= 1,000,000
#
# Recommended Time & Space Complexity
#
# You should aim for a solution with O(nlogn) time and O(n) space, where n is the size of the input array.

from tools import Interval
from typing import List
import pytest

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)  # sort by start date
        for i in range(1, (len(intervals))):
            if intervals[i].start < intervals[i-1].end:
                return False
        return True

@pytest.mark.parametrize("ivl_list,expected", [
    ([(0,30),(5,10),(15,20)], False),
    ([(5,8),(9,15)], True),
    ([(5,9),(9,15)], True),
    ([(1,5),(1,3)], False),
])
def test_can_attend_meetings(ivl_list, expected):
    sol = Solution()
    list_of_ivls = [Interval.from_tuple(x_i) for x_i in ivl_list]
    assert sol.canAttendMeetings(list_of_ivls) == expected
