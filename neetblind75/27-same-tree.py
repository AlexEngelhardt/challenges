# Given the roots of two binary trees p and q, return true if the trees are equivalent, otherwise return false.
#
# Two binary trees are considered equivalent if they share the exact same structure and the nodes have the same values.
#
# Example 1:
#
# Input: p = [1,2,3], q = [1,2,3]
#
# Output: true
#
# Example 2:
#
# Input: p = [4,7], q = [4,null,7]
#
# Output: false
#
# Example 3:
#
# Input: p = [1,2,3], q = [1,3,2]
#
# Output: false
#
# Recommended Time & Space Complexity
#
# You should aim for a solution with O(n) time and O(n) space, where n is the number of nodes in the tree.

from typing import Optional
import pytest
from tools import TreeNode

class Solution:
    # This corresponds to the 'recursive' solution on neetcode (but a bit less clean).
    # There is also a Iterative DFS solution and a BFS solution
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (p is None and q is not None) or (p is not None and q is None):
            # quit if only one tree is None
            return False
        if p is None and q is None:
            return True
        if p.val != q.val:  # early quit if the current root node value differs
            return False
        if (p.left is None and p.right is None
                and q.left is None and q.right is None):
            # root node in both trees
            return p.val == q.val

        # else: root node values equal AND both trees have children
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


@pytest.mark.parametrize("p,q,expected", [
    ([1,2,3], [1,2,3], True),
    ([4,7], [4, None, 7], False),
    ([1,2,3], [1,3,2], False),
])
def test_max_depth(p, q, expected):
    sol = Solution()
    assert sol.isSameTree(TreeNode.list_to_tree(p), TreeNode.list_to_tree(q)) == expected
