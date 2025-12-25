# You are given the heads of two sorted linked lists list1 and list2.
#
# Merge the two lists into one sorted linked list and return the head of the new sorted linked list.
#
# The new list should be made up of nodes from list1 and list2.
#
# Example 1:
#
# Input: list1 = [1,2,4], list2 = [1,3,5]
#
# Output: [1,1,2,3,4,5]
#
# Example 2:
#
# Input: list1 = [], list2 = [1,2]
#
# Output: [1,2]
#
# Example 3:
#
# Input: list1 = [], list2 = []
#
# Output: []
#
# Constraints:
#
#     0 <= The length of the each list <= 100.
#     -100 <= Node.val <= 100
#
# You should aim for a solution with O(n + m) time and O(1) space, where n is the length of list1 and m is the length of list2.
#

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dur

def test_merge_two_lists():
    sol = Solution()
    assert sol.mergeTwoLists([1, 2, 4], [1, 3, 5]) == [1,1,2,3,4,5] 
