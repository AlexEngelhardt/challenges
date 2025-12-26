# Given the beginning of a linked list head, return true if there is a cycle in the linked list. Otherwise, return false.
#
# There is a cycle in a linked list if at least one node in the list can be visited again by following the next pointer.
#
# Internally, index determines the index of the beginning of the cycle, if it exists. The tail node of the list will set it's next pointer to the index-th node. If index = -1, then the tail node points to null and no cycle exists.
#
# Note: index is not given to you as a parameter.
#
# Example 1:
#
# Input: head = [1,2,3,4], index = 1
#
# Output: true
#
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
#
# Example 2:
#
# Input: head = [1,2], index = -1
#
# Output: false
#
# Constraints:
#
#     1 <= Length of the list <= 1000.
#     -1000 <= Node.val <= 1000
#     index is -1 or a valid index in the linked list.
#
# You should aim for a solution with O(n) time and O(1) space, where n is the length of the given list. 
#

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow_ptr = head
        fast_ptr = head

        while fast_ptr is not None:
            slow_ptr = slow_ptr.next
            if fast_ptr.next is None:
                # more elegant: rewrite the while condition to while fast_ptr and fast_ptr.next
                return False
            fast_ptr = fast_ptr.next.next
            if slow_ptr == fast_ptr:
                return True
        return False


# Testing: do later, b/c I'd need a function that transforms 
# head = [1,2,3,4], index = 1
# into a LL where node 4's next is 2. Mendoukusai naa.
