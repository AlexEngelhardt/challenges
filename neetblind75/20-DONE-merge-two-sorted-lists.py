from typing import Optional
import pytest
from tools import ListNode

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


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        if list1.val < list2.val:
            new_head = list1
            curr = list1
            list1_next = list1.next
            list2_next = list2
        else:
            new_head = list2
            curr = list2
            list1_next = list1
            list2_next = list2.next

        while list1_next is not None or list2_next is not None:
            # TODO I think we can do this recursively!
            # TODO and the current solution can be written much more concisely and prettily.
            
            # If one of the rest-lists is None, just append the other one and you're done.
            if list1_next is None:
                curr.next = list2_next
                list2_next = None  # so that the while loop exits after this iteration
            elif list2_next is None:
                curr.next = list1_next
                list1_next = None

            elif list1_next.val < list2_next.val:
                curr.next = list1_next
                curr = list1_next
                list1_next = list1_next.next
            else:  # i.e. list1_next >= list2_next
                curr.next = list2_next
                curr = list2_next
                list2_next = list2_next.next

        return new_head

@pytest.mark.parametrize("list1, list2, expected", [
    ([1,2,4], [1,3,5], [1,1,2,3,4,5]),
    ([4,6,8], [1], [1,4,6,8]),
    ([], [1,4], [1,4]),
    ([], [], []),
])
def test_merge_two_lists(list1, list2, expected):
    sol = Solution()

    merged_ll = sol.mergeTwoLists(ListNode.list_to_ll(list1), ListNode.list_to_ll(list2))
    # import ipdb; ipdb.set_trace()
    merged_list = ListNode.ll_head_to_list(merged_ll)
    assert merged_list == expected 
