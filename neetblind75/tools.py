from __future__ import annotations
from collections import deque

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def list_to_ll(cls, list_in) -> ListNode:
        if not list_in:
            return None
        return cls(val=list_in[0], next=cls.list_to_ll(list_in[1:]))
    
    @staticmethod
    def ll_head_to_list(head):
        if not head:
            return []
        res = [head.val]
        while head.next:
            res.append(head.next.val)
            head = head.next
        return res


def test_list_to_ll():
    in_list = [1, "aa", 3.14]
    ll = ListNode.list_to_ll(in_list)
    assert ll.val == 1
    assert ll.next.val == "aa"
    assert ll.next.next.val == 3.14
    assert ll.next.next.next is None

def test_ll_head_to_list():
    in_list = [1, "aa", 3.14]
    ll = ListNode.list_to_ll(in_list)

    converted_list = ListNode.ll_head_to_list(ll)
    assert converted_list == in_list


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def list_to_tree(cls, list_in) -> TreeNode:
        queue = deque()
        root = cls(list_in.pop(0))
        queue.append(root)
        while list_in:
            parent = queue.popleft()
            parent.left = cls(list_in.pop(0))
            queue.append(parent.left)
            if list_in:
                parent.right = cls(list_in.pop(0))
                queue.append(parent.right)
        return root

    @staticmethod
    def tree_to_list(head):
        # TODO this function is not pretty, but it works for simple trees and at least the easy problems here
        nodequeue = deque()
        res = deque()
        res.append(head.val)
        nodequeue.append(head.left)
        nodequeue.append(head.right)

        while nodequeue:
            curr = nodequeue.popleft()
            if curr:
                res.append(curr.val)
                nodequeue.append(curr.left)
                nodequeue.append(curr.right)

        return list(res)

def test_list_to_tree():
    list_in = [1,2,3,4,5,6,7]
    tree = TreeNode.list_to_tree(list_in)
    assert tree.val == 1
    assert tree.left.val == 2
    assert tree.right.val == 3
    assert tree.left.left.val == 4
    assert tree.left.left.left is None
    assert tree.left.right.val == 5
    assert tree.right.left.val == 6
    assert tree.right.right.val == 7
    assert tree.right.right.left is None

def test_tree_to_list():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    list_out = TreeNode.tree_to_list(root)
    assert list_out == [1,2,3,4,5,6,7]

