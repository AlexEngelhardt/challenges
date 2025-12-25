import pytest
from typing import Optional
from tools import ListNode

# Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.
#
# Example 1:
#
# Input: head = [0,1,2,3]
#
# Output: [3,2,1,0]
#
# Example 2:
#
# Input: head = []
#
# Output: []
#
# Constraints:
#
#     0 <= The length of the list <= 1000.
#     -1000 <= Node.val <= 1000
#
# You should aim for a solution with O(n) time and O(1) space, where n is the length of the given list.

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # This elegantly works for an empty list (head==None) or a list of length 1 too!:w

        previous_node = None
        this_node = head
        # next_node = head.next # not needed, right?

        while this_node is not None:
            next_node = this_node.next  # buffer the next node

            # update 'next' of the current node
            this_node.next = previous_node

            # move both pointers one forward:
            previous_node = this_node
            this_node = next_node
        
        return previous_node  # this, not 'this_node', is the last (new: first) node


@pytest.mark.parametrize("test_input,expected", [
    ([0,1,2,3], [3,2,1,0]),
    ([3], [3]),
    ([], []),
])
def test_reverse_list(test_input, expected):
    sol = Solution()
    # import ipdb; ipdb.set_trace()
    assert ListNode.ll_head_to_list(sol.reverseList(ListNode.list_to_ll(test_input))) == expected

