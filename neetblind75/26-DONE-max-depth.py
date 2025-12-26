# Given the root of a binary tree, return its depth.
#
# The depth of a binary tree is defined as the number of nodes along the longest path from the root node down to the farthest leaf node.
#
# Example 1:
#
# Input: root = [1,2,3,null,null,4]
#
# Output: 3
#
# Example 2:
#
# Input: root = []
#
# Output: 0
#
# Target time and space complexity: both O(n)

from typing import Optional
from tools import TreeNode
import pytest

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

@pytest.mark.parametrize("in_list,expected", [([1,2,3,None,None,4], 3), ([], 0)])
def test_max_depth(in_list, expected):
    sol = Solution()
    assert sol.maxDepth(TreeNode.list_to_tree(in_list)) == expected

