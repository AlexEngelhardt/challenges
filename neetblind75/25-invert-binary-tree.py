# You are given the root of a binary tree root. Invert the binary tree and return its root.
#
# Example 1:
#
# Input: root = [1,2,3,4,5,6,7]
#
# (This tree has top root 1, then 2nd layer is 2,3, then 3rd layer is v.l.n.r. 4567
#
# Output: [1,3,2,7,6,5,4]
#
# Example 2:
#
# Input: root = [3,2,1]
#
# Output: [3,1,2]
#
# Example 3:
#
# Input: root = []
#
# Output: []
#
# Constraints:
#
#     0 <= The number of nodes in the tree <= 100.
#     -100 <= Node.val <= 100
#

from typing import Optional
from tools import TreeNode


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root or not root.right and not root.left:
            return root
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root


def test_invert_tree():
    sol = Solution()
    assert TreeNode.tree_to_list(sol.invertTree(TreeNode.list_to_tree([1,2,3,4,5,6,7]))) == [1,3,2,7,6,5,4]
