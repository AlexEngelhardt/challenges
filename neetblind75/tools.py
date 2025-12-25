from __future__ import annotations

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
