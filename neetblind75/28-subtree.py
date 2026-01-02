# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
#
# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.
#
# Example 1:
#
# Input: root = [1,2,3,4,5], subRoot = [2,4,5]
#
# Output: true
#
# Example 2:
#
# Input: root = [1,2,3,4,5,null,null,6], subRoot = [2,4,5]
#
# Output: false
#
# Constraints:
#
#     1 <= The number of nodes in both trees <= 100.
#     -100 <= root.val, subRoot.val <= 100
#
# Recommended Time & Space Complexity
#
# You should aim for a solution as good or better than O(m * n) time and O(m + n) space, where n and m are the number of nodes in root and subRoot, respectively.
#

from typing import Optional
from tools import TreeNode
import pytest

class Solution:   
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        return (p.val == q.val) and (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if self.isSameTree(root, subRoot):
            return True
        if root.left:
            if self.isSubtree(root.left, subRoot):
                return True
        if root.right:
            if self.isSubtree(root.right, subRoot):
                return True
        return False


@pytest.mark.parametrize("p,q,expected", [
    ([1,2,3,4,5], [2,4,5], True),
    ([1,2,3,4,5,None,None,6], [2,4,5], False),
])

def test_is_subtree(p, q, expected):
    sol = Solution()
    assert sol.isSubtree(TreeNode.list_to_tree(p), TreeNode.list_to_tree(q)) == expected
